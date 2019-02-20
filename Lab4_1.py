import sqlite3

db = sqlite3.connect('chainsaw_juggle_records.db')

cur = db.cursor()

cur.execute('create table if not exists Record_Holders (holder name, holder country, catches integor')

cur.execute('insert into Record_Holders values (?, ?, ?)', (holder, country, catches))