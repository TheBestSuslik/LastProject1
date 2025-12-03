Прототип зоомагазина на Django (упрощённо)
-----------------------------------------

Что есть в архиве:
- Управляемый Django-проект 'petshop_project'
- Приложение 'store' с моделями Category и Product
- Простые шаблоны и статический CSS
- SQLite база (не включена) — миграции надо сделать на вашей машине

Как запустить:
1. Создайте виртуальное окружение и установите Django:
   python -m venv venv
   source venv/bin/activate  # или venv\Scripts\activate на Windows
   pip install django

2. Перейдите в папку проекта и примените миграции:
   python manage.py makemigrations
   python manage.py migrate

3. Создайте суперпользователя:
   python manage.py createsuperuser

4. Запустите сервер:
   python manage.py runserver

5. Админка: http://127.0.0.1:8000/admin/
   Главная: http://127.0.0.1:8000/

Что можно добавить дальше:
- Корзина, оформление заказа
- Авторизация и профиль пользователя
- Загрузка изображений вместо URL
- Фильтрация и поиск по товарам
