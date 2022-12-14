from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import re

app = Flask(__name__)

line_bot_api = LineBotApi('XQvhTloIxWae1Sr0aCtrJ2lvcCA+dWfxyL866iE9BTeD2EcqlD2O3IFDK93bnHL1TvdJyCJNEl4HEV3eZTIVXEp2UXeZQiXLXmNOiZ0+MxH7FEUwvn2HE5bmZqnXNe+bxq3GziqRPCpijZu6NJ1B3QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('357b96f6d7614f9103b63b09b0483d1b')

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
		message = text=event.message.text
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text = message))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566)