# line_chatbot_api.py

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, 
    PostbackEvent,
    TextMessage, 
    TextSendMessage, 
    ImageSendMessage, 
    StickerSendMessage, 
    LocationSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    PostbackAction,
    MessageAction,
    URIAction,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    DatetimePickerAction,
    ConfirmTemplate
)

# Messaging API settings -> Channel access token -> Channel access token (long-lived)
line_bot_api = LineBotApi(
    'XQvhTloIxWae1Sr0aCtrJ2lvcCA+dWfxyL866iE9BTeD2EcqlD2O3IFDK93bnHL1TvdJyCJNEl4HEV3eZTIVXEp2UXeZQiXLXmNOiZ0+MxH7FEUwvn2HE5bmZqnXNe+bxq3GziqRPCpijZu6NJ1B3QdB04t89/1O/w1cDnyilFU='
)
# Basic settings -> Channel secret
handler = WebhookHandler('357b96f6d7614f9103b63b09b0483d1b')
