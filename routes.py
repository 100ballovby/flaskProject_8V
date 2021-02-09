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
