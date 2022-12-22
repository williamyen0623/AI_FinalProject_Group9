from flask import Flask, request, abort, render_template, url_for
from linebot import (LineBotApi, WebhookHandler)
from line_chatbot_api import *
from linebot.exceptions import (InvalidSignatureError)
from azure_speech_service import *
from operation import *
from sql_operation import *
from urllib.parse import parse_qsl, parse_qs
import json
import re
import sqlite3

app = Flask(__name__)

# line bot route
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

#web route
@app.route('/')
def index():
    return render_template('index.html')

# handle msg
@handler.add(MessageEvent)
def handle_something(event):
    if event.message.type=='audio':
        handle_audio_message(event)
    if event.message.type == 'text':
        recrive_text = event.message.text
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = recrive_text))

    
user_choices = {'feature': '', 'meal': '', 'day': '', 'rating': ''}
query_message = {   'feature': '請問是要查詢哪種料理風格的餐廳呢？\n中式、日式、韓式、泰式、美式、歐式',
                                    'meal': '請問是要查詢早餐、午餐還是晚餐的餐廳呢？',
                                    'day': '請問是要查詢星期一到日哪天的餐廳呢？',
                                    'rating': '請問希望餐廳最少要有幾顆星呢？\n不設限、4顆星、4.3顆星、4.5顆星、4.7顆星、5顆星'
                                    }
def handle_audio_message(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    filename_wav = 'temp_audio.wav'
    message_to_wav(message_content, filename_wav)
    text = transcribe_from_file(filename_wav)
    print('Transcribe:', text)

    if(get_user_choices_whether(text)): # 尋找餐廳 in text
        initial_user_choices(user_choices)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '料理風格、早午晚餐、星期幾、評論星星'))
        return
    else:
        insert_user_choices(text, user_choices)
        choice = check_user_choice_empty(user_choices)
        if(choice == ''): # no null information
            pass
        else: # null information exist
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = query_message[choice]))
            return
     
        
    
    # transform choices
    transform_choice(user_choices)
    # call service
    user_response_resturant = get_reply_from_audio(user_choices)

    line_bot_api.reply_message(event.reply_token, user_response_resturant)
    # initial for next time use
    for choice in choices_str:
        user_choices[choice] = ''
            

            


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566)