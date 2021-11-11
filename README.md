# polls-api

installation

for installation you need to install postgre sql database

1) create a virtual enviroment

virtualenv env

2) activate 

source env/bin/activate

3) installing packages

pip install django==2.2.10 psycopg2-binary==2.8.6 djangorestframework

4) create project

django-admin startproject poles

5) copied directories 'poles' and 'poles_app' in project

6) make migrations and create superuser

python manage.py migrate

python manage.py createsuperuser

#api for poll system


administration
http://localhost:8000/admin

#for user


get active polls
http://localhost:8000/api/v1.0/polls/

get user answer
http://localhost:8000/api/v1.0/answers/[user_id]/

post a reply of user
http://localhost:8000/api/v1.0/reply/

Method POST

{
"poll":[poll_id],

"question":[question_id],

"variant":[variant_choice],

"user_id":[user_id or default]
}
