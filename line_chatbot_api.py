# line_chatbot_api.py
import requests, json, os
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (
    MessageEvent, PostbackEvent, TextMessage, TextSendMessage,
    ImageSendMessage, StickerSendMessage, LocationSendMessage,
    TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction,
    URIAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate,
    ImageCarouselColumn, DatetimePickerAction, ConfirmTemplate, FlexSendMessage, 
    ImagemapSendMessage, MessageImagemapAction, BaseSize, ImagemapArea)

# Messaging API settings -> Channel access token -> Channel access token (long-lived)
line_bot_api = LineBotApi(
    'XQvhTloIxWae1Sr0aCtrJ2lvcCA+dWfxyL866iE9BTeD2EcqlD2O3IFDK93bnHL1TvdJyCJNEl4HEV3eZTIVXEp2UXeZQiXLXmNOiZ0+MxH7FEUwvn2HE5bmZqnXNe+bxq3GziqRPCpijZu6NJ1B3QdB04t89/1O/w1cDnyilFU='
)
# Basic settings -> Channel secret
handler = WebhookHandler('357b96f6d7614f9103b63b09b0483d1b')

rich_menu_id = "richmenu-e0f049c1d8938d4a087ce66d0b4f958e"

headers = {"Authorization":f"Bearer XQvhTloIxWae1Sr0aCtrJ2lvcCA+dWfxyL866iE9BTeD2EcqlD2O3IFDK93bnHL1TvdJyCJNEl4HEV3eZTIVXEp2UXeZQiXLXmNOiZ0+MxH7FEUwvn2HE5bmZqnXNe+bxq3GziqRPCpijZu6NJ1B3QdB04t89/1O/w1cDnyilFU=" , "Content-Type":"application/json"}

"""json_path = os.path.join(os.path.split(__file__)[0], 'rich_menu.txt')
with open(json_path, 'r', encoding='UTF-8') as f:
		flexmessagestring = f.read()
flexmessagedict = json.loads(flexmessagestring)
req = requests.request('POST',
                       'https://api.line.me/v2/bot/richmenu',
                       headers=headers,
                       data=json.dumps(flexmessagedict).encode('utf-8'))


print(req.text)"""

"""with open("./richmenu.png", 'rb') as f:
    line_bot_api.set_rich_menu_image(rich_menu_id, "image/png", f)"""
    
# ===================================================="""

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+rich_menu_id,
                       headers=headers)
print(req.text)

rich_menu_list = line_bot_api.get_rich_menu_list()

