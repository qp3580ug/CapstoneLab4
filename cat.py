from peewee import *

db = SqliteDatabase('cats.sqlite')

class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} is a {self.color} cat and is {self.age} years old.'

db.connect()
db.create_tables([Cat])

print('\nCreate and save 3 cats')

zoe = Cat(name="Zoe", color='Ginger', age=3)
zoe.save()

holly = Cat(name="Holly", color='Tabby', age=5)
holly.save()

mog = Cat(name="Mog", color='Black', age=7)
mog.save()

mog_id = mog.id
mog = Cat.get_by_id(mog_id)
print(f'\nGet by ID {mog_id} returns:', mog)

holly_again = Cat.get_or_none(Cat.name == 'Holly')
print('\nCat Called Holly: ', holly_again)

molly = Cat = Cat.get_or_none(Cat.name == 'Molly')
print('\nCat called Molly: ', molly)

print('\nCats, sorted by name')

for cat in Cat.select().order_by(Cat.name):
    print(cat)