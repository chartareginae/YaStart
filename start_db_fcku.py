from flask import Flask
from data import db_session
from data.startups import Startups

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def appi():
    user = Startups()
    user.title = "Воздух"
    user.budget = "3 000 000 RUB"
    user.sphere = "Недвижимость, строительство, ремонт"
    user.brief_info = 'Маркетплейс аренды загородной недвижимости'
    user.detailed_info = '''1.1. Данные о проекте. Проект «Воздух» был создан в 2021 году «Воздух» — Сервис для работы в сегменте аренды загородной недвижимости по всей России.

1.2. Основные цели проекта и что мы делаем. Главная цель проекта - объединить сегмент краткосрочной аренды загородной недвижимости внутри нашей платформы тем самым создав свою экосистему. На сегодняшний день не существует автоматизированного и специализированного сервиса для работы с загородной недвижимостью. ВОЗДУХ - сервис, объединяющий тех, кто хочет сдать в аренду загородный дом и тех, кто хочет его забронировать.

1.3. Ресурсы, необходимые для реализации проекта. Инвестиции в размере 3 млн. руб. за 10% доли компании. Сумма требуется для организации необходимых служб внутри платформы, расширить серверные мощности, сделать первую рекламу, нанять компетентных сотрудников для выхода компании на рынок.

1.4. Инвестиции, срок окупаемости и рентабельность продаж за 3 года. - Инвестиции 3 млн. руб. - Точка безубыточности достигается на 5 месяц; - Срок окупаемости проекта до 10 месяцев; - Средняя чистая прибыль в год 62 млн. руб. - Рентабельность продаж 74%

1.5. Расчет доли инвестора, уровень прибыли. Доля инвестора в проекте при инвестициях 3 млн. руб. составит 10% За 3 года уровень прибыли инвестора после возврата вложений составит от 16 000 000 руб. Доходность инвестора составит 130% годовых

1.6. Способы и временные рамки возврата инвестиций. Возврат до 11 месяцев с момента вхождения инвестора в проект при распределении прибыли в процентном соотношении 90% на 10% в пользу инвестора. После возврата вложенных средств % соотношение 90% на 10% в пользу инициаторов проекта.

 

Готовые документы: Инвестиционный меморандум, финансовая модель, презентация проекта, анализ конкурентов, юнит-экономика.

Проект прошел 2 акселератора АКСЕЛЕРАТОР МБМ и SKOLKOVO COMMUNITY.'''
    user.person = 'Кирилл'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def main():
    db_session.global_init("db/normal_db.db")
    # appi()
    app.run()


if __name__ == '__main__':
    main()
