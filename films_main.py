from data.films import Film
from data.catalog import Catalog
from flask import Flask
from data import db_session
from PIL import Image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/films.db")
    session = db_session.create_session()
    film = Film()
    film.film_name = 'Один дома'
    film.rating = 8.3
    film.genre = 'комедия, семейный'
    film.id_catalog = 1
    film.duration = '103 мин. / 01:43'
    film.year_of_publication = 1990
    film.content = '''Американское семейство отправляется из Чикаго в Европу, 
                   но в спешке сборов бестолковые родители забывают дома... одного из своих детей. Юное создание,
                   однако, не теряется и демонстрирует чудеса изобретательности. И когда в дом залезают грабители,
                   им приходится не раз пожалеть о встрече с милым крошкой.'''
    film.img_film = 'one_home.jpg'
    session.add(film)
    files_img(film.img_film)

    session.commit()

    film = Film()
    film.film_name = 'Уэйн'
    film.rating = 8.2
    film.genre = 'боевик, комедия'
    film.id_catalog = 2
    film.duration = '1 сезон(10 серий по 30 минут)'
    film.year_of_publication = 2019
    film.content = '''16-летний Уэйн вместе с подругой отправляется на мотоцикле из Бостона во Флориду, чтобы вернуть
                   старенький Понтиак своего отца, который был украден до его смерти.'''
    film.img_film = 'wayne.jpg'
    session.add(film)
    files_img(film.img_film)

    session.commit()

    film = Film()
    film.film_name = 'Тёмные отражения'
    film.rating = 6.2
    film.genre = 'боевик, фантастика, драма, приключения'
    film.id_catalog = 1
    film.duration = '104 мин. / 01:44'
    film.year_of_publication = 2018
    film.content = '''После того, как неизвестная болезнь убивает 98% американских детей, 2% выживших, у которых
     обнаруживаются суперспособности, отправляют в специальные лагеря. 16-летняя девушка сбегает из такого лагеря и 
     присоединяется к группе других подростков, которые скрываются от правительства.'''
    film.img_film = 'dark_reflections.jpg'
    session.add(film)
    files_img(film.img_film)

    session.commit()

    film = Film()
    film.film_name = 'Кома'
    film.rating = 6.5
    film.genre = 'боевик, фэнтези, фантастика, приключения'
    film.id_catalog = 1
    film.duration = '111 мин. / 01:51'
    film.year_of_publication = 2020
    film.content = '''После аварии молодой талантливый архитектор приходит в себя в очень странном мире, 
    лишь частично похожем на реальность. Ему предстоит выяснить, по каким законам существует это пространство, 
    бороться за жизнь, встретить любовь, найти, наконец, выход в реальный мир и осознать его по-новому, поняв, 
    что такое КОМА на самом деле.'''
    film.img_film = 'coma.jpg'
    session.add(film)
    files_img(film.img_film)

    session.commit()

    film = Film()
    film.film_name = 'Токийский гуль'
    film.rating = 7.1
    film.genre = 'боевик, фэнтези, аниме, мультфильм, триллер, ужасы'
    film.id_catalog = 2
    film.duration = '4 сезона(24 мин. серия (1152 мин. всего))'
    film.year_of_publication = 2018
    film.content = '''С обычным студентом Кэном Канэки случается беда, парень попадает в больницу. Но на этом 
    неприятности не заканчиваются: ему пересаживают органы гулей – существ, поедающих плоть людей. После злосчастной 
    операции Канэки становится одним из чудовищ, пытается стать своим, но для людей он теперь изгой, обреченный на 
    уничтожение.'''
    film.img_film = 'tokyo_ghoul.jpg'
    session.add(film)
    files_img(film.img_film)

    session.commit()

    film = Film()
    film.film_name = 'Москва слезам не верит'
    film.rating = 8.4
    film.genre = 'комедия, драма'
    film.id_catalog = 1
    film.duration = '150 мин. / 02:30'
    film.year_of_publication = 1979
    film.content = '''Москва, 1950-е годы. Три молодые провинциалки приезжают в Москву в поисках того, что ищут люди во 
    всех столицах мира — любви, счастья и достатка. Антонина выходит замуж, растит детей, любит мужа. Людмиле Москва 
    представляется лотереей, в которой она должна выиграть свое особенное счастье. Катерина же отчаянно влюбляется, 
    но избранник ее оставляет. Однако она не опускает руки, в одиночку растит дочь и к тому же успевает делать 
    блестящую карьеру. В 40 лет судьба дарит ей неожиданную встречу.'''
    film.img_film = 'Moscow_does_not_believe_in_tears.jpg'
    session.add(film)
    files_img(film.img_film)

    session.commit()

    film = Film()
    film.film_name = 'Человек дождя'
    film.rating = 8.2
    film.genre = 'драма'
    film.id_catalog = 1
    film.duration = '133 мин. / 02:13'
    film.year_of_publication = 1988
    film.content = '''Грубоватому и эгоистичному молодому человеку Чарли в наследство от отца достались лишь розовые 
    кусты да «Бьюик» 1949 года, а львиная доля наследства уходит его брату-аутисту Раймонду. Задавшись целью отобрать 
    «свою долю», Чарли похищает старшего брата. Но когда выясняет, что Раймонд обладает недюжими математическими 
    способностями, памятью и внимательностью, решает использовать это в корыстных целях.'''
    film.img_film = 'rain_man.jpg'
    session.add(film)
    files_img(film.img_film)

    session.commit()

    film = Film()
    film.film_name = 'Иван Васильевич меняет профессию'
    film.rating = 8.8
    film.genre = 'драма'
    film.id_catalog = 1
    film.duration = '88 мин. / 01:28'
    film.year_of_publication = 1973
    film.content = '''Грубоватому и эгоистичному молодому человеку Чарли в наследство от отца достались лишь розовые 
        кусты да «Бьюик» 1949 года, а львиная доля наследства уходит его брату-аутисту Раймонду. Задавшись целью отобрать 
        «свою долю», Чарли похищает старшего брата. Но когда выясняет, что Раймонд обладает недюжими математическими 
        способностями, памятью и внимательностью, решает использовать это в корыстных целях.'''
    film.img_film = 'Ivan_Vasilyevich_is_changing_his_profession.jpg'
    session.add(film)
    files_img(film.img_film)

    session.commit()

    film = Film()
    film.film_name = 'Вышка'
    film.rating = 6.7
    film.genre = 'триллер'
    film.id_catalog = 1
    film.duration = '107 мин. / 01:47'
    film.year_of_publication = 2022
    film.content = '''После гибели Дэна в результате падения со скалы его жена Бекки, ранее увлекавшаяся экстремальными
     развлечениями, впала в депрессию. Год спустя девушка всё ещё не может прийти в себя и регулярно заливает горе 
     алкоголем, когда в её жизни внезапно появляется старая боевая подруга Хантер. Она предлагает почтить память Дэна, 
     забравшись на телерадиомачту B67 и развеяв там его прах. Девушки отправляются к самому высокому сооружению 
     Соединённых Штатов, даже не представляя, с чем им придётся столкнуться на его верхушке.'''
    film.img_film = 'fall.jpg'
    session.add(film)
    files_img(film.img_film)

    session.commit()

    film = Film()
    film.film_name = 'Конец света'
    film.rating = 7.4
    film.genre = 'комедия, фэнтези'
    film.id_catalog = 2
    film.duration = '1 сезон(8 серий)'
    film.year_of_publication = 2022
    film.content = '''В районе Чертаново, известном периодическими вторжениями и притяжениями, внезапно объявляется сам 
    Князь Тьмы. У него грандиозные планы, но для их реализации ему нужна помощь сына — кассира супермаркета, который к 
    отцу из преисподней имеет массу вопросов. Всевластному Князю Тьмы придётся строить отношения с земными 
    родственниками, чтобы осуществить задуманное и преподать урок человечеству.'''
    film.img_film = 'the_end_of_the_world.jpg'
    session.add(film)
    files_img(film.img_film)

    session.commit()


def files_img(filename):
    img = Image.open(f'static/img/{filename}')
    width = 200
    height = 250
    resized_img = img.resize((width, height), Image.ANTIALIAS)
    resized_img.save(f'static/img/{filename}')


if __name__ == '__main__':
    main()