from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from line_chatbot_api import *
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)
import re

app = Flask(__name__)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text = event.message.text
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=message))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566)