# This is fork!
# Actual version Gencrud https://github.com/gencrud/gencrud

## Gen[crud] - free software for creating web projects. (varsion 0)

Gencrud is the platform for creating simple sites, corporate sites, internet-shop, or blogs. 
The platform is easy to expand and customize, which will create a project of any complexity.


## Install and run project

1. [Downolad](https://github.com/marychev/gencrud) or [clone](https://github.com/marychev/gencrud.git) a repo **gencrud**.

2. Open a console into the root `gencrud` and type `ll`. You must see the next structure folders and files:
```
gencrud/
.git/
.gitignore
README.md
```

3. Next, we will install and run the project. This script will install a virtual environment, set a DB (SQLite by default), add a default theme.
```
$ . gencrud/gencrud/sh/init.sh
```

**Congretulations!** Open browser - [localhost:8000](http://localhost:8000)
The welcome page should displays. 
Next, you need to fill **general settings** to see the Home page with your content. 
This should take about a minute!


### Structure project (after install)
+ **app/** - 	frontend folder (css, js, images, ...)
+ **gencrud/** - backand folder / core
+ **theme/** - 	theme folder (html, media, ...)
+ **venv/**-  	virtual environment folder
+ README.md
+ .gitignore


### Useful comands:
> All next commands run from the root `project_name$` folder. 
Go to the root `project_name$` folder.

**Create a supers user:**
```
$ python gencrud/manage.py createsuperuser
```

**Run project:**
```
$ python gencrud/manage.py runserver
```
**Run tests:**
```
$ python gencrud/manage.py test
```
**Installing a new theme / The first install:**
```
. gencrud/gencrud/sh/init.sh
```


##### Techologies
* Python 3.6
* Django 2.2
* Postgres, MySQL, SQLite
* Bootstrap 4

