# web: python unabjjsite/manage.py runserver 0.0.0.0:$PORT
web: cd unabjjsite && gunicorn unabjjsite.wsgi --bind=0.0.0.0:$PORT --workers=4 --access-logfile - --log-level INFO
