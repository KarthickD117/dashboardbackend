# Prerequisite
python, postgresql

# Install required packages
Install the required packages by: **pip install django djangorestframework djangorestframework-simplejwt django-cors-headers psycopg2**

# Changes required to do in settings.py
In database object change the name to postgresql database name and change the password to the database.

# Migrate the data base model to backend 
To migrate all the model to database first run the command py manage.py makemigrations, then run the command py manage.py migrate. 
The above commands will migrate all the model to the database.

## To run 
To run backend run the command py manage.py runserver (it will run in localhost), run the command py manage.py runsever 0.0.0.0:8000 to run in any host.
