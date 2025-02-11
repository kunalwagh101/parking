

# STEPS TO RUN THE APPLICATION

# Clone the repository

    git clone https://github.com/e9kwagh/Everest.git

# Create a virtual environment

**For Linux and macOS**

    python3.8 -m venv venv
    source venv/bin/activate

**For Windows**

    pip install virtualenv
    python -m venv venv
    virtualenv venv
    venv/Scripts/activate


# Install the necessary modules

    pip install -r requirements.txt

**If it shows error, run**

    pip install django

# Run the application

**generate dummy data using below command**
```
   python manage.py dummy_data 10 

```

**run server using below command**
```
    python manage.py runserver

```

# Open the below url on your browser

     http://127.0.0.1:8000/


# You can also test the app using the test command 
    python manage.py makemigration
    python manage.py migrate

**run this command to test the app**
```
     python manage.py test polls
```
    