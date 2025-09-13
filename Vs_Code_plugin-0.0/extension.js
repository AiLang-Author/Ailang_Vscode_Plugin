const vscode = require('vscode');
const { LanguageClient, LanguageClientOptions, ServerOptions } = require('vscode-languageclient/node');
const path = require('path');

let client;

function activate(context) {
    console.log('AILang extension activating...');
    const serverModule = context.asAbsolutePath(path.join('.', 'ailang_server.py'));
    const serverOptions = {
        run: { command: 'python3', args: [serverModule] },
        debug: { command: 'python3', args: [serverModule] }
    };

    const clientOptions = {
        documentSelector: [{ scheme: 'file', language: 'ailang' }],
        synchronize: {
            fileEvents: vscode.workspace.createFileSystemWatcher('**/*.{ailang,ail}')
        },
        initializationOptions: {}  // Ensure proper initialization
    };

    client = new LanguageClient('ailangServer', 'AILang Server', serverOptions, clientOptions);
    client.onDidChangeState((state) => {
        console.log(`Client state changed: ${state.newState}`);
    });
    client.start().then(() => {
        console.log('Language client started successfully');
    }).catch(err => {
        console.error('Language client failed to start:', err);
    });
    context.subscriptions.push(client);

    console.log('Registering commands...');
    context.subscriptions.push(
        vscode.commands.registerCommand('ailang.compile', () => {
            console.log('Command: ailang.compile triggered');
            const editor = vscode.window.activeTextEditor;
            if (editor && editor.document.languageId === 'ailang') {
                const filePath = editor.document.uri.fsPath;
                const terminal = vscode.window.createTerminal('AILang Compile');
                terminal.sendText(`echo "Compiling ${filePath} in user mode..."`);
                terminal.show();
            } else {
                vscode.window.showErrorMessage('No AILang file open for compilation.');
            }
        }),
        vscode.commands.registerCommand('ailang.compileKernel', () => {
            console.log('Command: ailang.compileKernel triggered');
            const editor = vscode.window.activeTextEditor;
            if (editor && editor.document.languageId === 'ailang') {
                const filePath = editor.document.uri.fsPath;
                const terminal = vscode.window.createTerminal('AILang Kernel Compile');
                terminal.sendText(`echo "Compiling ${filePath} in kernel mode..."`);
                terminal.show();
            } else {
                vscode.window.showErrorMessage('No AILang file open for kernel compilation.');
            }
        }),
        vscode.commands.registerCommand('ailang.showAST', async () => {
            console.log('Command: ailang.showAST triggered');
            const editor = vscode.window.activeTextEditor;
            if (editor && editor.document.languageId === 'ailang') {
                const doc = editor.document;
                const text = doc.getText();
                try {
                    const astResponse = await client.sendRequest('custom/showAST', { text: text, uri: doc.uri.toString() });
                    vscode.window.showInformationMessage('AST generated');
                    const panel = vscode.window.createOutputChannel('AILang AST');
                    panel.clear();
                    panel.append(astResponse.ast);
                    panel.show();
                } catch (error) {
                    vscode.window.showErrorMessage(`AST error: ${error.message}`);
                    console.error('AST request failed:', error);
                }
            } else {
                vscode.window.showErrorMessage('No AILang file open to show AST.');
            }
        }),
        vscode.commands.registerCommand('ailang.validate', () => {
            console.log('Command: ailang.validate triggered');
            vscode.window.showInformationMessage('Validate not implemented yet.');
        })
    );
    console.log('Commands registered successfully');
}

function deactivate() {
    if (client) client.stop();
}

module.exports = { activate, deactivate };