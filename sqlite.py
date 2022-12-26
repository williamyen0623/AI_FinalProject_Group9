import sqlite3
from turntodict import *
#connect database
try:
    food_db_conn = sqlite3.connect('food_db')
except:
    print("DB connect fail")
else:
    print("DB connect success")

food_db_cur = food_db_conn.cursor()

food_list = get_all_food()
#INSERT FOODLIST
for i in range(0, len(food_list)):
    food_db_cur.execute(
        '''INSERT INTO FOODLIST (NAME,FEATURE,OPENTIME,OPENDAY,ADDRESS,PHONENUM,RATING,RATINGTOTAL,LAT,LNG, NUM) VALUES ("{}","{}","{}","{}","{}","{}",{},{},{},{},{})'''
        .format(food_list[i]["NAME"], food_list[i]["FEATURE"],
                food_list[i]["OPENTIME"], food_list[i]["OPENDAY"],
                food_list[i]["ADDRESS"], food_list[i]["PHONENUM"],
                food_list[i]["RATING"], food_list[i]["RATINGTOTAL"],
                food_list[i]["LAT"], food_list[i]["LNG"], i))

#commit database
try:
    food_db_conn.commit()
except:
    print("DB commit fail")
else:
    print("DB commit success")

#close database
try:
    food_db_conn.close()
except:
    print("DB close fail")
else:
    print("DB close success")
