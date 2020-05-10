#### 1. Remove the all migrations files within your project
    cd gencrud/
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete


Drop the current database, or delete the db.sqlite3 if it is your case.

Create the initial migrations and generate the database schema:

    python manage.py makemigrations
    python manage.py migrate


Kill port / reboot
    sudo fuser -k 8000/tcp
    



