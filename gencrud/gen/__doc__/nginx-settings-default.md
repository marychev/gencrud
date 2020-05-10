# Установка проекта на новый сервер

    sudo apt-get update
    sudo apt-get -y upgrade 
    sudo apt-get install -y python3-pip

There are a few more packages and development tools to install to ensure that we have 
a robust set-up for our programming environment: 
    
    sudo apt-get install build-essential libssl-dev libffi-dev python-dev
    git clone ***


дальше все как в README.md


Поддомен / Значение 
---------------------
homebio.ru / 95.213.236.77


Полность переносим / клонируем весь проект на сервак с правильными параметрами.



NGINX
------------
    sudo nano /etc/nginx/sites-available/homebio


```
server {
    server_name	www.homebio.ru;
    return 301 http://homebio.ru$request_uri;

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/www.homebio.ru/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.homebio.ru/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}

server {
    server_name homebio.ru;
    charset     utf-8;

    access_log  /home/homebio/logs/nginx-access.log;
    error_log   /home/homebio/logs/nginx-error.log;

    client_max_body_size 88850M;

    # обслуживание медиа файлов и статики
    location /media/  {
        root /home/homebio/theme;
    }

    location /static/ {
        root /home/homebio/theme;

        expires 30d;

        gzip             on;
        gzip_min_length  1000;
        gzip_types       text/plain application/xml application/x-javascript application/javascript text/css text/json;
        gzip_comp_level  6;

        access_log off;
    }

    location / {
        proxy_pass http://127.0.0.1:1920/;
        proxy_set_header Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_send_timeout 350s;
        proxy_read_timeout 350s;
    }
}

server {
    if ($host = www.homebio.ru) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen	80;
    server_name	www.homebio.ru;
    return 404; # managed by Certbot
}
```
    
    
    sudo ln -s /etc/nginx/sites-available/homebio /etc/nginx/sites-enabled/
    
    sudo chown -R $USER:$USER /home/homebio
    sudo chmod -R 755 /home/homebio/
    sudo chmod -R 777 /home/homebio/gencrud/gencrud_v10.sqlite3 



Supervisor configuration
Create a supervisor configuration file: (Warning: Please note the .conf extension)
--------------------------------------------------------------------------------
sudo nano /etc/supervisor/conf.d/homebio.conf

[program:homebio]
command=/home/homebio/venv/bin/gunicorn gencrud.wsgi:application -c /home/homebio/gencrud/gencrud/gunicorn.conf.py
directory=/home/homebio/gencrud
user=nobody
autorestart=true
redirect_stderr=true



sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start homebio

Ждем когда встанут ДНС!!!