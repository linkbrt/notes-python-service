API Сервер заметок.
Стек: aiohttp + postgresql + docker.

Эндпоинты:
- /register [POST] - Регистрация пользователя. Возвращает {access_token: str, refresh_token: str} при успешной регистрации. Требует атрибуты username и password в теле запроса.
- /refresh-token [POST] - Выпуск нового access token при истечении срока жизни токена. Требуется авторизация и атрибут refresh_token в теле запроса.

- / [GET] - Получение заметок пользователя. Возвращает json в формате [{id: int, text: str, user_id: int}]. Требуется авторизация.
- /create-note [POST] - Создание новой заметки. Орфографические ошибки проверяются сервисом Яндекс.Спеллер и автоматически исправляются. Возвращает 201 при успешном создании и 400 при неправильных данных. Требуется авторизация и атрибут text в теле запроса.


Коллекция Postman для тестов.
https://web.postman.co/workspace/linkbrt_workspace~7b9197ec-425f-4308-a758-dec1190765f5/folder/13431995-1d1165fe-2ff0-4a98-b1c4-c2df739cbf40

Инструкция по развертыванию:
Клонирование проекта:
- git clone git@github.com:linkbrt/notes-python-service.git
Создание файла с переменными окружения .env:
- За основу брать .env.template из репозитория
Построение и запуск докер контейнеров
- sudo docker compose build && sudo docker compose up -d
