## ChatGPT Bot

### 前提

* `.env.exsample` を `.env` にし TOKEN・API 情報を入れる
* local のみ起動確認済
* Mac M1
* Python 3.12.7

### 手順

1. 実行コマンド

    ```bash
    # 環境作成
    $ python -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt

    # bot 起動
    $ python slack_chatbot.py
    ...

    ⚡️ Bolt app is running!
    ```

2. Slack で 登録したBotにメンションして投稿する。

3. Botからの回答を確認。

#### 動作イメージ:

![slack bot](docs/images/gpt_slack.gif)

### Ref

* [Slack: Bolt 入門ガイド](https://slack.dev/bolt-python/ja-jp/tutorial/getting-started)
* [API GPT Models](https://platform.openai.com/docs/models)
