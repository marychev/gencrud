# Данные проекта xxx.ru


[sudo] password for marychev: 

    mmc81086

    ip address
    xx.213.xx.77
    Маска подсети
    255.xxx.255.0 
    Шлюз
    95.xxx.xxx.1


    email:
    xxxx@gmail.com

##### после внесения изменений на сервер выполнить команды

    source /home/xxx/premium37_venv/bin/activate && 
    cd premium37 &&
    python manage.py migrate && 
    python manage.py collectstatic && 
    sudo systemctl restart gunicorn



## DATABASE: POSTGRES

    user:  xxx
    pass: xxxx89898
    
    $ sudo su - postgres 
    $ psql

##### установить все привилегии для пользователя

    grant all privileges on database xxx to xxxx;


##### бэкап базы

    pg_dump -h localhost -U zzz xxx > /0171112.sql
    
##### востановление базы

    psql -h localhost -U premium37 -d premium37 -f /20171112.sql
	
    
### MANAGE.PY: команду выполнять из папки где лежит файл ``manage.py`` "pyar/manage.py"

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py makemigrations thumbnail
    

### fixtures
##### По умолчанию нужно хранить в папке fixtures, которую нужно создать внутри каждого приложения.

    python manage.py dumpdata --format=json myapp > myapp/fixtures/initial_data.json

##### Загрузка фикстуры из файла

    python manage.py loaddata myapp/fixtures/myfix.json

###### "выброшено" исключение IntegrityError.
###### исключить таблицы contenttypes и auth.permissions:

    python manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json


# ... admin panel
    python manage.py createsuperuser ``superuser`` ``superuser888``
    
    [!]sudo fuser -k 8000 / tcp 
    Это должно уничтожить все процессы, связанные с портом 8000.

