from line_chatbot_api import *
feature = ['中式', '日式', '韓式', '泰式', '美式', '歐式']
meal = ['早餐', '午餐', '晚餐']
day = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
rating = ['不設限', '5顆星', '4顆星', '3顆星']
choices_list = [feature, meal, day, rating]
choices_str = ['feature', 'meal', 'day', 'rating']
#user_choices = {'feature': '', 'meal': '', 'day': '', 'rating': ''}

def insert_user_choices(text, _user_choices):
    
    for choice in choices_list:
        for c in choice:
            if c in text:
                _user_choices[choices_str[choices_list.index(choice)]] = c 
                break
    print('inserted_choices: ', _user_choices)
    return _user_choices

def check_user_choice_empty(_user_choices):
    empty_choice = ''
    for choice in choices_str:
        if _user_choices[choice] == '':
            empty_choice += choice
            return choice
    return empty_choice
    

def get_user_choices_whether(text):
    if '尋找餐廳' in text:
        return True
    else:
        return False
    
def initial_user_choices(_user_choices):
        for choice in choices_str:
            _user_choices[choice] = ''
        return _user_choices

def transform_choice(user_choices):
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
        
    if('5' in user_choices['rating']):
        user_choices['rating'] = '5'
    elif('4' in user_choices['rating']):
        user_choices['rating'] = '4'
    elif('3' in user_choices['rating']):
        user_choices['rating'] = '3'
    elif('不設限' in user_choices['rating']):
        user_choices['rating'] = '0'
    
    if('五' in user_choices['rating']):
        user_choices['rating'] = '5'
    elif('四' in user_choices['rating']):
        user_choices['rating'] = '4'
    elif('三' in user_choices['rating']):
        user_choices['rating'] = '3'
    elif('不設限' in user_choices['rating']):
        user_choices['rating'] = '0'
    
    if('泰' in user_choices['feature']):
        user_choices['feature']='泰式'
    print('trans_choices: ', user_choices)  
    return user_choices