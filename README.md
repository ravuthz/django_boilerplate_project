# Django Biolerplate Project

This my prepare django project with some common configure for next project


## How to use

1. Make you have virtualenv or virtualenvwrapper installed
    
   
    Using **virtualenv**
    ```bash
    pip install virtualenv

    # Create virtual env
    virtualenv django_pos_venv

    # Activate on Windows
    django_pos_venv\Scripts\activate

    # Activate on Linux 
    source django_pos_venv/bin/activate
    ```


    Using **virtualenvwrapper**
    ```bash
    pip install virtualenvwrapper

    # Create virtualenv and activate it automatic
    mkvirtualenv django_pos
    ```


    ***NOTE*:** Disable both virtual env about just ```deactivate```



2. Just *clone* and *rename* **boilerplate_project** to **new_project_name**

    ```bash
    git clone https://github.com/ravuthz/django_boilerplate_project.git django_pos

    cd django_pos 

    pip install -r requirements.txt

    cp .env.sample .env

    python manage.py rename boilerplate_project django_pos
    ```

    ***NOTE*:** Configure ***env**iroment* setting from **.env.sample** or create new **.env**
    ```bash
    # Copy from .env.sample
    cp .env.sample .env

    # Create one from command or editor

    echo ENV="staging" >> .env
    echo DEBUG=True >> .env
    echo SECRET_KEY="!@c*ljujxq!xh-6%egnn(*s=dev)89*0xy$z#$cto_z1y279z!" >> .env
    echo DATABASE_URL="postgres://adminz:123123@localhost:5432/django_boilerplate_project" >> .env
    echo INTERNAL_IPS=127.0.0.1 >> .env
    ```

## Let's start to develop

```bash

python manage.py runserver

```