# AiLang VS Code Extension

The official VS Code extension for AiLang, a verb-first programming language designed for clarity and concurrency.

## What This Extension Does

- **Syntax highlighting** with full grammar support
- **Language Server Protocol (LSP)** providing real-time diagnostics from the parser
- **AST explorer** to visualize program structure (`AiLang: Show AST` command)
- **Progressive shorthand system** - toggle between verbosity levels without modifying source files
- **Integrated debugging** - debug primitives are part of the language, not bolted on

## Language Features

### Core Design

AiLang uses verb-first syntax (`Function`, `LoopMain`, `SubRoutine`) to make program flow explicit. The language includes actor-based concurrency primitives (`LoopActor`, `LoopSend`, `LoopReceive`, `LoopJoin`) and resource management through pools (`DynamicPool`, `FilePool`).

### Progressive Shorthand

Write at whatever level of verbosity makes sense for your context:

- **Level 0**: Full canonical syntax
- **Level 1-2**: Common acronyms and operators
- **Level 3**: C-like brevity (`fn`, `->`, `if`, `else`)
- **Level 4**: Ultra-compressed for embedded/AI contexts

Switch levels in the editor without touching your `.ailang` files. See [The Philosophy of Progressive Shorthand](link) and the [mapping JSON](link) for details.

### Built-in Debugging

Debug features are language primitives, not afterthoughts:

- **Assertions**: `DebugAssert`, `DebugAssertRange`
- **Tracing**: Entry/exit/point markers
- **Memory**: Leak detection, watchpoints, memory dumps
- **Performance**: Cache stats, profiling markers
- **Breakpoints**: Conditional, counted, or data-triggered
- **Inspection**: Live view of pools, agents, stack, and variables

Full documentation: [Native Debug System Design](link)

## Language Server Features

The extension includes a Python-backed language server that provides:

- Real-time syntax validation
- Quick fixes for common patterns (dotted declarations, placeholders)
- AST visualization panel

## Experimental: C/C++ Import

We're working on tools to import existing C/C++ code into AiLang. The planned workflow:

1. Import `.c`/`.cpp` files
2. Generate equivalent AiLang structures
3. Use shorthand projections to ease the transition

This feature is early-stage but will eventually support dual-pane views and gradual refactoring from legacy code to AiLang idioms.

## Repository Structure

```
/extension.js                    # VS Code activation & AST command
/language-configuration.json     # Language config
/ailang.tmLanguage.json          # Syntax grammar
/ailang.json                     # Code snippets
/package.json                    # Extension manifest
/server.js                       # Language Server entry point
/bridge.py                       # Python bridge to compiler
/lexer.py, /parser.py            # Compiler frontend
/ailang_ast.py                   # AST definitions
/docs/                           # Language specifications
```

## Roadmap

**Current**: Full VS Code support with syntax highlighting, LSP diagnostics, AST explorer, and shorthand projection.

**Next**: Enhanced debug integration with inline values and memory visualization. Improved shorthand level switching UI.

**Future**: C/C++ import tools, remote debugging, concurrency analysis and visualization.

**Long-term**: Complete native toolchain (profiler, debugger, build system) with AI-assisted development features.

## Installation

```bash
git clone https://github.com/your-org/ailang-vscode
cd ailang-vscode
npm install
npm run package
code --install-extension ailang-vscode-0.1.0.vsix
```

## Contributing

We're particularly interested in contributions for:

- UI improvements for shorthand level switching
- Visualization tools for concurrency and debugging
- C/C++ to AiLang converter improvements

## Documentation

- [AiLang Language Specification](link)
- [Progressive Shorthand Philosophy](link)
- [Native Debug System Design](link)
- [Loop Concurrency Model](link)
