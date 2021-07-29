# Send Mail Demo
 
 _This project demonstrate how to send email from django._
 

##### Installation steps:

1. Clone the repository

2. Create virtual enviornment

> virtualenv -p python3.6 venv_mail_demo
> .venv_mail_demo/bin/activate

3. Install dependencies/packages:

> pip install -r requirements.txt

4. Make migrations:
>  cd contact_email/
>
>  python manage.py migrate

5. Create superuser:
> python manage.py createsuperuser

6. Run the following command:
  _Note: Make sure you are inside the contact_email directory_
>  python manage.py runserver

