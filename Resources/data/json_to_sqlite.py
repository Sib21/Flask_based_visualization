import json
import sqlite3

connection = sqlite3.connect('testDB.sqlite')
cursor = connection.cursor()
cursor.execute('Create Table if not exists Energy (end_year Text,intensity Integer,sector Text,topic Text,insight Text,url Text,region Text,start_year Text,impact Text,added Text,published  Text, country Text, relevance Integer, pestle Text, source Text, title Text, likelihood Integer)')

traffic = json.load(open('jsondata.json',encoding="utf8") )
columns = ['end_year','intensity','sector','topic','insight','url', 'region','start_year','impact','added','published','country', 'relevance','pestle','source','title','likelihood']
for row in traffic:
    keys= tuple(row[c] for c in columns)
    cursor.execute('insert into Energy values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',keys)
    print(f'{row["end_year"]} data inserted Succefully')

connection.commit()
connection.close()