# Events proj

## Steps of installing and launching

1. clone repo using:
    `git clone https://github.com/lyf2000/events.git`
1. Create `.env` file at `backend/core` dir and add these variables(according to your data):
    ```
    # .env file at backend/core directory
    
    # Gmail credits to send email (also u need to allow email sending)
    EMAIL = <email> # 
    PASSWORD = <password>
    # Postgres DB
    DB_NAME = <db_name>
    DB_USER = <db_user>
    DB_PASSWORD = <db_password>
    ``` 
1. Run redis server (default port and host are specified already)
1. Install all libs for python using(at `/backend/` dir):
    `pip install -r requirements.txt`
1. Run celery via command(at `/backend/` dir):
    `celery -A core worker -l info --pool=solo`
1. Run django server(at `/backend/` dir):
   ```python
   python manage.py migrate
   python manage.py runserver
   ```
1. Install node.js and vue.cli
1. At `/frontend/` run:
   ```
   npm install
   npm run serve
   ```
1. Move by url that Vue opened