import requests
import os
from datetime import datetime, timedelta, timezone

SLACK_API_TOKEN = os.environ.get('SLACK_API_TOKEN')

def fetch_threads(channel_id: str, parent_ts: str) -> list:
    # 親スレッドに紐づくすべてのスレッドを取得するために、まずは親スレッドを取得
    response = requests.get(f"https://slack.com/api/conversations.replies?channel={channel_id}&ts={parent_ts}",
                            headers={"Authorization": f"Bearer {SLACK_API_TOKEN}"})
    data = response.json()
    
    if not data["ok"]:
        # 親スレッドが見つからなかった場合は、空リストを返す
        return []
    
    # 親スレッドのメッセージ情報
    parent_thread = data["messages"][0]
    
    # 親スレッドのタイムスタンプ
    parent_ts = parent_thread["ts"]
    
    # 親スレッドの日本時間
    parent_ts_jst = datetime.fromtimestamp(float(parent_ts)).astimezone(timezone(timedelta(hours=9)))
    
    # 親スレッドに紐づくすべてのスレッドを取得するために、ts_from を親スレッドの日本時間から 7 日前に設定する
    ts_from = (parent_ts_jst - timedelta(days=7)).strftime("%s")
    
    # conversations.history API を使用して、親スレッドに紐づくすべてのスレッドを取得
    response = requests.get(f"https://slack.com/api/conversations.history?channel={channel_id}&latest={parent_ts}&oldest={ts_from}",
                            headers={"Authorization": f"Bearer {SLACK_API_TOKEN}"})
    data = response.json()
    
    if not data["ok"]:
        # 取得に失敗した場合は、空リストを返す
        return []
    
    # スレッドのリストを返す
    return data["messages"]
