
# VS Code Dev Tips

### Manually install vscode server for remote ssh
1. Get the `commit_id` from Help -> About
2. Download with https://update.code.visualstudio.com/commit:${commit_id}/server-linux-x64/stable
3. scp the downloaded tar file to remote server.
4. Unpack into ~/.vscode-server/bin/${commit_id}/ directory.
```sh
cd ~/.vscode-server/bin/$COMMIT_ID
tar -xvzf vscode-server-linux-x64.tar.gz --strip-components 1
```


### Manually install vscode extensions in vscode server
1. Download the extension using the "Download" button next to the extensions in the marketplace. 
2. Use "Install from VSIX" option to install.