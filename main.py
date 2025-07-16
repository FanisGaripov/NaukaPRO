from flask import Flask, render_template, session, redirect
import requests
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
app.secret_key = 'supersecretkey'


token = os.getenv('YANDEX_TOKEN')

headers = {
    'Authorization': f'OAuth {token}',
    'Content-Type': 'application/json'
}

date_to = ''


def scheduled_task():
    global date_to
    current_datetime = datetime.now()
    date_to = str(current_datetime.date())


scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_task, 'interval', hours=1)
scheduler.start()


params_for_shows = {
    'query_indicator': 'TOTAL_SHOWS',
    'date_from': '2025-01-01',
    'date_to': date_to,
}

params_for_clicks = {
    'query_indicator': 'TOTAL_CLICKS',
    'date_from': '2025-01-01',
    'date_to': date_to,
}

user_id = os.getenv('USER_ID')


@app.route('/change_language/ru', methods=['GET', 'POST'])
def language_ru():
    if 'page' not in session:
        session['page'] = '/'
        session.modified = True
    if 'language' not in session:
        session['language'] = 'Ru'
        session.modified = True
    session['language'] = 'Ru'
    session.modified = True
    print(session['language'])
    return redirect(session['page'])


@app.route('/change_language/tat', methods=['GET', 'POST'])
def language_tat():
    if 'page' not in session:
        session['page'] = '/'
        session.modified = True
    if 'language' not in session:
        session['language'] = 'Ru'
        session.modified = True
    session['language'] = 'Tat'
    session.modified = True
    print(session['language'])
    return redirect(session['page'])


@app.route('/')
def index():
    if 'page' not in session:
        session['page'] = '/'
        session.modified = True
    session['page'] = '/'
    session.modified = True
    if 'language' not in session:
        session['language'] = 'Ru'
        session.modified = True
    if session['language'] == 'Ru':
        return render_template('index.html')
    else:
        return render_template('index_tat.html')


@app.route('/aboutme')
def aboutme():
    if 'page' not in session:
        session['page'] = '/'
        session.modified = True
    session['page'] = '/aboutme'
    session.modified = True
    if 'language' not in session:
        session['language'] = 'Ru'
        session.modified = True
    if session['language'] == 'Ru':
        return render_template('aboutme.html')
    else:
        return render_template('aboutme_tat.html')


@app.route('/chemistrypro')
def chemistrypro():
    if 'language' not in session:
        session['language'] = 'Ru'
        session.modified = True
    if 'page' not in session:
        session['page'] = '/'
        session.modified = True
    session['page'] = '/chemistrypro'
    session.modified = True
    global date_to
    host_id = 'https:chemistrypro.onrender.com:443'
    response_shows = requests.get(
        f'https://api.webmaster.yandex.net/v4/user/{user_id}/hosts/{host_id}/search-queries/all/history/',
        headers=headers,
        params=params_for_shows
    )

    response_clicks = requests.get(
        f'https://api.webmaster.yandex.net/v4/user/{user_id}/hosts/{host_id}/search-queries/all/history/',
        headers=headers,
        params=params_for_clicks
    )

    data_shows = response_shows.json()
    data_clicks = response_clicks.json()
    print(data_shows)
    total_shows = int(sum(item['value'] for item in data_shows['indicators']['TOTAL_SHOWS']))
    total_clicks = int(sum(item['value'] for item in data_clicks['indicators']['TOTAL_CLICKS']))
    project_name = 'ChemistryPRO'
    gradient_color_1 = '#b3a5ed'
    gradient_color_2 = '#a5a8f2'
    main_screenshot = '/static/chemistrypro_main.png'
    stats_countries = 10
    stats_users_percentage = total_clicks/total_shows*100
    project_icon = '/static/favicon.svg'
    project_url = 'https://chemistrypro.onrender.com'
    screenshots = ['/static/chemistrypro_main.png', '/static/about.png', '/static/tg.png', '/static/tablica.png']
    if session['language'] == 'Ru':
        project_description = '''ChemistryPro — это веб-приложение, разработанное для изучения Химии школьного уровня 8-11 классов.
            ChemistryPRO предлагает структурированные материалы для освоения школьного курса химии и подготовки к экзаменам.<br> На сайте собраны:<br>

            • Разделы по общей, неорганической и органической химии<br>
            • Актуальные материалы ФИПИ для подготовки к ЕГЭ<br>
            • Интерактивные таблицы — периодическая система элементов с подробными характеристиками, таблица растворимости и таблица кислот<br>
            • Практические тренажёры — мини-игра для запоминания элементов периодической таблицы (особенно полезно для 8-9 классов)<br>
            • Искусственный интеллект - ИИ поможет и объяснит непонятную тему, а также способен решать химические задачи<br>

            Сайт работает как на компьютерах, так и на мобильных устройствах. Все материалы доступны бесплатно.<br>

            ChemistryPRO продолжает развиваться — постепенно добавляются новые материалы и улучшается функционал.<br>
            Сайт опубликован на хостинге render.com: <a href='https://chemistrypro.onrender.com/'>https://chemistrypro.onrender.com/</a>.'''
        short_description = 'ChemistryPRO — химический портал и ученический проект. Здесь Вы сможете воспользоваться разными функциями: начиная от вычисления Молярной Массы, заканчивая получением Структур Органических Веществ. Также на сайте присутствует много таблиц, и дополнительных функций.'
        technologies = ['<strong>1) Python:</strong>', 'Flask, chempy, g4f', '<strong>2) JavaScript:</strong>',
                        'Boostrap, MathJax',
                        '<strong>3) Html</strong>', '<strong>4) Метрики:</strong>',
                        'Webmaster, Yandex Metrika, Google Analytics']
        feat = [
            {
                "icon": "fas fa-microscope",
                "title": "Онлайн Лаборатория",
                "description": "Проводите эксперименты онлайн, без риска для здоровья"
            },
            {
                "icon": "fas fa-robot",
                "title": "AI-помощник",
                "description": "Персональный ассистент для решения разных задач"
            },
            {
                "icon": "fas fa-table",
                "title": "Уникальные интерактивные таблицы",
                "description": "Интерактивная таблица химических элементов, таблица кислот, таблица растворимости - и всё это в одном месте!"
            },
            {
                "icon": "fas fa-leaf",
                "title": "Органическая химия",
                "description": "Структуры веществ, просмотр 3D-молекул, органические реакции"
            },
            {
                "icon": "fas fa-flask",
                "title": "Неорганическая химия",
                "description": "Цепочки превращений, дописывание и уравнивание химических реакций"
            },
            {
                "icon": "fas fa-calculator",
                "title": "Общие функции",
                "description": "Электронная конфигурация, молярные массы, калькуляторы"
            }
        ]
        return render_template('project.html', project_name=project_name, short_description=short_description,
                               gradient_color_1=gradient_color_1, gradient_color_2=gradient_color_2, main_screenshot=main_screenshot,
                               video_review=None, stats_views=total_shows, stats_users=total_clicks, stats_users_percentage=stats_users_percentage,
                               project_url=project_url, technologies=technologies, stats_countries=stats_countries, project_icon=project_icon,
                               screenshots=screenshots, project_description=project_description, features=feat)
    else:
        project_description = '''ChemistryPro - 8-11 нче сыйныф укучылары дәрәҗәсендәге Химияне өйрәнү өчен эшләнгән веб-кушымта.
                    ChemistryPRO химиянең мәктәп курсын үзләштерү һәм имтиханнарга әзерләнү өчен структур материаллар тәкъдим итә.<br> Сайтта:<br>
                    
                    
                    • Гомуми, органик һәм органик булмаган химия буенча бүлекләр<br>
                    • БДИга әзерләнү өчен ФИПИның актуаль материаллары<br>
                    • «Интерактив таблицалар - элементларның периодик системасы, эретелү таблицасы һәм башка таблицалар<br>
                    • «Практик тренажёрлар - периодик таблица элементларын истә калдыру өчен мини-уен (бигрәк тә 8-9 сыйныфлар өчен файдалы)<br>
                    • Ясалма интеллект - аңлаешсыз теманы аңлата, шулай ук химик бурычларны чишә ала <br>
                    
                    
                    Сайт компьютерларда да, мобиль җайланмаларда да эшли. Барлык материаллар бушлай.<br>

                    ChemistryPRO үсүен дәвам итә - акрынлап яңа материаллар өстәлә һәм функционал яхшыра.
                       Сайт render.com хостингында урнаштырылды: <a href="https://chemistrypro.onrender.com/">https://chemistrypro.onrender.com/</a>'''
        short_description = 'ChemistryPRO - химик портал һәм өйрәнчек проект. Биредә сез төрле функцияләрдән файдалана аласыз: Моляр авырлыкны исәпләүдән башлап, Органик матдәләрнең структурасын алу белән тәмамлап. Шулай ук сайтта таблицалар һәм өстәмә функцияләр дә бар.'
        technologies = ['<strong>1) Python:</strong>', 'Flask, chempy, g4f', '<strong>2) JavaScript:</strong>',
                        'Boostrap, MathJax',
                        '<strong>3) Html</strong>', '<strong>4) Метрикалар:</strong>',
                        'Webmaster, Yandex Metrika, Google Analytics']
        feat = [
            {
                "icon": "fas fa-microscope",
                "title": "Онлайн Лаборатория",
                "description": "Сәламәтлек өчен куркыныч янамас өчен, онлайн экспериментлар үткәрегез"
            },
            {
                "icon": "fas fa-robot",
                "title": "AI-ярдәмче",
                "description": "Төрле вазифалар башкару өчен персональ булышчы"
            },
            {
                "icon": "fas fa-table",
                "title": "Уникаль интерактив таблицалар",
                "description": "Элементларның периодик системасы, эретелү таблицасы һәм башка таблицалар - барысы да бер сайтта!"
            },
            {
                "icon": "fas fa-leaf",
                "title": "Органик химия",
                "description": "Матдәләр структурасы, 3D-молекулаларны карау, органик реакцияләр"
            },
            {
                "icon": "fas fa-flask",
                "title": "Органик булмаган химия",
                "description": "Химик реакцияләрнең әверелешләре, аларны язып бетерү һәм тигезләү"
            },
            {
                "icon": "fas fa-calculator",
                "title": "Гомуми функцияләр",
                "description": "Электрон конфигурацияләр, моляр авырлыклар, калькуляторлар"
            }
        ]
        return render_template('project_tat.html', project_name=project_name, short_description=short_description,
                               gradient_color_1=gradient_color_1, gradient_color_2=gradient_color_2,
                               main_screenshot=main_screenshot,
                               video_review=None, stats_views=total_shows, stats_users=total_clicks,
                               stats_users_percentage=stats_users_percentage,
                               project_url=project_url, technologies=technologies, stats_countries=stats_countries,
                               project_icon=project_icon,
                               screenshots=screenshots, project_description=project_description, features=feat)



@app.route('/physicspro')
def physicspro():
    if 'language' not in session:
        session['language'] = 'Ru'
        session.modified = True
    if 'page' not in session:
        session['page'] = '/'
        session.modified = True
    session['page'] = 'physicspro'
    session.modified = True
    global date_to
    host_id = 'https:physicspro.onrender.com:443'
    response_shows = requests.get(
        f'https://api.webmaster.yandex.net/v4/user/{user_id}/hosts/{host_id}/search-queries/all/history/',
        headers=headers,
        params=params_for_shows
    )

    response_clicks = requests.get(
        f'https://api.webmaster.yandex.net/v4/user/{user_id}/hosts/{host_id}/search-queries/all/history/',
        headers=headers,
        params=params_for_clicks
    )

    data_shows = response_shows.json()
    data_clicks = response_clicks.json()

    total_shows = int(sum(item['value'] for item in data_shows['indicators']['TOTAL_SHOWS']))
    total_clicks = int(sum(item['value'] for item in data_clicks['indicators']['TOTAL_CLICKS']))
    project_name = 'PhysicsPRO'
    gradient_color_1 = '#cc80ff'
    gradient_color_2 = '#a319ff'
    main_screenshot = '/static/physicspro_main.png'
    stats_countries = 13
    stats_users_percentage = total_clicks / total_shows * 100
    project_icon = '/static/favicon.png'
    project_url = 'https://physicspro.onrender.com'
    screenshots = ['/static/physicspro_main.png', '/static/main2.png', '/static/aboutme.png', '/static/ege.png', '/static/ai.png']
    if session['language'] == 'Ru':
        project_description = '''PhysicsPRO — это образовательная платформа, разработанная для системного изучения школьного курса физики и подготовки к экзаменам.<br>
            Сайт предлагает:<br>
            Подготовка к ОГЭ и ЕГЭ с актуальными материалами ФИПИ<br>

            Интерактивные формулы с пояснениями<br>

            Визуализация физических законов и явлений<br>

            Калькуляторы для решения задач<br>

            Мини-игра для решения простых задач на скорость<br><br>

            Уникальные функции:<br>

            Искусственный интеллект для объяснения сложных тем<br>

            Возможность решения задач с пошаговым разбором<br>
            <br>

            Сайт полностью адаптирован для использования на компьютерах и мобильных устройствах. Все образовательные материалы доступны бесплатно.<br>

            PhysicsPRO постоянно развивается — мы добавляем новые учебные материалы, улучшаем существующие функции и работаем над расширением возможностей платформы.<br>
            Сайт опубликован на хостинге render.com: <a href='https://physicspro.onrender.com/'>https://physicspro.onrender.com/</a>.'''
        technologies = ['<strong>1)Python:</strong>', 'Flask, g4f', '<strong>2) JavaScript:</strong>',
                    'Boostrap, MathJax, Ajax', '<strong>3) Html</strong>', '<strong>4) Метрики:</strong>', 'Webmaster, Yandex Metrika']
        short_description = 'PhysicsPRO - это ваш персональный помощник в изучении физики. Получайте подробные объяснения, решайте задачи ЕГЭ и углубляйте свои знания с помощью передовых технологий искусственного интеллекта Physics AI.'

        feat = [
            {
                "icon": "fas fa-microscope",
                "title": "Онлайн Лаборатория",
                "description": "Проводите эксперименты онлайн, без риска для здоровья"
            },
            {
                "icon": "fas fa-robot",
                "title": "Умный AI-помощник",
                "description": "Персональный ассистент для решения разных задач, объяснения тем"
            },
            {
                "icon": "fas fa-info",
                "title": "Уникальные материалы по физике",
                "description": "Краткий конспект разделов, основные формулы, термины"
            },
            {
                "icon": "fas fa-book",
                "title": "Подготовка к ЕГЭ/ОГЭ",
                "description": "На сайте есть каталог заданий ФИПИ ЕГЭ и ОГЭ по физике"
            },
        ]
        return render_template('project.html', project_name=project_name, short_description=short_description,
                               gradient_color_1=gradient_color_1, gradient_color_2=gradient_color_2,
                               main_screenshot=main_screenshot,
                               video_review=None, stats_views=total_shows, stats_users=total_clicks,
                               stats_users_percentage=stats_users_percentage, features=feat,
                               project_url=project_url, technologies=technologies, stats_countries=stats_countries,
                               project_icon=project_icon, screenshots=screenshots, project_description=project_description)
    else:
        project_description = '''PhysicsPRO - ул физиканың мәктәп курсын системалы өйрәнү һәм имтиханнарга әзерлек өчен эшләнгән белем бирү платформасы.<br>
                    Сайтта:<br>
                    ФИПИның актуаль материаллары белән ТДИ һәм БДИга әзерлек<br>

                    Интерактив формулалар<br>

                    Визуализация физических законов и явлений<br>

                    Мәсьәләләрне чишү өчен калькуляторлар<br>

                    Тизлеккә гади мәсьәләләрне чишү өчен мини-уен<br><br>

                    Уникаль функцияләр:<br>

                    Катлаулы темаларны аңлату өчен ясалма интеллект<br>

                    Мәcьәләрне адымлап чишү мөмкинлеге<br>
                    <br>

                    Сайт компьютерларда һәм мобиль җайланмаларда файдалану өчен тулысынча җайлаштырылган. Барлык материаллар бушлай.<br>

                    PhysicsPRO даими үсә - без яңа уку материалларын өстибез, булган функцияләрне яхшыртабыз һәм мөмкинлекләрен киңәйтү өстендә эшлибез.<br>
                    Сайт render.com хостингында урнаштырылды: <a href='https://physicspro.onrender.com/'>https://physicspro.onrender.com/</a>.'''
        technologies = ['<strong>1)Python:</strong>', 'Flask, g4f', '<strong>2) JavaScript:</strong>',
                        'Boostrap, MathJax, Ajax', '<strong>3) Html</strong>', '<strong>4) Метрикалар:</strong>',
                        'Webmaster, Yandex Metrika']
        short_description = 'PhysicsPRO - сезнең физиканы өйрәнүдә шәхси ярдәмчегез. Physics AI ясалма интеллектының алдынгы технологияләре ярдәмендә БДИ биремнәрен чишегез һәм белемнәрегезне тирәнәйтегез.'

        feat = [
            {
                "icon": "fas fa-microscope",
                "title": "Онлайн Лаборатория",
                "description": "Сәламәтлек өчен куркыныч янамас өчен, онлайн экспериментлар үткәрегез"
            },
            {
                "icon": "fas fa-robot",
                "title": "AI-булышчы",
                "description": "Төрле вазифалар башкару өчен персональ булышчы"
            },
            {
                "icon": "fas fa-info",
                "title": "Уникаль материаллар",
                "description": "Һәр физика бүлеменең кыскача конспекты, төп формулалар, терминнар"
            },
            {
                "icon": "fas fa-book",
                "title": "БДИ/ТДИга әзерләнү",
                "description": "Сайтта ФИПИдагы Физика буенча БДИ/ТДИ биремнәре каталоглары бар"
            },
        ]
        return render_template('project_tat.html', project_name=project_name, short_description=short_description,
                               gradient_color_1=gradient_color_1, gradient_color_2=gradient_color_2,
                               main_screenshot=main_screenshot,
                               video_review=None, stats_views=total_shows, stats_users=total_clicks,
                               stats_users_percentage=stats_users_percentage, features=feat,
                               project_url=project_url, technologies=technologies, stats_countries=stats_countries,
                               project_icon=project_icon, screenshots=screenshots,
                               project_description=project_description)



@app.route('/informpro')
def informpro():
    if 'language' not in session:
        session['language'] = 'Ru'
        session.modified = True
    if 'page' not in session:
        session['page'] = '/'
        session.modified = True
    session['page'] = '/informpro'
    session.modified = True
    global date_to
    host_id = 'https:informpro.onrender.com:443'
    response_shows = requests.get(
        f'https://api.webmaster.yandex.net/v4/user/{user_id}/hosts/{host_id}/search-queries/all/history/',
        headers=headers,
        params=params_for_shows
    )

    response_clicks = requests.get(
        f'https://api.webmaster.yandex.net/v4/user/{user_id}/hosts/{host_id}/search-queries/all/history/',
        headers=headers,
        params=params_for_clicks
    )

    data_shows = response_shows.json()
    data_clicks = response_clicks.json()
    print(data_shows)
    # total_shows = int(sum(item['value'] for item in data_shows['indicators']['TOTAL_SHOWS']))
    # total_clicks = int(sum(item['value'] for item in data_clicks['indicators']['TOTAL_CLICKS']))
    total_shows = 1
    total_clicks = 1
    project_name = 'InformPRO'
    gradient_color_1 = '#8a2be2'
    gradient_color_2 = '#4b6cb7'
    main_screenshot = '/static/informpro_main.png'
    stats_countries = 1
    stats_users_percentage = total_clicks / total_shows * 100
    project_icon = '/static/favicon_inform.png'
    project_url = 'https://informpro.onrender.com'
    screenshots = ['/static/informpro_main.png', '/static/informpro_1.png', '/static/informpro_2.png', '/static/informpro_3.png']
    if session['language'] == 'Ru':
        project_description = '''InformPRO — это веб-приложение, разработанное для изучения Информатики 7-11 класса, а также программирования на базовом уровне. 
        InformPRO предлагает структурированные материалы для освоения программирования и математического мышления. Это помогает при подготовке к Основному и Единому Государственным экзаменам.<br> На сайте собраны:<br>

        • Материалы по программированию, базам данных и криптобезопасности<br>
        • Онлайн-компилятор для того, чтобы заниматься программированием, не выходя из браузера<br>
        • Искусственный интеллект - ИИ поможет и объяснит непонятную тему, а также способен решать и генерировать разные задачи<br>
        • Генератор задач по программированию<br>
        • Также для саморазвития на сайте представлен список идей для пет-проектов<br>
        
        Платформа адаптирована для использования на компьютерах и мобильных устройствах. Все материалы доступны бесплатно.<br>
        InformPRO продолжает развиваться — постепенно добавляются новые материалы и улучшается функционал.<br>
        Сайт опубликован на хостинге render.com: <a href='https://informpro.onrender.com/'>https://informpro.onrender.com/</a>.'''
        

        short_description = 'InformPRO — сайт по информатике и программированию. Здесь Вы сможете воспользоваться разными функциями: начиная от изучения языка программирования Python, заканчивая решением экзаменационных заданий ОГЭ и ЕГЭ. Также на сайте присутствует онлайн-компилятор, и дополнительные теоретические материалы.'
        technologies = ['<strong>1) Python:</strong>', 'Flask, g4f', '<strong>2) JavaScript:</strong>',
                        'Boostrap, MathJax', 'Boxicons', 'FontAwesome',
                        '<strong>3) Html</strong>', '<strong>4) Метрики:</strong>',
                        'Webmaster, Yandex Metrika']
        feat = [
            {
                "icon": "fas fa-laptop-code",
                "title": "Программирование",
                "description": "Уроки по Python, SQL, ИИ с практическими примерами"
            },
            {
                "icon": "fas fa-code",
                "title": "Онлайн-компилятор",
                "description": "Позволяет заниматься программирование прямо на сайте. Доступно 70 языков программирования"
            },
            {
                "icon": "fas fa-robot",
                "title": "AI-помощник",
                "description": "Искусственный интеллект, с которым можно обсудить программирование и информатику"
            },
            {
                "icon": "fas fa-check-double",
                "title": "Практика",
                "description": "Задания ОГЭ/ЕГЭ для закрепления знаний"
            },
            {
                "icon": "fas fa-project-diagram",
                "title": "Генерация задач",
                "description": "ИИ генерирует код разного уровня сложности: от простого до олимпиадного уровня"
            }
        ]
        return render_template('project.html', project_name=project_name, short_description=short_description,
                               gradient_color_1=gradient_color_1, gradient_color_2=gradient_color_2,
                               main_screenshot=main_screenshot,
                               video_review=None, stats_views=total_shows, stats_users=total_clicks,
                               stats_users_percentage=stats_users_percentage,
                               project_url=project_url, technologies=technologies, stats_countries=stats_countries,
                               project_icon=project_icon,
                               screenshots=screenshots, project_description=project_description, features=feat)
    else:
        project_description = '''InformPRO - 7-11 сыйныф Информатика материалын өйрәнү өчен эшләнгән веб-кушымта, шулай ук программалаштыруны да өйрәтә, математик фикерләүгә тәэсир итә. Бу Төп һәм Бердәм Дәүләт имтиханнарына әзерләнгәндә ярдәм итә. <br> Сайтта:<br>


                    • Программалаштыру, мәгълүматлар базасы һәм криптокуркынычсызлык буенча материаллар<br>
                    • Браузердан чыкмыйча гына программалаштыру өчен онлайн-компилятор<br>
                    • Шулай ук үз-үзеңне үстерү өчен сайтта пет-проектлар тәкъдимнәре исемлеге бар<br>
                    • Ясалма интеллект - аңлаешсыз теманы аңлата, шулай ук төрле мәсьәләләрне чишәргә һәм генерацияләргә сәләтле<br>


                    Сайт компьютерларда да, мобиль җайланмаларда да эшли. Барлык материаллар бушлай.<br>

                    InformPRO үсүен дәвам итә - акрынлап яңа материаллар өстәлә һәм функционал яхшыра.
                    Сайт render.com хостингында урнаштырылды: <a href='https://informpro.onrender.com/'>https://informpro.onrender.com/</a>'''
        short_description = 'InformPRO - программалаштыру һәм информатика сайты. Биредә сез төрле функцияләрдән файдалана аласыз: Python телен өйрәнүдән башлап, ТДИ һәм БДИ биремнәре чишү белән тәмамлап. Шулай ук сайтта онлайн-компилятор һәм өстәмә функцияләр дә бар.'
        technologies = ['<strong>1) Python:</strong>', 'Flask, g4f', '<strong>2) JavaScript:</strong>',
                        'Boostrap, MathJax', 'Boxicons', 'FontAwesome',
                        '<strong>3) Html</strong>', '<strong>4) Метрикалар:</strong>',
                        'Webmaster, Yandex Metrika']
        feat = [
            {
                "icon": "fas fa-laptop-code",
                "title": "Программалаштыру",
                "description": "Python, SQL, Ясалма интеллект дәресләре"
            },
            {
                "icon": "fas fa-code",
                "title": "Онлайн-компилятор",
                "description": "Браузердан чыкмыйча гына программалаштыру. 70 программалаштыру теле бар"
            },
            {
                "icon": "fas fa-robot",
                "title": "AI-булышчы",
                "description": "Ясалма интеллект - программалаштыру һәм информатика биремнәрен чишә белә"
            },
            {
                "icon": "fas fa-check-double",
                "title": "Кабатлау",
                "description": "ТДИ/БДИ биремнәрен кабатлау"
            },
            {
                "icon": "fas fa-project-diagram",
                "title": "Биремнәр генерациясе",
                "description": "Ясалма интеллект катлаулы биремнәр генерацияли"
            }
        ]
        return render_template('project_tat.html', project_name=project_name, short_description=short_description,
                               gradient_color_1=gradient_color_1, gradient_color_2=gradient_color_2,
                               main_screenshot=main_screenshot,
                               video_review=None, stats_views=total_shows, stats_users=total_clicks,
                               stats_users_percentage=stats_users_percentage,
                               project_url=project_url, technologies=technologies, stats_countries=stats_countries,
                               project_icon=project_icon,
                               screenshots=screenshots, project_description=project_description, features=feat)


@app.route('/contacts')
def contacts():
    if 'page' not in session:
        session['page'] = '/'
        session.modified = True
    session['page'] = '/contacts'
    session.modified = True
    if 'language' not in session:
        session['language'] = 'Ru'
        session.modified = True
    if session['language'] == 'Ru':
        return render_template('contacts.html')
    else:
        return render_template('contacts_tat.html')


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        scheduler.shutdown()
