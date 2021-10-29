# Django Biolerplate Project

This my prepare django project with some common configure for next project


## How to use

Just *clone* and *rename* **biolerplate_project** to **new_project_name**

```bash

git clone https://github.com/ravuthz/django_boilerplate_project.git django_pos

cd django_pos && python manage.py rename biolerplate_project django_pos

```

Configure ***env**iroment* setting from **.env.sample** or create new **.env**
```bash
# Copy from .env.sample
cp .env.sample .env

# Create one from command or ide

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