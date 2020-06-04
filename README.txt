【Git操作方法】

------初期設定-------
Shellを開く
$git init
$git config --global user.name "ユーザー名(例:shoken ohshiro)"
$git config --global user.email "登録メールアドレス"
$git remote add origin https://gitlab.com/team01_system_dev/employeesystem.git
$git clone https://gitlab.com/team01_system_dev/employeesystem.git



------コード編集方法------

ローカルリポジトリに反映させる
　$git pull origin master
ブランチを切る
　$git branch "ブランチ名"

コード編集

ブランチをコミット
　$git add "ファイル名"
  $git commit -m "メッセージ"
ブランチの内容をプッシュ
  $git push origin "ブランチ名"

masterに変更内容を統合
　$git checkout master
　$git merge --no-ff "ブランチ名"
masterをプッシュ
  $git add "ファイル名(git statusで変更ファイルを確認)"
  $git commit -m "メッセージ"
  $git push origin master

Web上のGitLabで変更されているか確認


