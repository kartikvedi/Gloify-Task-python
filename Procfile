release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn bookstore.wsgi --log-level=info --log-file -
