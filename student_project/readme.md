# Note: Python must be installed 

1. First open terminal and activate virtual environment by typing 

  my_venv/scripts/activate

2. Then go to student_project/student_project/settings.py/ and change postgres database credentials you created on postgres setup
`Also Create a database in postgres using pgAdmin server > databases > create your database and add its credentials in  student_project/student_project/settings.py/`

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # PostgreSQL backend
        'NAME': 'student',  # your_database_name
        'USER': 'postgres', # your_database_user
        'PASSWORD': '9876', # your_database_password
        'HOST': 'localhost',  
        'PORT': '5432', # default PostgreSQL port
    }
}

3. Now make migrations by using following commands
   first check you are in your project directory and environment is activated also check image.png  then run following commands
   
   python manage.py makemigrations
   python manage.py migrate

python manage.py runserver  // to run your server then go to URL `http://127.0.0.1:8000/` to check your server funcionality

