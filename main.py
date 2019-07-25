from linebot import LineBotApi
from linebot.models import TextSendMessage
import os

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))


def line_push_message():
    messages = TextSendMessage(text=f"こんにちは😁\n\n"
                                    f"最近はいかがお過ごしでしょうか?")
    line_bot_api.broadcast(messages=messages)

def hoge():
    print('hoge')

def main(*args):
    print(*args)
    line_push_message()


if __name__ == "__main__":
    line_push_message()
