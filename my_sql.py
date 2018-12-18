import peewee
import datetime, time
from wenku8 import read_index, log_in

setting = {
    "host":"localhost",
    "port":3306,
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
        table_name = 'Articles'
        database = db




def migrate():
    a_list = A.select()
    s = []
    for i in a_list:
        #print(i.index, i.name, type(i))
        a = {}
        a["name"] = i.name
        a["num"] = i.num
        a["author"] = i.author
        a["publisher"] = i.publisher
        a["finished"] = i.finished
        a["last_update"] = i.last_update
        a["introduction"] = i.introduction
        #print(a,type(a), s, type(s))
        s.append(a)

    query = B.insert_many(s).execute()
    print(query)




def main_proecss():
    db.connect()
    s = log_in()
    for i in range(1, 123):
        data = read_index(s, i)
        query = Article.insert_many(data).execute()
        print(i, "page ok")
    db.close()

if __name__ == "__main__":
    while True:
        main_proecss()


