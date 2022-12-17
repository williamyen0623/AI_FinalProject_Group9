import sqlite3

#connect database
try:
    food_db_conn = sqlite3.connect('food_db')
except:
    print("DB connect fail")
else:
    print("DB connect success")

food_db_cur = food_db_conn.cursor()

#INSERT FOODLIST
for i in range(0,10):
    try:
        food_db_cur.execute(
            '''
            INSERT INTO FOODLIST (ID,TIME,NAME,FEATURE)
            VALUES ('{}','breakfirst','{}','{}')
            '''.format(str(i),str(i),str(i))
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
    



