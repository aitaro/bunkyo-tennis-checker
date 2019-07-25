from linebot import LineBotApi
from linebot.models import TextSendMessage
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))


def line_push_message():
    messages = TextSendMessage(text=f"こんにちは😁\n\n"
                                    f"最近はいかがお過ごしでしょうか?")
    line_bot_api.broadcast(messages=messages)

def hoge():
    print('hoge')

def get_data():
    # セッションを開始
    session = requests.session()

    res = session.get("https://www.yoyaku.city.bunkyo.lg.jp/reselve/m_index.do")
    res.raise_for_status() # エラーならここで例外を発生させる

    print(res.text)
    return {}

def main(*args):
    print(*args)
    line_push_message()


if __name__ == "__main__":
    get_data()
