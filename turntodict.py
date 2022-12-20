import pandas as pd
import os
allfood = []
keyja = ["日式餐廳", "日式料理", "日式鍋物", "日式海鮮", "日式拉麵", "日式咖哩", "日式拉麵"]
keych = ["中式餐廳", "中式料理", "中國菜", "中式鍋物", "古早味料理", "羊肉爐薑母鴨", "中式小吃"]
keyth = ["泰式餐廳", "泰式料理", "泰式鍋物"]
keyam = ["美式餐廳", "美式漢堡", "美式料理"]
keyko = ["韓式餐廳", "韓式料理", "韓式燒肉", "韓式小吃", "韓式鍋物"]
keyeu = ["歐式餐廳", "義式餐廳", "義式料理","披薩", "義大利麵"]
keywords={"日式": keyja, "中式":keych, "泰式":keyth, "美式": keyam, "韓式": keyko, "歐式":keyeu}
areas = keywords.keys()


tag = ['風格', '開店時間', '地址', '名字', 'id', '電話', '經度', '緯度', '評論數', '評價', '開店日']
exceltag = ['style', 'opentime', 'vicinity', 'name',
    'place_id', 'formatted_phone_number', 'lat', 'lng', 'user_ratings_total', 'rating', 'openday']
for area in areas:
    output = pd.read_excel(area+'.xlsx')
    seqs = list(output.index)
    #c = [{ x : output.at[seq, y] for x in tag for y in exceltag} for seq in seqs]
    #allfood += c  

    for seq in seqs:
        dict = {}
        dict['風格'] = output.at[seq, 'style']
        dict['開店時間'] = output.at[seq, 'opentime']
        dict['地址'] = output.at[seq, 'vicinity']
        dict['名字'] = output.at[seq, 'name']
        dict['id'] = output.at[seq, 'place_id']
        dict['電話'] = output.at[seq, 'formatted_phone_number']
        dict['經度'] = output.at[seq, 'lat']
        dict['緯度'] = output.at[seq, 'lng']
        dict['評論數'] = output.at[seq, 'user_ratings_total']
        dict['評價'] = output.at[seq, 'rating']
        dict['開店日'] = output.at[seq, 'openday']
        allfood.append(dict)
print(allfood)