<center>
  <h3>C3_team3</h3>
  <h1>Hackathon_LINE_Bot</h1>
</center>

## 運用
- 開発する際には[`ngrok`](https://ngrok.com/download)を利用することを推奨．  
  毎回Herokuにデプロイして確認するなんてめんどくさすぎるので．ローカルでサーバー立てつつngrokでポート開いてWebhookに設定しておきましょう．  
  ちなみに**ngrokは一回止めるとURL変わっちゃう**のでWebhookの設定を起動するたびにやらなけりゃいけません．まあずっと起動しとけばいいと思う．  

- `release-heroku`ブランチの内容がherokuに自動デプロイされるようにしてます．まあ私が適当に確認してマージしますので気にしないでー．皆さんは普通に`master`ブランチにPushしてもらってOKです．
