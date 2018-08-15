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


# Homework
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
