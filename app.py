from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from line_chatbot_api import *
from linebot.exceptions import (InvalidSignatureError)
from azure_speech_service import *
import json
import re
import sqlite3

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
    if event.message.type=='audio':
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '收到聲音了..'))
        handle_audio_message(event)
    if event.message.type == 'text':
        recrive_text = event.message.text
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = recrive_text))

feature = ['中式', '日式', '韓式', '泰式', '美式', '歐式']
meal = ['早餐', '午餐', '晚餐']
day = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
#review_number = ['不限定', '0到200', '201到500', '501到1000', '1000以上']
rating = ['不設限', '4.5顆星', '4.3顆星', '4.7顆星', '5顆星', '4顆星']
choices_list = [feature, meal, day, rating]
choices_str = ['feature', 'meal', 'day', 'rating']
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
    
    if '找餐廳' in text:
        for choice in choices_str:
            user_choices[choice] = ''
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '料理風格、早午晚餐、星期幾、評論星星'))
        return
    
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
    # transform choices
    if('早' in user_choices['meal']):
        user_choices['meal'] = 'B'
    elif('午' in user_choices['meal']):
        user_choices['meal'] = 'L'
    elif('晚' in user_choices['meal']):
        user_choices['meal'] = 'D'
        
    if('一' in user_choices['day']):
        user_choices['day'] = '1'
    elif('二' in user_choices['day']):
        user_choices['day'] = '2'
    elif('三' in user_choices['day']):
        user_choices['day'] = '3'
    elif('四' in user_choices['day']):
        user_choices['day'] = '4'
    elif('五' in user_choices['day']):
        user_choices['day'] = '5'
    elif('六' in user_choices['day']):
        user_choices['day'] = '6'
    elif('日' in user_choices['day']):
        user_choices['day'] = '7'
        
    if('4.7' in user_choices['rating']):
        user_choices['rating'] = '4.7'
    elif('4.5' in user_choices['rating']):
        user_choices['rating'] = '4.5'
    elif('4.3' in user_choices['rating']):
        user_choices['rating'] = '4.3'
    elif('5' in user_choices['rating']):
        user_choices['rating'] = '5'
    elif('4' in user_choices['rating']):
        user_choices['rating'] = '4'     
    
    print('user_choices2:', user_choices)
    # call service
    food_db_conn = sqlite3.connect('food_db')
    food_db_cur = food_db_conn.cursor()
    cursor = food_db_cur.execute(
        '''
        SELECT NAME,FEATURE,OPENTIME,OPENDAY,ADDRESS,PHONENUM,RATING,RATINGTOTAL,LAT,LNG FROM FOODLIST
        WHERE FEATURE = '{}' AND RATING >= {} AND OPENTIME LIKE '%{}%' AND OPENDAY LIKE '%{}%';
        '''.format(user_choices['feature'], user_choices['rating'], user_choices['meal'], user_choices['day'])
    )
    count = 0
    user_response_resturant = []
    for row in cursor:
        reply_messsage = ''
        print("NAME = ", row[0])
        print("FEATURE = ", row[1])
        print("OPENTIME = ", row[2])
        print("OPENDAY = ", row[3])
        print("ADDRESS = ", row[4])
        print("PHONENUM = ", row[5])
        print("RATING = ", row[6])
        print("RATINGTOTAL = ", row[7])
        print("LAT = ", row[8])
        print("LNG = ", row[9], "\n")
        count += 1
        reply_messsage += '店名:{}\n地址:{}\n電話:{}\n評價:{}\n評論數:{}'.format(row[0], row[4], row[5], row[6], row[7])
        user_response_resturant.append(TextSendMessage(text=reply_messsage))
        user_response_resturant.append(LocationSendMessage(title=row[0],address=row[4],latitude=row[8],longitude=row[9]))
        if(count == 2): break
    food_db_conn.commit()
    food_db_conn.close()
    line_bot_api.reply_message(event.reply_token, user_response_resturant)
    # initial for next time use
    for choice in choices_str:
        user_choices[choice] = ''

            


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566)