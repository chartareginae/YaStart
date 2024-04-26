from flask import Flask, request
from flask import render_template
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from data import db_session
from data.users import User
from data.startups import Startups
import random
import urllib.request

SqlAlchemyBase = orm.declarative_base()

__factory = None

app = Flask(__name__)
flag = False
otrasls = ['style/IT1.jpg ', 'style/med1.jpg ', 'style/place.jpg ', 'style/pravo.jpg ',
           'style/trans1.jpg ', 'style/sciense1.jpg ']
listt = (('Новый стартап', '/new_start'), ('Главная', '/main'), ('Личный кабинет', '/lk'), ('Выйти', '/logout'))
listt1 = (('Новый стартап', '/new_start'), ('Главная', '/main'), ('Войти/Зарегистрироваться', '/login'))
photos = ['style/team1.jpg', 'style/invest1.jpg', 'style/startup1.jpg', 'style/team1.jpg', 'style/invest1.jpg',
          'style/startup1.jpg', 'style/team1.jpg', 'style/invest1.jpg', 'style/startup1.jpg', 'style/team1.jpg',
          'style/invest1.jpg']  # импорт из базы данных топ-10
a = len(photos)
sphere1 = {'1': 'Интернет-проекты, приложения', '2': 'Здоровье, медицина, фармацевтика',
           '3': 'Недвижимость, строительство, ремонт', '4': 'Финансы, управление, право',
           '5': 'Транспорт, топливо, логистика', '6': 'Наука, образование, кульура'}


@app.route('/')
@app.route('/main')
def main():
    popular = app_popular()
    random.shuffle(popular)
    if flag:
        return render_template('main_page.html', otrasls=otrasls, listt=listt, info=popular)
    else:
        return render_template('main_page.html', otrasls=otrasls, listt=listt1, info=popular)


@app.route('/login')
def registration_and_login():
    return render_template('login.html', listt=listt1)


@app.route('/new_start')
def sphere():
    popular = app_popular()
    random.shuffle(popular)
    if flag:
        return render_template('new_startup.html', listt=listt)
    else:
        return render_template('login.html', listt=listt1)


@app.route('/idea')
def idea():
    info = app_state('Есть идея')
    a = len(info)
    if flag:
        return render_template('first.html', info=info, la=a, listt=listt, title='Есть идея')
    else:
        return render_template('first.html', info=info, la=a, listt=listt1, title='Есть идея')


@app.route('/registration')
def regist():
    return render_template('registration.html', listt=listt1)


@app.route('/IT')
def IT():
    it = app_sphere('Интернет-проекты, приложения')
    itlen = len(it)
    return render_template('sphere.html', listt=listt, la=itlen, info=it, title='Интернет-проекты, приложения')


@app.route('/med')
def med():
    med = app_sphere('Здоровье, медицина, фармацевтика')
    medlen = len(med)
    return render_template('sphere.html', listt=listt, la=medlen, info=med, title='Здоровье, медицина, фармацевтика')


@app.route('/construction')
def const():
    con = app_sphere('Недвижимость, строительство, ремонт')
    conlen = len(con)
    return render_template('sphere.html', listt=listt, la=conlen, info=con, title='Недвижимость, строительство, ремонт')


@app.route('/pravo')
def pravo():
    prav = app_sphere('Финансы, управление, право')
    pravlen = len(prav)
    return render_template('sphere.html', listt=listt, la=pravlen, info=prav, title='Финансы, управление, право')


@app.route('/transport')
def trans():
    tran = app_sphere('Транспорт, топливо, логистика')
    tranlen = len(tran)
    return render_template('sphere.html', listt=listt, la=tranlen, info=tran, title='Транспорт, топливо, логистика')


@app.route('/science')
def science():
    sci = app_sphere('Наука, образование, кульура')
    scilen = len(sci)
    return render_template('sphere.html', listt=listt, la=scilen, info=sci, title='Наука, образование, кульура')


@app.route('/startupp')
def startupp():
    return render_template('startup.html', listt=listt)  # доделать


@app.route('/team')
def team():
    info = app_state('Собрана команда')
    a = len(info)
    if flag:
        return render_template('first.html', info=info, la=a, listt=listt, title='Собрана команда')
    else:
        return render_template('first.html', info=info, la=a, listt=listt1, title='Собрана команда')


@app.route('/hello', methods=['POST'])
def reg():
    global flag
    global nim
    nim = request.form['log']
    email = request.form['email']
    password = request.form['pass1']
    password_re = request.form['pass2']
    if password == password_re:
        app_registration(nim, email, password)
        flag = True
        popular = app_popular()
        random.shuffle(popular)
        return render_template('main_page.html', photos=photos, la=a, otrasls=otrasls, listt=listt, info=popular)
    return render_template('registration.html', photos=photos, la=a, otrasls=otrasls, listt=listt1)


@app.route('/hell', methods=['POST'])
def log():
    global flag
    global nim
    nim = request.form['log']
    password = request.form['pass']
    if app_enter(nim, password) == 'Ok':
        flag = True
        popular = app_popular()
        random.shuffle(popular)
        return render_template('main_page.html', photos=photos, la=a, otrasls=otrasls, listt=listt, info=popular)
    return render_template('login.html', photos=photos, la=a, listt=listt1)


@app.route('/invest')
def invest():
    info = app_state('Инвестируется')
    a = len(info)
    if flag:
        return render_template('first.html', info=info, la=a, listt=listt, title='Инвестируется')
    else:
        return render_template('first.html', info=info, la=a, listt=listt1, title='Инвестируется')


@app.route('/new_startt', methods=['POST'])
def new_start():
    status = request.form['status']
    title = request.form['title']
    budget = request.form['budget']
    spheree = request.form['sph']
    sh_info = request.form['sh_info']
    big_info = request.form['big_info']
    spheree = sphere1[spheree]
    new_startups(title, budget, spheree, sh_info, big_info, status)
    popular = app_popular()
    random.shuffle(popular)
    return render_template('main_page.html', photos=photos, la=a, otrasls=otrasls, listt=listt, info=popular)


@app.route('/lk')
def lk():
    my_startups = app_person(nim)
    a = len(my_startups)
    return render_template('lk.html', listt=listt, la=a, info=my_startups)


@app.route('/logout')
def logout():
    global nim
    global flag
    flag = False
    nim = None
    popular = app_popular()
    random.shuffle(popular)
    return render_template('main_page.html', otrasls=otrasls, listt=listt1, info=popular)


@app.route('/about_project')
def about_project():
    return render_template('ab_proj.html', otrasls=otrasls, listt=listt1)


def app_registration(name, email, password):
    global db_sess
    user = User()
    user.name = name
    user.hashed_password = hasher(password)
    user.email = email
    db_sess.add(user)
    db_sess.commit()


def app_sphere(sphere):
    global db_sess
    lis = []
    for user in db_sess.query(Startups).all():
        if user.sphere == sphere:
            lis.append([user.title, user.budget, user.sphere, user.brief_info, user.detailed_info, user.person])
    return lis


def app_person(person):
    global db_sess
    lis = []
    for user in db_sess.query(Startups).all():
        if user.person == person:
            lis.append([user.title, user.budget, user.sphere, user.brief_info, user.detailed_info, user.person])
    return lis


def app_popular():
    global db_sess
    lis = []
    for user in db_sess.query(Startups).all():
        lis.append([user.title, user.budget, user.sphere, user.brief_info, user.detailed_info, user.id])
    return lis

def app_state(key):
    global db_sess
    lis = []
    for user in db_sess.query(Startups).all():
        if user.state == key:
            lis.append([user.title, user.budget, user.sphere, user.brief_info, user.detailed_info, user.person, user.state])
    return lis

def app_enter(name, password):
    global db_sess
    for user in db_sess.query(User).all():
        if user.name == name and user.hashed_password == hasher(password) and name != '' and password != '':
            return 'Ok'
        # Че-то дописать


def new_startups(name, budget, sphere, brief_info, detailed_info, state):
    global db_sess
    user = Startups()
    user.title = name
    user.budget = budget
    user.sphere = sphere
    user.brief_info = brief_info
    user.detailed_info = detailed_info
    user.person = nim
    user.state = state
    db_sess.add(user)
    db_sess.commit()


def hasher(password):
    password_hashed = ''
    for i in range(len(password)):
        if i % 2 == 0:
            password_hashed += chr(ord(password[i]) + i)
        else:
            password_hashed += chr(ord(password[i]) - i)
    return password_hashed


def dehasher(password_hashed):
    password = ''
    for i in range(len(password_hashed)):
        if i % 2 != 0:
            password += chr(ord(password_hashed[i]) + i)
        else:
            password += chr(ord(password_hashed[i]) - i)
    return password


def mainn():
    global db_sess
    db_session.global_init("db/normal_db.db")
    db_sess = db_session.create_session()
    app.run(port=8000, host='0.0.0.0')


if __name__ == '__main__':
    mainn()