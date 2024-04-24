from flask import Flask
from flask import render_template
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

SqlAlchemyBase = orm.declarative_base()

__factory = None

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    photos = ['style/team1.jpg', 'style/invest1.jpg', 'style/startup1.jpg', 'style/team1.jpg', 'style/invest1.jpg',
              'style/startup1.jpg', 'style/team1.jpg', 'style/invest1.jpg', 'style/startup1.jpg', 'style/team1.jpg',
              'style/invest1.jpg']
    otrasls = ['style/IT1.jpg ', 'style/med1.jpg ', 'style/place.jpg ', 'style/pravo.jpg ',
               'style/trans1.jpg ', 'style/sciense1.jpg ']
    return render_template('main_page.html', photos=photos, otrasls=otrasls)


@app.route('/login')
def registration_and_login():
    return render_template('login.html')


@app.route('/sphere')
def sphere():
    return render_template('mars.html', title='OK')


@app.route('/registration')
def regist():
    return render_template('registration.html')


@app.route('/favorites')
def fav():
    photos = ['style/team1.jpg', 'style/invest1.jpg', 'style/startup1.jpg', 'style/team1.jpg', 'style/invest1.jpg',
              'style/startup1.jpg', 'style/team1.jpg', 'style/invest1.jpg', 'style/startup1.jpg', 'style/team1.jpg',
              'style/invest1.jpg']
    a = len(photos)
    return render_template('favorites.html', photos=photos, la=a)


# def global_init(db_file):
#     global __factory
#
#     if __factory:
#         return
#
#     if not db_file or not db_file.strip():
#         raise Exception("Необходимо указать файл базы данных.")
#
#     conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
#     print(f"Подключение к базе данных по адресу {conn_str}")
#
#     engine = sa.create_engine(conn_str, echo=False)
#     __factory = orm.sessionmaker(bind=engine)
#
#     SqlAlchemyBase.metadata.create_all(engine)
#
#
# def create_session() -> Session:
#     global __factory
#     return __factory()
#

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
