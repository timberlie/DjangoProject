
## 🎌 Веселье с флагами

Веб-приложение для изучения флагов мира в игровой форме.

## Автор
Timbelie

## Описание проекта
Проект представляет собой образовательный веб-сервис для изучения флагов разных стран. Приложение включает бесконечную игру "Угадай флаг" с тремя вариантами ответов, блог с интересными фактами о флагах, регистрацию и авторизацию пользователей, систему подсчёта очков.

## Технологии
- Python 3.8
- Django 4.2
- SQLite
- HTML/CSS (собственные стили)
- JavaScript (AJAX)

## Установка и запуск


git clone https://github.com/timberlie/DjangoProject.git
cd DjangoProject
python -m venv myvenv
myvenv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Открыть в браузере: http://127.0.0.1:8000/

## Функциональность

- **Главная страница** — карточки с описанием игры и блога, последние посты
- **Игра "Угадай флаги"** — случайный вопрос, три варианта флагов, подсчёт очков, мгновенная проверка ответа
- **Блог** — список статей о флагах, детальная страница, похожие статьи
- **Регистрация и вход** — валидация полей, проверка сложности пароля, читаемые сообщения об ошибках

## Проверка качества кода


pylint flag_game/


Результат: 8.5/10

## Коммиты

- add registration form
- add game logic
- fix CSRF error
- add blog templates
- add pylint fixes

## Контакты

GitHub: [timberlie](https://github.com/timberlie)
