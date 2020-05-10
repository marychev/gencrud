	git clone git@bitbucket.org:marychev/homebio.git


    cd PROJECT_NAME
    virtualenv --python=python3 venv
	source venv/bin/activate
	cd gencrud/
	pip install -r requirements.txt
	python manage.py collectstatic --noinput
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver
	

#  Развертывание проекта 

Структура папок проекта
    
    PROJECT_NAME
    mkdir gencrud_v10
    cd gencrud_v10
    
проверяем `ls`. Должны быть следующие директории 
* app 
* gencrud 
* theme


Ставим виртуальное окружение. Активируем.

	virtualenv --python=python3 venv
	source venv/bin/activate


Устанавливаем Джанго и все необходимые зависимости. Входим в папку где лежит файл `manage.py`.
	
	 cd ~/projects/gencrud_v10/gencrud/
	 pip install -r requirements.txt


По умолчанию установливается база `SQLite` `gencrud_v10` в проект 
	
	python manage.py collectstatic --noinput
	python manage.py makemigrations
	python manage.py migrate

Проект создан! Проверяем `python manage.py runserver`. 
Запускаем локальный сервер и переходим на страницу в `http://localhost:8000/`. 
	

[I]Заполним проект дефолтными данными

	python manage.py createsuperuser
 		name: `superuser`
 		emal: `superuser@mail.ru`
 		password: `superuser888`


Проверяем `python manage.py runserver`.


Создадим базу данных `xxx` и настроем `postgres` для проекта

	sudo apt-get update
	sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib 
	
	# Если нужен `postgis`
	# sudo apt-get install postgis gdal-bin	

	sudo -u postgres psql
	postgres=# 
		CREATE DATABASE homebio;
		CREATE USER homebio WITH PASSWORD 'homebio888';
		ALTER ROLE homebio SET client_encoding TO 'utf8';
		ALTER ROLE homebio SET default_transaction_isolation TO 'read committed';
		ALTER ROLE homebio SET timezone TO 'UTC';
		GRANT ALL PRIVILEGES ON DATABASE homebio TO homebio;
		\q


Меняем настройку подключения к Базе в `~/projects/gencrud_v10/gencrud/gencrud/settings.py`
```
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'homebio',
        'USER': 'homebio',
        'PASSWORD': 'homebio888',
        'HOST': 'localhost',
        'PORT': '',
    }
}
...
```
	
	python manage.py migrate


[I]Заполним проект дефолтными данными
	
	# ... создаем суперпользователя и приминяем фикстуры ...


Проверяем `python manage.py runserver`.

# Если сервер


## GIT / BITBACKET 
	
	cd ~/projects/gencrud_v10

	git config --global user.name "Mihail"
	git config --global user.email gencrudmail@gmail.com
	git config --global core.pager 'less -r'

	git init
	git add *
	git commit -m 'Hello World!'
	

#### TRY/EXCEPT 

1.`Error: That port is already in use.`
	
	fuser -k 8000/tcp 


# ----      ---- #
  --- [pYAr] --- 
# ----      ---- #



