import os 
import sqlite3 

file_name = "data_base.db"

def try_create():
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()

    result = cursor.execute('''CREATE TABLE IF NOT EXISTS Players (
        name TEXT  PRIMARY KEY,
        scores INTEGER)
        ''')
   
    connection.commit()
    connection.close()

def get_records():
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()
    result = cursor.execute('SELECT name, scores FROM Players ORDER BY scores DESC') 
    return result.fetchall()
    
def set_record(name, scores):
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()


    result = cursor.execute('SELECT name, scores FROM Players').fetchall()

    # вынести в отдельный метод 
    player_exist = False
    player_score = -1
    for row in result:
        print(row[0], row[0] == name)
        if row[0] == name:
            player_exist = True
            player_score = int(row[1])

    if player_exist == True:
        if player_score >= scores:
            print ("Рекорд меньше, обновление записи не требуется")
        else:    
            print("Есть")
            cursor.execute('''UPDATE Players SET scores = ? WHERE name = ?''', (scores, name))
    else:
        cursor.execute('''INSERT INTO Players(name, scores) VALUES(?, ?)''', (name, scores))
        print("Нет")
    
    
    connection.commit()
    connection.close()


