""" Slack, OPENAI API を使って指定した Slack チャンネルに返答する Bot """
import certifi
import os
import ssl
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from models.oepnai import OpenAI

# FIXME: 開発環境のみ使用: 脆弱性あり
os.environ["SSL_CERT_FILE"] = certifi.where()
ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()

# API トークンを設定する
SLACK_APP_TOKEN = os.getenv('SLACK_APP_TOKEN')
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

if not SLACK_APP_TOKEN and not SLACK_BOT_TOKEN:
    raise

app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def handle_mentions(body, say, logger):
    logger.level = 20 # INFO
    logger.info({'body': body})

    try:
        # はじめの半角スペースをきりとって、テキストのみ抽出
        prompt = body['event']['text'].split(' ', 1)[1]
        # スレッドの time-stamp を取得
        thread_ts = body["event"]["ts"]
        logger.info({'prompt': prompt})
    except IndexError as ex:
        logger.error({
            'msg': '入力規則がまちがっています. @メンションの後に 半角スペースが必要です.',
            'ex': ex,
        })

    text = OpenAI().response_text(prompt)
    # スレッドに返信
    say(text, thread_ts=thread_ts)
    logger.info({
        'text': text,
        'thread_ts': thread_ts,
        'status': 200,
    })

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
