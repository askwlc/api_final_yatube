# **API для социальной сети Yatube** 

![Python 3.7, 3.8](https://img.shields.io/badge/python-3.9-blue) ![django](https://img.shields.io/badge/Django-3.2-green)
___

## Описание:

Проект «API для Yatube» предоставляет доступ к постам, комментариям, группам и подпискам [социально сети Yatube](https://github.com/askwlc/hw05_final.git), в зависимости от статуса пользователя.

## Возможности

- Получение постов для любых пользователей
- Написание постов для авторизированных пользователей
- Разбиение постов на группы
- Получение и работа с комментариями к постам
- Подписка на понравившегося автора
- Подписка на авторов
- Аутентификацию по JWT-токену


## Примеры запросов к эндпоинтам и ответов:
> GET Получение публикаций api/v1/posts/
```200:```

```sh
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

> POST Создание публикации api/v1/posts/
```200:```

```sh
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

> PATCH Частичное обновление публикации api/v1/posts/{id}/
```200:```

```sh
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

```401:```

```sh
{
  "detail": "Учетные данные не были предоставлены."
}
```

```403:```

```sh
{
  "detail": "У вас недостаточно прав для выполнения данного действия."
}
```

```404:```

```sh
{
  "detail": "Страница не найдена."
}
```



## Установка:

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

