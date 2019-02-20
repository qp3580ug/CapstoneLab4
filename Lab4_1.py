import sqlite3

db = sqlite3.connect('chainsaw_juggle_records.db')

cur = db.cursor()

cur.execute('create table if not exists Record_Holders (holder, country, catches)')

holder = input('Enter Record Holder\'s Full Name: ')
country = input('Enter Record Holder\'s Country: ')
catches = int(input('Enter their total number of catches: '))

cur.execute('insert into Record_Holders values (?, ?, ?)', (holder, country, catches))

search_param = input('Enter Record Holder\'s Full Name you Would Like to Search: ')

for row in cur.execute('SELECT rowid, * FROM Record_Holders WHERE holder = ?', (search_param, id)):
    print(row['holder'])
    print(row['country'])
    print(row['catches'])

