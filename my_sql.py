import peewee
from wenku8 import read_index, log_in

setting = {
    "host":"127.0.0.1",
#    "port":3306,
    "user":"root",
    "password":"lukawish12",

}

db = peewee.MySQLDatabase("websites", **setting)

class A(peewee.Model):
    name = peewee.CharField()
    author = peewee.CharField()
    publisher = peewee.CharField()
    finished =  peewee.BooleanField()
    last_update = peewee.DateField()
    num = peewee.IntegerField(unique=True)
    introduction = peewee.TextField()
    class Meta:
        table_name = 'wenku_article'
        database = db


def main_proecss():
    s = log_in()
    db.connect()    
    exist_data = [i.num for i in A.select()]
    for i in range(1, 10):
        data = read_index(s, i)
        to_add = [ i for i in data if i["num"] not in exist_data]
        if to_add:
            A.insert_many(to_add).execute()
        print(i, "page ok")
    db.close()

if __name__ == "__main__":      
    main_proecss()
    pass

