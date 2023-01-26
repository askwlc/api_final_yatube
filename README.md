# **API for social network**

![Python 3.7, 3.8](https://img.shields.io/badge/python-3.9-blue) ![django](https://img.shields.io/badge/Django-3.2-green)
___

**API for social network** - Yandex Practicum educational project for learning how to work with the api.

### Examples of requests and responses:
![get](https://img.shields.io/badge/%20-GET%20-green) ```http://127.0.0.1:8000/api/v1/posts/{id}/```
```json
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```

![](https://img.shields.io/badge/%20-POST%20-blue)   ```/api/v1/posts/ ```

```json
{
"text": "string",
"image": "jpg",
"group": 1
}
```
```json
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "jpg",
"group": 1
}
```



### Installation:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:askwlc/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

