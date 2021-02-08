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
    return '<p>Страница О нас</p>'


@app.route('/contact')
def contact_page():
    return '<p>Страница контакты</p>'
