# Democrance

Democrance Customer and Insurance API's

######################### Docker based instalation ########################################

Install Docker Desktop in system

Docker Desktop (https://www.docker.com/products/docker-desktop)

After installing the software, open terminal and verify the docker installation by using below command.

---->>>>>> docker run hello-world

Clone the repository:

$ git clone https://github.com/akashgusain/Democrance.git

$ cd Democrance

Run below command after installing docker in your system

docker build -t django_web:latest .

docker run -it -p 8000:8000 django_web:latest

http://127.0.0.1:8000/api/swagger/ ----------- Swagger UI (API Documentation)

Create Super User by accesing Docker container command below

Open Terminal --

docker ps

docker exec -it ContainerID /bin/sh

Create a superuser:

python3 manage.py createsuperuser and follow instructions on screen to add your credentials

after completion you can exit or explore the container more as per your needs

Admin Dashboard Login - http://127.0.0.1:8000/admin/login/?next=/admin/

For Accessing and creating customer

http://127.0.0.1:8000/api/v1/create_customer/

For Accessing and creating policy

http://127.0.0.1:8000/api/v1/create_policy/

################################ Virtual Environment based installation ####################################################

Download Python from official website https://www.python.org/downloads/

Create a virtual environment to install dependencies in and activate it:

Virtual Env installation

https://virtualenv.pypa.io/en/latest/installation.html

$ virtualenv venv

$ source env/bin/activate

Then install the dependencies:

(env)$ pip install -r requirements.txt

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Once pip has finished downloading the dependencies:

(env)$ cd Democrance (you have to be inside Democrance main folder where manage.py file is there )

(env)python3 manage.py makemigrations 
(env)python3 manage.py migrate

Create a superuser:

python3 manage.py createsuperuser and follow instructions on screen to add your credentials

(env)$ python manage.py runserver

And navigate to http://127.0.0.1:8000/api/swagger/

check all api listed in the Swagger UI

login for accesing logged in user API's (Djano Rest api are Browsable API - https://www.django-rest-framework.org/topics/browsable-api/#the-browsable-api)

http://127.0.0.1:8000/admin/login/?next=/admin/

For Accessing and creating customer

http://127.0.0.1:8000/api/v1/create_customer/

For Accessing and creating policy

http://127.0.0.1:8000/api/v1/create_policy/

