import sqlite3

#connect database
try:
    food_db_conn = sqlite3.connect('food_db')
except:
    print("DB connect fail")
else:
    print("DB connect success")

food_db_cur = food_db_conn.cursor()

food_list=[{'ID':'1','TIME':'br','NAME':'維克美','FEATURE':'美式'}]
#INSERT FOODLIST
try:
    for i in range(0,len(food_list)):
        food_db_cur.execute(
            '''
            INSERT INTO FOODLIST (ID,TIME,NAME,FEATURE)
            VALUES ('{}','{}','{}','{}')
            '''.format(food_list[i]["ID"],food_list[i]["TIME"],food_list[i]["NAME"],food_list[i]["FEATURE"])
        )
except:
    print("INSERT FOODLIST fail")
else:
    print("INSERT FOODLIST success")

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
    



