from flask import Flask, render_template
import requests
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)


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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')


@app.route('/chemistrypro')
def chemistrypro():
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

    total_shows = int(sum(item['value'] for item in data_shows['indicators']['TOTAL_SHOWS']))

    total_clicks = int(sum(item['value'] for item in data_clicks['indicators']['TOTAL_CLICKS']))
    project_name = 'ChemistryPRO'
    short_description = 'ChemistryPRO — химический портал и ученический проект. Здесь Вы сможете воспользоваться разными функциями: начиная от вычисления Молярной Массы, заканчивая получением Структур Органических Веществ. Также на сайте присутствует много таблиц, и дополнительных функций.'
    gradient_color_1 = '#b3a5ed'
    gradient_color_2 = '#a5a8f2'
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
    main_screenshot = '/static/chemistrypro_main.png'
    stats_countries = 10
    stats_users_percentage = total_clicks/total_shows*100
    project_icon = '/static/favicon.svg'
    project_url = 'https://chemistrypro.onrender.com'
    screenshots = ['/static/chemistrypro_main.png', '/static/about.png', '/static/tg.png', '/static/tablica.png']
    technologies = ['<strong>1) Python:</strong>', 'Flask, chempy, g4f', '<strong>2) JavaScript:</strong>', 'Boostrap, MathJax',
                    '<strong>3) Html</strong>', '<strong>4) Метрики:</strong>', 'Webmaster, Yandex Metrika, Google Analytics']
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


@app.route('/physicspro')
def physicspro():
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
    short_description = 'PhysicsPRO - это ваш персональный помощник в изучении физики. Получайте подробные объяснения, решайте задачи ЕГЭ и углубляйте свои знания с помощью передовых технологий искусственного интеллекта Physics AI.'
    gradient_color_1 = '#cc80ff'
    gradient_color_2 = '#a319ff'
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
    main_screenshot = '/static/physicspro_main.png'
    stats_countries = 13
    stats_users_percentage = total_clicks / total_shows * 100
    project_icon = '/static/favicon.png'
    project_url = 'https://physicspro.onrender.com'
    screenshots = ['/static/physicspro_main.png', '/static/main2.png', '/static/aboutme.png', '/static/ege.png', '/static/ai.png']
    technologies = ['<strong>1)Python:</strong>', 'Flask, g4f', '<strong>2) JavaScript:</strong>',
                    'Boostrap, MathJax, Ajax', '<strong>3) Html</strong>', '<strong>4) Метрики:</strong>', 'Webmaster, Yandex Metrika']
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


@app.route('/informpro')
def informpro():
    return render_template('informpro.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        scheduler.shutdown()