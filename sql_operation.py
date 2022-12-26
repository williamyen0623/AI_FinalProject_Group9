import sqlite3
import random
from line_chatbot_api import *

current={"count":0, "now":0}
def get_reply_from_audio(user_choices):
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
        current['count'] += 1
        reply_messsage += '店名:{}\n地址:{}\n電話:{}\n評價:{}\n評論數:{}'.format(row[0], row[4], row[5], row[6], row[7])
        user_response_resturant.append(TextSendMessage(text=reply_messsage))
        user_response_resturant.append(LocationSendMessage(title=row[0],address=row[4],latitude=row[8],longitude=row[9]))
        if(count == 2): break
    if(count == 0):
        user_response_resturant.append(TextSendMessage(text="很抱歉，沒有符合您需求的餐廳"))
    else:
        user_response_resturant.append(TemplateSendMessage(
            alt_text='給programmer看的, 不會顯示',
            template=ConfirmTemplate(
                text='請問要查詢更多餐廳嗎?',
                actions=[
                    MessageAction(
                        label='結束查詢',
                        text='結束查詢'
                    ),
                    MessageAction(
                        label='顯示更多',
                        text='顯示更多'
                    )
                ]
            )))
    food_db_conn.commit()
    food_db_conn.close()
    return user_response_resturant

def get_more_rest(user_choices):
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
    current['now'] = 0
    for row in cursor:
        current['now'] += 1
        if(current['count'] >= current['now']):
            continue
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
        current['count'] += 1
        reply_messsage += '店名:{}\n地址:{}\n電話:{}\n評價:{}\n評論數:{}'.format(row[0], row[4], row[5], row[6], row[7])
        user_response_resturant.append(TextSendMessage(text=reply_messsage))
        user_response_resturant.append(LocationSendMessage(title=row[0],address=row[4],latitude=row[8],longitude=row[9]))
        if(count == 2): break
    if(count == 0):
        user_response_resturant.append(TextSendMessage(text="很抱歉，沒有更多符合您需求的餐廳"))
    else:
        user_response_resturant.append(TemplateSendMessage(
            alt_text='給programmer看的, 不會顯示',
            template=ConfirmTemplate(
                text='請問要查詢更多餐廳嗎?',
                actions=[
                    MessageAction(
                        label='結束查詢',
                        text='結束查詢'
                    ),
                    MessageAction(
                        label='顯示更多',
                        text='顯示更多'
                    )
                ]
            )))
    food_db_conn.commit()
    food_db_conn.close()
    return user_response_resturant
    

def set_current_count(_int_set):
    current['count'] = _int_set
    
def get_random_rest():
    random_num = random.randint(0,671)
    print(random_num)
    food_db_conn = sqlite3.connect('food_db')
    food_db_cur = food_db_conn.cursor()
    cursor = food_db_cur.execute(
        '''
        SELECT NAME,FEATURE,OPENTIME,OPENDAY,ADDRESS,PHONENUM,RATING,RATINGTOTAL,LAT,LNG FROM FOODLIST
        WHERE NUM = {};
        '''.format(random_num)
    )
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
        reply_messsage += '店名:{}\n地址:{}\n電話:{}\n評價:{}\n評論數:{}'.format(row[0], row[4], row[5], row[6], row[7])
        user_response_resturant.append(TextSendMessage(text=reply_messsage))
        user_response_resturant.append(LocationSendMessage(title=row[0],address=row[4],latitude=row[8],longitude=row[9]))
    food_db_conn.commit()
    food_db_conn.close()
    return user_response_resturant
