# Для запуска приложения
- Установить пакеты(если не стоят) pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

# Для запука тестов
- python manage.py test

# Для запуска через coverage
- coverage run manage.py test

# Для генерации отчета 
- coverage html --include="../django_test*"


# Homework 1
В файлах 
- library/models.py
- library/forms.py
- library/views.py

был добавлен код. При запуске тестов и построения отчета, видно, что эти файлы 
покрыты не полностью. Необходимо добиться 100% по каждому из файлов.

### Создаем свою ветку, пушим в свою ветку, ставим пулреквест на master


# Полезные ссылки
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
- https://docs.djangoproject.com/en/2.1/topics/testing/overview/


# Homework 2
Задание - easy
- Добавить в приложение library статику - bootstrap
https://getbootstrap.com/docs/4.1/getting-started/download/
- Подключить к темплейту
- Выводить модель Book в виде таблицы (пример таблицы https://getbootstrap.com/docs/4.1/content/tables/)
- В конетекст процессоре, отдавать модель Book, отсортированные по name

Задание easy*

- Создать модель галереи
- В админке добавить возможность загружать в эту модель - картинки
- Создать отдельную view для отдачи галереи по id
- рендерить на отдельном темплейте галерею
- галерею взять отсюда https://getbootstrap.com/docs/4.1/components/carousel/#with-indicators

# Полезные ссылки 
- https://docs.djangoproject.com/en/2.1/howto/static-files/
- https://docs.djangoproject.com/ko/2.1/ref/templates/api/

# Homework 3
1) Создать middleware, которая считает сколько времени отрабатывала каждая из view. Результат записать в request
2) В файле library/view.py создать две вью при помощи django-rest-framework: первая - обновляет уже существующую запись, вторая - удаляет.

# Полезные ссылки
- https://docs.djangoproject.com/en/2.1/topics/http/middleware/
- http://www.django-rest-framework.org/api-guide/generic-views/#updatemodelmixin


