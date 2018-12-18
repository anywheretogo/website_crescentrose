import peewee
from wenku8 import read_index, log_in

setting = {
    "host":"guoliangsz.mysql.pythonanywhere-services.com",
#    "port":3306,
    "user":"guoliangsz",
    "password":"lukawish12",

}

db = peewee.MySQLDatabase("guoliangsz$web", **setting)

class A(peewee.Model):
    name = peewee.CharField()
    author = peewee.CharField()
    publisher = peewee.CharField()
    finished =  peewee.BooleanField()
    last_update = peewee.DateField()
    num = peewee.IntegerField(unique=True)
    introduction = peewee.TextField()
    class Meta:
        table_name = 'webku_article'
        database = db


def main_proecss():
    db.connect()
    s = log_in()
    for i in range(1, 123):
        data = read_index(s, i)
        A.insert_many(data).execute()
        print(i, "page ok")
    db.close()

if __name__ == "__main__":
    while True:
        main_proecss()


