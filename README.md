## **To start the app**

- Cd into the root directory. 
- Run ***pip install -r requirements.txt*** to install all requirements.
- Run ***python manage.py runserver*** to start up the Django web server, and visit the website in your browser.

You can register as usual user or log into superuser via  
email - *superuser@superuser.com*  
password - *superuser*  
and go to http://127.0.0.1:8000/admin/ to see django admin interface.

---
## **To change database**

- In your terminal, cd into the commerce directory. 
- Run ***python manage.py makemigrations finance_tracker*** to make migrations for the finance tracker app.
- Run ***python manage.py migrate*** to apply migrations to your database.