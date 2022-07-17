# Содержание <a class="anchor" id="contents"> 

* [Описание](#about) 

* [Установка](#setup) 

* [Примеры](#examples) 

 

 

## Описание:<a class="anchor" id="about"> 

[к оглавлению](#contents) 

[к следующему разделу](#setup) 

 

Проект представляет собой готовый API для разворачивания и поддержания приложения социальной сети "Yatube". 

Приложение позволяет пользователям: 

* публиковать свои записи/посты/тексты 

* объединять их в сообщества 

* подписываться на других авторов 

* комментировать тексты других авторов 

 

Данный API позволит разработать самостоятельный клиент для взаимодействия с приложением "Yatube". 

 

 

## Установка:<a class="anchor" id="setup"> 

[к оглавлению](#contents) 

[к следующему разделу](#examples) 

 

Клонировать репозиторий и перейти в него в командной строке: 

 

``` 

git clone https://github.com/yandex-praktikum/kittygram.git 

``` 

 

``` 

cd api_final_yatube 

``` 

 

Cоздать и активировать виртуальное окружение: 

 

``` 

python3 -m venv venv 

``` 

 

``` 

source venv/bin/activate 

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

 

 

 

 

## Примеры:<a class="anchor" id="examples"> 

[к оглавлению](#contents) 

[к предыдущему разделу](#setup) 

* [Публикации](#posts) 

* [Комментарии](#comments) 

* [Сообщества](#groups) 

* [Подписки](#follow) 

* [Работа с токенами](#jwt) 

 

### Публикации:<a class="anchor" id="posts"> 

[обратно к примерам](#examples) 

#### Получить список всех публикаций. 

При указании параметров limit и offset выдача работает с пагинацией. 

``` 

GET: http://127.0.0.1:8000/api/v1/posts/ 

``` 

Пример ответа: 

``` 

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

Коды ответов: 200 

 

#### Создание публикации 

Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены. 

``` 

POST: http://127.0.0.1:8000/api/v1/posts/ 

{ 

  "text": "string", 

  "image": "string", 

  "group": 0 

} 

``` 

Пример ответа: 

``` 

{ 

  "id": 0, 

  "author": "string", 

  "text": "string", 

  "pub_date": "2019-08-24T14:15:22Z", 

  "image": "string", 

  "group": 0 

} 

``` 

Коды ответов: 201, 400, 401 

 

#### Получение публикации 

Получение публикации по id. 

``` 

GET: http://127.0.0.1:8000/api/v1/posts/{id}/ 

``` 

Пример ответа: 

``` 

{ 

  "id": 0, 

  "author": "string", 

  "text": "string", 

  "pub_date": "2019-08-24T14:15:22Z", 

  "image": "string", 

  "group": 0 

} 

``` 

Коды ответов: 200. 404 

 

#### Обновление публикации 

Обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены. 

``` 

PUT: http://127.0.0.1:8000/api/v1/posts/{id}/ 

{ 

  "text": "string", 

  "image": "string", 

  "group": 0 

} 

``` 

Пример ответа: 

``` 

{ 

  "id": 0, 

  "author": "string", 

  "text": "string", 

  "pub_date": "2019-08-24T14:15:22Z", 

  "image": "string", 

  "group": 0 

} 

``` 

Коды ответов: 200, 400, 401, 403, 404 

 

### Комментарии:<a class="anchor" id="comments"> 

[обратно к примерам](#examples) 

#### Получение комментариев 

Получение всех комментариев к публикации. 

``` 

GET: http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ 

``` 

Пример ответа: 

``` 

[ 

  { 

    "id": 0, 

    "author": "string", 

    "text": "string", 

    "created": "2019-08-24T14:15:22Z", 

    "post": 0 

  } 

] 

``` 

Коды ответов: 200, 404 

 

### Сообщества:<a class="anchor" id="groups"> 

[обратно к примерам](#examples) 

#### Список сообществ 

Получение списка доступных сообществ. 

``` 

GET: http://127.0.0.1:8000/api/v1/groups/ 

``` 

Пример ответа: 

``` 

[ 

  { 

    "id": 0, 

    "title": "string", 

    "slug": "string", 

    "description": "string" 

  } 

] 

``` 

Коды ответов: 200, 404 

 

### Подписки:<a class="anchor" id="follow"> 

[обратно к примерам](#examples) 

#### Подписки 

Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены. 

``` 

GET: http://127.0.0.1:8000/api/v1/follow/ 

``` 

Пример ответа: 

``` 

[ 

  { 

    "user": "string", 

    "following": "string" 

  } 

] 

``` 

Коды ответов: 200, 401 

 

### Работа с токенами:<a class="anchor" id="jwt"> 

[обратно к примерам](#examples) 

#### Получить JWT-токен 

``` 

POST: http://127.0.0.1:8000/api/v1/jwt/create/ 

{ 

  "username": "string", 

  "password": "string" 

} 

``` 

Пример ответа: 

``` 

{ 

  "refresh": "string", 

  "access": "string" 

} 

``` 

Коды ответов: 200, 400, 401 
