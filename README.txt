python -m pip install --upgrade pip
pip install django
django-admin startproject project
cd project
python manage.py startapp pagge
python manage.py migrate
python manage.py runserver
python manage.py makemigrations

