from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from line_chatbot_api import *
from linebot.exceptions import (InvalidSignatureError)
from azure_speech_service import *
import json
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

# handle msg
@handler.add(MessageEvent)
def handle_something(event):
    if event.message.type == 'audio':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '收到聲音了'))
        handle_audio_message(event)
    if event.message.type == 'text':
        recrive_text = event.message.text
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = recrive_text))


style = ['中式', '日式', '韓式', '泰式', '美式', '歐式']
meal = ['早餐', '午餐', '晚餐']
day = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
review_number = ['不限定', '0到200', '201到500', '501到1000', '1000以上']
review_star = ['不設限', '4', '4.3', '4.5', '4.7', '5']
choices_list = [style, meal, day, review_number, review_star]
choices_str = ['style', 'meal', 'day', 'review_number', 'review_star']
user_choices = {'style': '', 'meal': '', 'day': '', 'review_number': '', 'review_star': ''}
query_message = {   'style': '請問是要查詢哪種料理風格的餐廳呢？\n中式、日式、韓式、泰式、美式、歐式',
                                    'meal': '請問是要查詢早餐、午餐還是晚餐的餐廳呢？',
                                    'day': '請問是要查詢星期一到日哪天的餐廳呢？',
                                    'review_number': '請問是要查詢幾個評論以上的餐廳呢？\n不限定、0到200、201到500、501到1000、1000以上',
                                    'review_star': '請問是要查詢幾顆星以上的餐廳呢？\n不設限、4、4.3、4.5、4.7、5'
                                    }
    
def handle_audio_message(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    filename_wav = 'temp_audio.wav'
    message_to_wav(message_content, filename_wav)
    text = transcribe_from_file(filename_wav)
    print('Transcribe:', text)
    if '找餐廳' in text:
        user_choices = {'style': '', 'meal': '', 'day': '', 'review_number': '', 'review_star': ''}
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '料理風格、早午晚餐、星期幾、評論數、評論星星'))
    for choice in choices_list:
        for c in choice:
            if c in text:
                user_choices[choices_str[choices_list.index(choice)]] = c 
                break
    for choice in choices_str:
        if user_choices[choice] == '':
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = query_message[choice]))
            return
    print('user_choices:', user_choices)
    # call service
    user_choices = {'style': '', 'meal': '', 'day': '', 'review_number': '', 'review_star': ''}
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
		message = text=event.message.text
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text = message))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566)