from bs4 import BeautifulSoup
import requests,threading,time
from datetime import date




def download(id_name):
    num_id, name = id_name
    print(num_id,name,'start')
    cookies = load_cookies()
    url = 'http://dl.wenku8.net/down.php'
    payload = {'type':'txt',
                'id':num_id }
    re = requests.get(url, cookies = cookies, params = payload)
    try:
        with open(num_id + name + '.txt', 'wb') as file:
            file.write(re.content)
    except:
        with open(num_id + '.txt', 'wb') as file:
            file.write(re.content)
    print(num_id,name,'download')

def log_in():
    s = requests.Session()
    data = {'username': 'blueliqi',
        'password': 'redback12',
        'usecookie': 0,
        'action': 'login',
        'submit': '''%26%23160%3B%B5%C7%26%23160%3B%26%23160%3B%C2%BC%26%23160%3B'''}

    params = {'do':'submit'}

    url = "https://www.wenku8.net/login.php"

    re = s.post(url, params=params, data=data)
    re.encoding = 'gbk'
    html = BeautifulSoup(re.text,'lxml')
    assert "登录成功" in  html.title
    print(html.title)
    return s

def read_index(s, p):
    url = 'http://www.wenku8.net/modules/article/articlelist.php'
    payload = {'page':p}
    re = s.get(url, params = payload)
    re.encoding = 'gbk'
    html = BeautifulSoup(re.text,'lxml')
    divs = html.findAll(style="margin-top:5px;")
    answer = []
    for div in divs:
        try:
            a = dict()
            link = div.b.a['href']
            a["name"] = div.b.a.getText()
            a["index"] = int(link.split('/')[-1].split('.')[0])
            ps = [i.getText() for i in div.findAll('p')]
            a["author"] = ps[0].split('/')[0].split(':')[1]
            a["publisher"] = ps[0].split('/')[1].split(':')[1]
            a["finished"] = True if ps[0].split('/')[2].split(':')[1]=='已完成' else False
            x,y,z = [int(i) for i in ps[1].split(':')[1].split('-')]
            a["last_update"] = date(x, y, z)
            a["introduction"] = ps[2]
            answer.append(a)
        except:
            print(div)
        #print(a)

    return answer   


    