# bunkyo-tennis-checker

## 開発
`env.yaml`通りに環境変数を設定してください

## デプロイ

デプロイには`env.yaml`が必要
```
gcloud config set project bunkyo-tennis-checker
gcloud functions deploy main --runtime python37 --trigger-http --region asia-northeast1 --env-vars-file='env.yaml'
```
