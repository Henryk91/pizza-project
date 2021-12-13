# Pizza Project 

This is a python django serverside app to integrate with Trello boards. (https://trello.com/)<br> With this project you will be able to view your boards, lists, cards and create cards on a Trello list.

A running example of this project: https://trello-pizza-project.herokuapp.com <br><br>
NB: This project is not intended to be used in production 
<hr>
<br>

## Setup:

### Setting up the project

1. Make sure you have python 3 or later
2. Make sure you have virtualenv (python3 -m pip install --user virtualenv)
3. CD into project directory
3. run: python3 -m venv env 
4. run: source env/bin/activate
5. run: pip install -r requirements.txt

### Setting up Trello
- Create a Trello account if you don't have one
- Manually create 2 lists eg: To Do and Done
### Setup and Add your Trello Key and Token
- To use this project you need a Trello key and Token that can be created here: https://trello.com/app-key
- You also need to add 'Allowed Origins' urls where you are going to test and deploy to 
- In the root directory of this project create a file called .env
- Add your trello 'KEY' to TRELLO_KEY in the .env file eg: TRELLO_KEY='sdkmmosvmoes'
- Add your trello 'Token' to TRELLO_TOKEN in the .env file eg: TRELLO_TOKEN='sdkmmosvmoes'

### Run the project
1. python manage.py migrate
2. python manage.py runserver
- Default url is http://127.0.0.1:8000/

<hr>
<br>
## Usefull Commands
<br>

### Run Server
- python manage.py runserver
### To add Admin creds to your project
- python manage.py createsuperuser

### To Run the tests 
- python manage.py test board

### Create migration code
- python manage.py makemigrations board

### See new migration sql code
- python manage.py sqlmigrate < migragion name >
### Initial db or run migration scripts
- python manage.py migrate

### If you added new packages
- pip freeze > requirements.txt
### Find admin templates:
- python -c "import django; print(django.__path__)"

### Note:
- To host remember to add url to ALLOWED_HOSTS in listproject/settinggs.py