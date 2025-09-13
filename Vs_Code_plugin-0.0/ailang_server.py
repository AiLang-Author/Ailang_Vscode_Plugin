from pygls.server import LanguageServer
from lsprotocol.types import (
    TextDocumentSyncKind, InitializeParams, CompletionParams, Diagnostic,
    CompletionItem, CompletionItemKind, Position, Range, DidOpenTextDocumentParams
)
from lexer import Lexer
from parser import Parser
import re
import os
import json
import tempfile

ailang_server = LanguageServer(name="AILangServer", version="1.0.0")

@ailang_server.feature("textDocument/didOpen")
def did_open(ls: LanguageServer, params: DidOpenTextDocumentParams):
    print("didOpen triggered")
    uri = params.text_document.uri
    text = params.text_document.text
    
    # Extract filename from URI
    filename = uri.split('/')[-1] if '/' in uri else uri.split('\\')[-1]
    
    # DEBUG: Save the content that VSCode sends us
    debug_path = os.path.join(tempfile.gettempdir(), f"vscode_content_{filename}")
    
    try:
        with open(debug_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"DEBUG: VSCode content saved to: {debug_path}")
    except Exception as e:
        print(f"DEBUG: Failed to save VSCode content: {e}")
    
    print(f"DEBUG: Processing file: {filename}")
    print(f"DEBUG: Content length: {len(text)} characters")
    print(f"DEBUG: First 100 chars: {repr(text[:100])}")
    print(f"DEBUG: Last 100 chars: {repr(text[-100:])}")
    
    # Check for exclamation marks in VSCode content
    exclamation_positions = []
    for i, char in enumerate(text):
        if char == '!':
            line_num = text[:i].count('\n') + 1
            col_num = i - text.rfind('\n', 0, i)
            exclamation_positions.append((line_num, col_num, i))
    
    if exclamation_positions:
        print(f"DEBUG: Found {len(exclamation_positions)} exclamation marks in VSCode content:")
        for line_num, col_num, pos in exclamation_positions:
            print(f"  Line {line_num}, Column {col_num}, Position {pos}")
            # Show context around each exclamation mark
            start = max(0, pos - 20)
            end = min(len(text), pos + 20)
            context = text[start:end]
            print(f"    Context: {repr(context)}")
    else:
        print("DEBUG: No exclamation marks found in VSCode content")
    
    # Check for any non-ASCII characters that might cause issues
    non_ascii_chars = []
    for i, char in enumerate(text):
        if ord(char) > 127:
            line_num = text[:i].count('\n') + 1
            col_num = i - text.rfind('\n', 0, i)
            non_ascii_chars.append((line_num, col_num, i, char, ord(char)))
    
    if non_ascii_chars:
        print(f"DEBUG: Found {len(non_ascii_chars)} non-ASCII characters:")
        for line_num, col_num, pos, char, char_code in non_ascii_chars[:10]:  # Show first 10
            print(f"  Line {line_num}, Column {col_num}: '{char}' (U+{char_code:04X})")
    
    diagnostics = []
    try:
        # Create lexer with debugging enabled
        print(f"DEBUG: Creating lexer for {filename}")
        lexer = Lexer(text)
        
        # Add debugging to lexer if it doesn't have it
        if hasattr(lexer, 'debug_filename'):
            lexer.debug_filename = filename
        
        print(f"DEBUG: Starting tokenization")
        tokens = lexer.tokenize()
        print(f"DEBUG: Tokenization successful, got {len(tokens)} tokens")
        
        # NEW: Extract lexer warnings as diagnostics
        if hasattr(lexer, 'diagnostics'):
            print(f"DEBUG: Found {len(lexer.diagnostics)} lexer warnings")
            for warning in lexer.diagnostics:
                diagnostics.append(Diagnostic(
                    range=Range(
                        start=Position(line=warning["line"] - 1, character=warning["column"] - 1),
                        end=Position(line=warning["line"] - 1, character=warning["column"] + 10)
                    ),
                    message=warning["message"],
                    severity=warning["severity"],  # 2 = Warning
                    source="ailang-lexer",
                    code="identifier_length"
                ))
        else:
            print("DEBUG: Lexer doesn't have diagnostics collection yet")
        
        print(f"DEBUG: Creating parser")
        parser = Parser(tokens)
        print(f"DEBUG: Starting parsing")
        ast = parser.parse()
        print(f"DEBUG: Parsing successful")
        
    except Exception as e:
        print(f"=== PARSE ERROR DEBUG ===")
        print(f"File: {filename}")
        print(f"Error: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        
        # Try to extract line/column info from error message
        line, column = 0, 0
        error_msg = str(e)
        match = re.search(r'line (\d+)', error_msg)
        if match:
            line = int(match.group(1)) - 1
            print(f"Extracted line: {line + 1}")
        
        match = re.search(r'column (\d+)', error_msg)
        if match:
            column = int(match.group(1)) - 1
            print(f"Extracted column: {column + 1}")
        
        # Show the problematic line if we can find it
        if line < len(text.split('\n')):
            lines = text.split('\n')
            problematic_line = lines[line] if line < len(lines) else ""
            print(f"Problematic line {line + 1}: {repr(problematic_line)}")
            
            if column < len(problematic_line):
                print(f"Character at error position: '{problematic_line[column]}' (ord: {ord(problematic_line[column])})")
        
        # Show context around the error position if we can calculate it
        if line > 0 and column > 0:
            # Calculate absolute position in text
            lines_before = text.split('\n')[:line]
            char_position = sum(len(l) + 1 for l in lines_before) + column  # +1 for newlines
            
            if 0 <= char_position < len(text):
                start = max(0, char_position - 50)
                end = min(len(text), char_position + 50)
                context = text[start:end]
                print(f"Context around error: {repr(context)}")
                print(f"Error position marker: {' ' * (char_position - start)}^")
        
        print("=========================")
        
        diagnostics.append(Diagnostic(
            range=Range(start=Position(line=line, character=column), 
                       end=Position(line=line, character=column + 1)),
            message=error_msg,
            severity=1
        ))
    
    # Send all diagnostics (warnings + errors) to VSCode
    ls.publish_diagnostics(uri, diagnostics)
    print(f"DEBUG: Published {len(diagnostics)} diagnostics to VSCode")
    
@ailang_server.feature("textDocument/completion")
def completions(ls: LanguageServer, params: CompletionParams):
    print("Completion triggered")
    keywords = ["PrintMessage", "IfCondition", "WhileLoop", "Function", "FixedPool", "PageTable", "VirtualMemory", "Integer", "FloatingPoint", "True", "False"]
    extras = ["Initialize", "CanChange", "CanBeNull", "Range", "MaximumLength"]
    
    # Create function suggestions (with error handling for undefined library_functions)
    function_suggestions = []
    try:
        if 'library_functions' in globals():
            function_suggestions = [
                CompletionItem(label=name, kind=CompletionItemKind.Function, 
                             detail=f"{', '.join(f[0] for f in func.input_params)} -> {func.output_type.base_type if func.output_type else 'Void'}")
                for name, func in library_functions.items()
            ]
    except NameError:
        print("DEBUG: library_functions not defined, skipping function suggestions")
    
    return ([CompletionItem(label=k, kind=CompletionItemKind.Keyword) for k in keywords] + 
            [CompletionItem(label=e, kind=CompletionItemKind.Property) for e in extras] + 
            function_suggestions)

@ailang_server.feature("custom/showAST")
async def show_ast(ls: LanguageServer, params):
    print("showAST triggered")
    text = params.get('text')
    uri = params.get('uri')
    filename = uri.split('/')[-1] if uri else "unknown"
    
    try:
        print(f"DEBUG: Generating AST for {filename}")
        lexer = Lexer(text)
        if hasattr(lexer, 'debug_filename'):
            lexer.debug_filename = filename
            
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        ast_str = json.dumps(ast.to_dict(), indent=2) if hasattr(ast, 'to_dict') else str(ast)
        return {"ast": ast_str}
    except Exception as e:
        print(f"AST error for {filename}: {str(e)}")
        return {"ast": f"Error generating AST: {str(e)}"}

def load_library_files():
    """Load and parse library files with enhanced debugging"""
    library_dir = "/mnt/c/Users/Sean/Documents/AILANG_VSCode/VsCodeExtension"
    
    if not os.path.exists(library_dir):
        print(f"WARNING: Library directory not found: {library_dir}")
        return
    
    print(f"Loading library files from: {library_dir}")
    
    for file in os.listdir(library_dir):
        if file.endswith('.ailang') and "Library" in file:
            file_path = os.path.join(library_dir, file)
            print(f"Processing library file: {file}")
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                print(f"  Content length: {len(content)} characters")
                print(f"  First 100 chars: {repr(content[:100])}")
                
                print("  Creating lexer...")
                lexer = Lexer(content)
                
                print("  Starting tokenization...")
                tokens = lexer.tokenize()
                print(f"  Tokenization successful: {len(tokens)} tokens")
                
                print("  Creating parser...")
                parser = Parser(tokens)
                
                print("  Starting parsing...")
                result = parser.parse()
                print(f"✓ Successfully loaded {file}")
                
            except Exception as e:
                import traceback
                print(f"✗ Failed to parse {file}:")
                print(f"  Error: {str(e)}")
                print(f"  Error type: {type(e).__name__}")
                print("  Full traceback:")
                traceback.print_exc()
                print("-" * 50)

def main():
    print("=" * 50)
    print("AILang Language Server starting...")
    print("=" * 50)
    load_library_files()
    print("=" * 50)
    print("Server ready, starting I/O...")
    ailang_server.start_io()

if __name__ == '__main__':
    main()