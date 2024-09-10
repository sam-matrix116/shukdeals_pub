# Introduction

* This is the backend code for ShukTV. It has APIs and the admin.
* The project uses Django as the dev framework and MySQL(5.7.x+)/MariaDB(10.x.x+) as the database.

## Installation Instruction
* Create a virtual environment with Python 3.8 or higher version, activate it. You can ignore it if you want to install the project on system level.
* Go to project root and follow the following steps:
    * run `pip install -r requirements.txt`
    * Copy `.env_example` to `.env` and configure the values based on your computer setup
    * Create a `log` folder and `info.log` in this directory
    * Run `python manage.py migrate`
    * Run `python manage.py createsuperuser` to create the admin user
    * Run `python manage.py runserver` to run the server on your machine
    * Create a `media` folder to store user uploaded files
* The last step is to import sql files from the `sqlfiles`. Just ensure to import plans.sql before plan_features.sql

## Usage
Once the project is running successfully on your computer, you can access the admin panel at http://127.0.0.1:8000/account/login/

Copy the default images at-

/static/dist/img/def_imgs/default_cover_pic.png
/static/dist/img/def_imgs/profile_pic.jpeg

TO

media/default_images/