# Bank security console

This is an internal repository for employees of "Siyaniye" bank. If you have landed on this repository accidentally, you won't be able to use it as you don't have access to the database. However, feel free to utilize the markup code or take a look at how the database queries are implemented.

The Security console is a website that can be connected to a remote database containing records of visits and employee access cards for our bank.

## How to install

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

`pip install -r requirements.txt`

To set up the environment variables, create a file named .env with the following content

```
DSM_DB_URL='postgres://db_user:db_password@db_host:db_port/db_name'
DSM_DEBUG=True # defult value = False
DSM_ALLOWED_HOSTS=['localhost', '127.0.0.1', 'www.mysite.com'] # defult value = ['localhost', '127.0.0.1']
```

To start the server using Django, run the following command `python manage.py runserver 0.0.0.0:8000`

Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.