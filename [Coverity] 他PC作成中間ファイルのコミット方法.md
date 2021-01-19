### Coverity
### ベンダーが作成した中間ファイルをコミットする方法
 - ベンダーから入手した中間ファイルをそのままコミットすると次のエラーが出ます
 - エラーメッセージ：
   ```
   No emit DB found for this host ("PCA001") in C:/Users/hoge/Desktop/imd02/emit, but one was found for host "PCB001".
   ```
 - "PCB001" が、ベンダーさんのホストPCで、"PCA001" が自分のホストPCのためコミットできません
 - メッセージの続きにある通り、次のコマンドを実行しホスト名を変更してからコミットします
   ```
   Please run  
   cov-manage-emit --dir <intermediate-directory> reset-host-name
   ```
 - 実行例
   ```
   C:\Users\hoge\Desktop>cov-manage-emit --dir imd03 reset-host-name
   ```
 - これを実行すると、フォルダー名 `C:\Users\hoge\Desktop\imd01\emit\PCB001` が、`C:\Users\hoge\Desktop\imd01\emit\PCA001`　に書き換わります
 - 次に、コミットコマンドを実行します
   ```
   C:\Users\hoge\Desktop>cov-commit-defects --dir imd03 --stream ERMS --host xxx.xxx.xxx.xxx --user hoge --password yyyy
   ```
