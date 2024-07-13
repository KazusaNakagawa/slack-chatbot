import certifi
import os
import ssl
from datetime import datetime, timezone, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# FIXME: 開発環境のみ使用: 脆弱性あり
os.environ["SSL_CERT_FILE"] = certifi.where()
ssl._create_default_https_context = ssl._create_unverified_context

# 環境変数からSlack APIトークンを取得
SLACK_API_TOKEN = os.environ["THREADS_SLACK_API_TOKEN"]

# Slack APIクライアントを初期化
client = WebClient(token=SLACK_API_TOKEN)

def fetch_threads(channel_id, ts):
    try:
        response = client.conversations_replies(channel=channel_id, ts=ts)
        messages = response['messages']
        return messages
    except SlackApiError as e:
        print(f"Error fetching threads: {e}")
        return None

# チャンネルIDと親メッセージのタイムスタンプを指定
channel_id = os.environ["CANNEL_ID_RANDOM"]


# 日本時間をUTCに変換
jst = timezone(timedelta(hours=+9), 'JST')
# dt_jst = datetime(2023, 4, 23, 20, 18, 33, tzinfo=jst)
dt_jst = datetime(2023, 4, 22, 11, 45, 2, tzinfo=jst)
dt_utc = dt_jst.astimezone(timezone.utc)

# タイムスタンプに変換し、小数点以下6桁まで表示
parent_ts = dt_utc.timestamp()
formatted_ts = f"{parent_ts:.6f}"

print(formatted_ts)

# スレッドを取得
threads = fetch_threads(channel_id, parent_ts)

# 取得したスレッドを表示
if threads:
    for message in threads:
        print(f"{message['user']} : {message['text']}")
else:
    print("No threads found.")