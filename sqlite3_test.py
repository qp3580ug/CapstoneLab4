import sqlite3

db = sqlite3.connect('my_first_db.db')
db.row_factory = sqlite3.Row
cur = db.cursor()

cur.execute('create table phones (brand test, version integor)')

cur.execute('insert into phones values ("Android", 5)')
cur.execute('insert into phones values ("iPhone", 6)')

for row in cur.execute('select * from phones'):
    print(row['brand'])
    print(row['version'])

cur.execute('drop table phones')

db.commit()

db.close()