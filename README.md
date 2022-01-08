
1.Project's Title


Web application for greeting the user and checking the duplicate name in the database.


2.Project Description


The application accepts a request from the user and saves his name and email, and also checks the name whether it has been repeated before or not. Django The session starts when a new name is created and continues until a new name is created anew, which allows you to track the state of the client and add new functionality.


3.How to Install and Run the Project


To start our project in local server:

need make clone repo from git  https://github.com/MoriartyJam/setup

pip install virtualenv

virtualenv venv -p python3.8

source venv/bin/activate

pip install -U -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver



To start project from Docker:

docker-compose build

docker-compose up


4.How to Use the Project


On the start page, enter your email name in the form and click the Submit button. After that we can see your greeting and your email. In the upper right corner there is also a greeting and the name of your session, you can also see a list of names. By clicking on the logo in the upper left corner , you are taken to the start page.
