"""
Slack BotにGPT APIを組み込むには、まずOpenAI APIキーを取得する必要があります。
OpenAI APIは、有料のWeb APIであり、APIキーを取得するにはOpenAIのWebサイトでアカウント登録を行う必要があります。

次に、Slack Botを開発するためのWebフレームワークとして、slack-boltライブラリを使用することをお勧めします。
slack-boltライブラリは、SlackのAPIにアクセスするためのPythonライブラリで、Webフレームワークとしての機能も備えています。

以下は、slack-boltライブラリを使用して、Slack BotにGPT APIを組み込むための例です。

下記の例では、openaiライブラリを使用してGPT APIにアクセスしています。
app_mentionイベントが発生すると、入力されたテキストからプロンプトを抽出し、GPT APIを使用して応答を生成しています。

この例では、davinciエンジンを使用しており、応答の最大トークン数は1024、temperatureは0.7に設定されています。
これらの値は、必要に応じて変更することができます。

なお、この例ではSocketModeHandlerを使用してBotを起動していますが、必要に応じてWebサーバーを使用することもできます。
また、GPT APIを使用するために必要なライブラリをインストールする必要があります。詳細については、OpenAIの公式ドキュメントを
参照してください。

"""
import certifi
import os
import openai
import logging
import ssl
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from dotenv import load_dotenv

os.environ["SSL_CERT_FILE"] = certifi.where()

# FIXME: 開発環境のみ使用: 脆弱性あり
ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()

# API トークンを設定する
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SLACK_APP_TOKEN = os.getenv('SLACK_APP_TOKEN')
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

if not SLACK_APP_TOKEN and not SLACK_BOT_TOKEN:
    raise

openai.api_key = OPENAI_API_KEY
app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def handle_mentions(body, say, logger):
# async def command_handler(body, say):

    # prompt = body['event']['text'].split(' ', 1)[1]
    # response = openai.Completion.create(
    #     engine="davinci",
    #     prompt=prompt,
    #     max_tokens=1024,
    #     n=1,
    #     stop=None,
    #     temperature=0.7
    # )
    # text = response.choices[0].text.strip()
    # say(text)
    logging.debug("Received an app_mention event")
    text = body['event']['text']
    # メッセージに「hello」という文字列が含まれている場合、応答する
    if 'hello' in text.lower():
        say('Hello! How can I help you?')


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
