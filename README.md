# じゃんけんプロジェクト (Janken Project)

このリポジトリは、GitとGitHubの使い方を学ぶための練習用プロジェクトやで。

## 1. 環境構築 (Windows)
Gitをインストールして、初期設定を行った際の手順や。

### Gitのインストール
Windowsのパッケージマネージャー `winget` を使用してインストールしたで。
```powershell
winget install --id Git.Git -e --source winget
```

### Gitのユーザー設定
コミット時に記録される名前とメールアドレスを設定したで。
```powershell
git config --global user.name "yourname"
git config --global user.email "youremail"
```

## 2. ローカルリポジトリの作成
自分のPC内でGitの管理を開始した手順や。

1. **リポジトリの初期化**
   ```powershell
   git init
   ```
2. **ファイルの作成**
   `janken.py` を作成したで。
3. **ステージングとコミット**
   ファイルを保存対象（ステージ）に追加して、歴史を記録（コミット）した。
   ```powershell
   git add janken.py
   ```
   ```powershell
   git commit -m "Initial commit: Add simple janken game"
   ```

## 3. GitHubへのアップロード (Push)
ローカルの変更をGitHubに反映させた手順や。

1. **リモートリポジトリの登録**
   ```powershell
   git remote add origin https://github.com/fujiya-test/janken.git
   ```
2. **メインブランチ名を `main` に変更**
   ```powershell
   git branch -M main
   ```
3. **リモートからの取り込み（同期）**
   GitHub側に既にファイルがあった場合、一度取り込んで同期を合わせる必要がある。
   ```powershell
   git pull origin main --rebase
   ```
4. **プッシュ**
   ```powershell
   git push -u origin main
   ```

## 4. 今後の使い方 (基本の3ステップ)
コードを修正した後は、以下のコマンドを叩くだけでGitHubに反映できるで。

1. **変更をステージに追加:** `git add .`
2. **変更を記録:** `git commit -m "修正内容のメッセージ"`
3. **GitHubに送信:** `git push origin main`

## 5. Gitの基本コンセプト（例え話で理解！）

Gitの操作で一番よく使う「add」「commit」「push」の違いを、スーパーでの買い物に例えて解説するで。

### 🛒 `git add` (準備：買い物かごに入れる)
*   **イメージ:** スーパーで買うものを**「買い物かご」**に入れる状態。
*   **意味:** 変更したファイルの中から、次の記録に残したいものを**「選ぶ」**作業。
*   **場所:** 「ステージングエリア」と呼ばれる準備場所。

### 🧾 `git commit` (記録：レジで精算する)
*   **イメージ:** レジで精算して**「レシート」**をもらう状態。
*   **意味:** 選んだ変更を、メッセージ（何をしたか）と一緒に自分のPCに**「確定させて保存する」**作業。
*   **場所:** 自分のPCの中（ローカルリポジトリ）に歴史が刻まれる。

### 🌐 `git push` (共有：買ったものをSNSに上げる)
*   **イメージ:** 買ったものをネットにアップして**「みんなに見せる」**状態。
*   **意味:** 自分のPCに記録した歴史を、**「GitHub（ネット上の貯蔵庫）に送信する」**作業。
*   **場所:** GitHub（リモートリポジトリ）に反映され、他の人も見れるようになる。

**「`add` で選んで、`commit` でスタンプ押して、`push` で世界に発信！」** と覚えればOKや！
