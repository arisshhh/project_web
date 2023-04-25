from data.catalog import Catalog
from flask import Flask
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/films.db")
    session = db_session.create_session()

    ct = Catalog()
    ct.catalog = 'фильм'
    session.add(ct)

    ct = Catalog()
    ct.catalog = 'сериал'
    session.add(ct)

    session.commit()


if __name__ == '__main__':
    main()