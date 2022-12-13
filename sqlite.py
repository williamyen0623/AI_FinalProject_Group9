import sqlite3

#connect database
try:
    food_db_conn = sqlite3.connect('food_db')
except:
    print("DB connect fail")
else:
    print("DB connect success")

#create table and set attributes

food_db_c = food_db_conn.cursor()
try:
    food_db_c.execute(
    '''
    CREATE TABLE FOODLIST
    (
        ID TEXT PRIMARY KEY NOT NULL
    );
    '''
)
except:
    print("DB TABLE create fail")
else:
    print("DB TABLE create success")

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
