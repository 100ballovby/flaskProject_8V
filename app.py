from flask import Flask  # импортируем модуль flask


app = Flask(__name__)
# app - это сам ваш сайт


from routes import *
# импортирую файл с путями для сайта

if __name__ == '__main__':
    app.run()
    # эта штука его запускает
