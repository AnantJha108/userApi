RUN THE COMMAND IN YOUR COMMAND PROMPT TO SETUP THE DJANGO
STEP 1 : - python -m pip install -U pip
STEP 2 :- python -m venv env_site
STEP 3 :- env_site\Scripts\activate.bat
STEP 4 :- pip install django
STEP 5:- python manage.py runserver

When the project in run on your local server then check all api functionality
GET(METHOD) /users - Returns a list of all users.
GET(METHOD) /users/<id> - Returns the user with the specified ID.
POST(METHOD) /users - Creates a new user with the specified data.
PUT(METHOD) /users/<id>/ - Update the user with specified ID.
DELETE(METHOD) /users/<id> - Deletes the user with the specified ID
