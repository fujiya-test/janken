# 共同開発の手順 (How to Contribute)

このプロジェクトを他の人が落としてきて、一緒に開発する時の基本的な流れやで。

## 1. リポジトリを自分のPCに持ってくる (Clone)
まずは、GitHub上にあるコードを自分のPCにコピー（クローン）するんや。

```powershell
git clone https://github.com/fujiya-test/janken.git
cd janken
```

## 2. 最新の状態にする (Pull)
作業を始める前に、他の人が更新した内容がないか確認して、最新の状態を取り込んでおくんや。

```powershell
git pull origin main
```

## 3. 作業用の「枝」を作る (Branch)
`main` ブランチ（本番用）を直接いじると危ないから、自分専用の作業場所（ブランチ）を作るのがマナーや。

```powershell
# "feature-new-rule" という名前のブランチを作って、そこに切り替える
git checkout -b feature-new-rule
```

## 4. コードを書いて記録する (Add & Commit)
いつもの「買い物かごに入れて、レシートをもらう」流れや。

```powershell
git add .
git commit -m "新しいルールを追加したで"
```

## 5. 自分の作業をGitHubに送る (Push)
自分の作ったブランチをGitHubにアップロードするんや。

```powershell
git push origin feature-new-rule
```

## 6. プルリクエストを送る (Pull Request)
GitHubの画面に行くと「Compare & pull request」というボタンが出てるから、それを押して変更内容を説明して、管理者に「取り込んでや！」とお願い（プルリク）を送るんや。

## 7. 終わったら main に戻る
作業が終わって、プルリクが承認（マージ）されたら、また `main` に戻って次の作業に備えるんや。

```powershell
git checkout main
git pull origin main
```

**「本番(main)は汚さず、枝(branch)で作業して、お願い(Pull Request)を送る」**。これがチーム開発の鉄則や！
