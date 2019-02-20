import sqlite3

db = sqlite3.connect('chainsaw_juggle_records.db')

cur = db.cursor()

cur.execute('create table if not exists Record_Holders (holder name, holder country, catches integor')

holder = input('Enter Record Holder\'s Full Name: ')
country = input('Enter Record Holder\'s Country: ')
catches = int(input('Enter their total number of catches: '))

cur.execute('insert into Record_Holders values (?, ?, ?)', (holder, country, catches))

