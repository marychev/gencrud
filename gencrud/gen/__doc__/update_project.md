ssh -p 888 marychev@95.213.236.77

[pjkmlfuthlf]

### SERVER

    cd /home/homebio/
    . venv/bin/activate
    pg_dump -h localhost -U homebio homebio > theme/17042020_2.sql  
    # homebio888
    
    git add .
    git commit -m "ser: auto commit 17042020 22:48"
    git pull origin master  # mmc_81086

Chechkout **git**! 

    
    cd gencrud
    pip install -r requirements.txt
    python manage.py collectstatic --noinput
    python manage.py migrate
    
    sudo supervisorctl restart homebio

Permmissions:

    sudo chmod -R 755 /home/homebio/
    sudo chmod -R 777 /home/homebio/theme/
    
    sudo chmod -R 777 /home/homebio/gencrud/blog/fixtures/
    sudo chmod -R 777 /home/homebio/gencrud/home/fixtures/
    sudo chmod -R 777 /home/homebio/gencrud/catalog/fixtures/
    sudo chmod -R 777 /home/homebio/gencrud/menu/fixtures/
    sudo chmod -R 777 /home/homebio/gencrud/page/fixtures/
    sudo chmod -R 777 /home/homebio/gencrud/settings_template/


```
sudo ln -s /etc/nginx/sites-available/homebio /etc/nginx/sites-enabled/
sudo chown -R $USER:$USER /home/homebio
sudo chmod -R 755 /home/homebio/

# /etc/init.d/nginx restart
sudo service nginx restart
```


### local machine MMC
```
sudo -u postgres psql

postgres=# drop database homebio;
postgres=# create database homebio;
postgres=# \q;

# psql -h localhost -U homebio -d homebio (-p 5433) -f /home/mmc/project/4teker/theme/xxxxxxxx.sql   
psql -h localhost -U homebio -d homebio -f /home/mmc/project/homebio/theme/00.sql

# Download a file from server  
scp -P 888 marychev@95.213.236.77:/home/homebio/theme/04022020.sql /home/mmc/project/homebio/theme/
```



### auth
server: pjkmlfuthlf
bitbacket: PjkmlfUthlf81086

