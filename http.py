"""

Домашнее задание №3

Работа http

* Получите данные с помощью requests в формате json по ссылке 
  http://api.data.mos.ru/v1/datasets/2009/rows
* Добавьте на сайт страницу /names
* Выведите данные о именах новорожденных, получаемые при помощи
  функции из предыдущей задачи
* Пример простейшего оформления таблицы в файле table.html
* Ограничьте выводимые данные одним годом. Год должен указываться в 
  URL как параметр, например /names?year=2016

"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Домашнее задание №3"


if __name__ == "__main__":
    app.run(port=5010, debug=True)
