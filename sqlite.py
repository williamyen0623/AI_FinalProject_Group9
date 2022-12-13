import sqlite3

food_db_conn = sqlite3.connect('food_db')
print("Datebase open success")
food_db_c = food_db_conn.cursor()
food_db_conn.commit()
food_db_conn.close()