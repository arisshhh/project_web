from flask import Flask, render_template, make_response, jsonify, redirect, request
from flask_login import LoginManager, login_user, login_required, logout_user
from os import abort
from PIL import Image
from data import db_session
from data.films import Film
from data.users import User
from data.login_form import LoginForm
from data.register_form import RegisterForm
from data.add_film import AddFilmForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)


def search_film_all():
    db_sess = db_session.create_session()
    films = db_sess.query(Film).all()
    result = [(fl.img_film, fl.film_name, fl.rating, fl.genre,
               fl.catalog.catalog, fl.duration, fl.year_of_publication, fl.content) for fl in films]
    return result


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            if user.email == 'admin@mail.ru' and user.id == 1:
                return redirect('/index_admin')
            else:
                return redirect("/avt_all_films")
        return render_template('login.html', message="Неверный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
@app.route('/index')
def index():
    rez = search_film_all()
    return render_template("index.html", rez=rez, title='Главная')


@app.route("/sorting_name_film")
def sorting_name_film():
    rez = search_film_all()
    rez.sort(key=lambda x: x[1])
    return render_template("index.html", rez=rez, title="Отсортированный список фильмов по названию")


@app.route("/sorting_rating_film")
def sorting_rating_film():
    rez = search_film_all()
    rez.sort(key=lambda x: -x[2])
    return render_template("index.html", rez=rez, title="Отсортированный список фильмов по рейтингу")


@app.route("/avt_all_films")
def avt_all_film():
    db_sess = db_session.create_session()
    films = db_sess.query(Film).all()
    return render_template("avt_film.html", rez=films, title="Весь каталог")


@app.route('/edit_film/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_film(id):
    form = AddFilmForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        fl = db_sess.query(Film).filter(Film.id == id).first()
        if fl:
            form.film_name.data = fl.film_name
            form.genre.data = fl.genre
            form.rating.data = fl.rating
            form.year_of_publication.data = fl.year_of_publication
            form.duration.data = fl.duration
            form.content.data = fl.content
            form.id_catalog.data = fl.id_catalog
            form.img_film.data = fl.img_film
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        fl = db_sess.query(Film).filter(Film.id == id).first()
        if fl:
            fl.film_name = form.film_name.data
            fl.genre = form.genre.data
            fl.rating = form.rating.data
            fl.year_of_publication = form.year_of_publication.data
            fl.duration = form.duration.data
            fl.content = form.content.data
            fl.id_catalog = form.id_catalog.data
            fl.img_film = form.img_film.data
            db_sess.commit()
            return redirect('/index_admin')
        else:
            abort(404)
    return render_template('add_film.html', title='Редактирование фильма/сериала', form=form)


@app.route('/delete_film/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_film(id):
    db_sess = db_session.create_session()
    fl = db_sess.query(Film).filter(Film.id == id).first()
    if fl:
        db_sess.delete(fl)
        db_sess.commit()

    else:
        abort()
    return redirect('/index_admin')


@app.route('/index_admin', methods=['GET', 'POST'])
@login_required
def index_admin():
    return render_template('index_admin.html', title='Страница администратора')


@app.route('/view_films', methods=['GET', 'POST'])
@login_required
def view_films():
    db_sess = db_session.create_session()
    films_in_bd = db_sess.query(Film).all()
    return render_template('view_film.html', title='Просмотр таблицы с фильмами и сериалами', result=films_in_bd)


@app.route('/load_files', methods=['POST', 'GET'])
@login_required
def load_files_img():
    if request.method == 'GET':
        return render_template("load_files.html", title="Загрузка файлов изображений")
    elif request.method == 'POST':
        f = request.files['file']
        with open(f'static/img/{f.filename}', 'wb') as file:
            file.write(f.read())
        img = Image.open(f'static/img/{f.filename}')
        width = 200
        height = 250
        resized_img = img.resize((width, height), Image.ANTIALIAS)
        resized_img.save(f'static/img/{f.filename}')
        return render_template("load_files.html", title="Загрузка файлов изображений")


@app.route('/add_film', methods=['GET', 'POST'])
@login_required
def add_film():
    form = AddFilmForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        fl = Film()
        fl.film_name = form.film_name.data
        fl.genre = form.genre.data
        fl.rating = form.rating.data
        fl.year_of_publication = form.year_of_publication.data
        fl.duration = form.duration.data
        fl.content = form.content.data
        fl.id_catalog = form.id_catalog.data
        fl.img_film = form.img_film.data
        db_sess.add(fl)
        db_sess.commit()
        return redirect('/index_admin')
    return render_template('add_film.html', title='Добавление фильма', form=form)


def main():
    db_session.global_init("db/films.db")
    app.run()


if __name__ == '__main__':
    main()
