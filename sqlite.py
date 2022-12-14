import sqlite3

#connect database
try:
    food_db_conn = sqlite3.connect('food_db')
except:
    print("DB connect fail")
else:
    print("DB connect success")

food_db_cur = food_db_conn.cursor()

#create table and set attributes
"""
try:
    food_db_cur.execute(
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
"""

#ALTER FOODLIST
"""
try:
    food_db_cur.execute(
        '''
        ALTER TABLE FOODLIST ADD COLUMN
        TIME TEXT NOT NULL;
        '''
    )
except:
    print("ALTER FOODLIST fail")
else:
    print("ALTER FOODLIST success")
"""


#INSERT FOODLIST
"""
try:
    food_db_cur.execute(
        '''
        INSERT INTO FOODLIST (ID,TIME)
        VALUES ('001','breakfirst')
        '''
        )
except:
    print("INSERT FOODLIST fail")
else:
    print("INSERT FOODLIST success")
"""

#commit database
try:
    food_db_conn.commit()
except:
    print("DB commit fail")
else:
    print("DB commit success")

#print table
cursor = food_db_cur.execute('''SELECT ID, TIME FROM FOODLIST;''')
for row in cursor:
    print("ID = ", row[0])
    print("TIME = ", row[1], "\n")

#close database
try:
    food_db_conn.close()
except:
    print("DB close fail")
else:
    print("DB close success")
    



