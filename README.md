RUN THE COMMAND IN YOUR COMMAND PROMPT TO SETUP THE DJANGO <br>
STEP 1 : - python -m pip install -U pip <br>
STEP 2 :- python -m venv env_site <br>
STEP 3 :- env_site\Scripts\activate.bat <br>
STEP 4 :- pip install django <br>
STEP 5:- python manage.py runserver <br>

When the project in run on your local server then check all api functionality <br>
GET(METHOD) /users - Returns a list of all users. <br>
GET(METHOD) /users/<id> - Returns the user with the specified ID. <br>
POST(METHOD) /users - Creates a new user with the specified data. <br>
PUT(METHOD) /users/<id>/ - Update the user with specified ID. <br>
DELETE(METHOD) /users/<id> - Deletes the user with the specified ID
