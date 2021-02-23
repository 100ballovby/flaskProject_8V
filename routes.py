from app import app
# из файла app.py импортирую переменную app (сам сайт)
from flask import render_template

'''
@app.путь('/адрес_страницы')
def название_фукнции():
    что_отображать_функцией
'''


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/about')
def about_page():
    """Рисую шаблон about.html и отображаю СВОЙ тег title"""
    return render_template('about.html', title='Страница о нас')


@app.route('/contact')
def contact_page():
    return render_template('contacts.html', title='Контакты')


@app.route('/news')
def news_page():
    posts = [
        {
            'author': {'username': 'Zodiac'},
            'body': 'Hello there! Im Zodiac!'
        },
        {
            'author': {'username': 'Architect'},
            'body': 'Zodiac is dummy!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'They are stupid! Hello there!'
        }
    ]
    return render_template('news.html', title='Новости', posts=posts)