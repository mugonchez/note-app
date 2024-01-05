# Note-App
A RESTful API that allows users to create, read, update, and delete notes. The application also allow users to share their notes with other users and search for notes based on keywords.

## Application Framework and Database
The backbone of my application is built upon Django Rest Framework with a robust PostgreSQL database. This powerful combination ensures data integrity, scalability, and performance.

## Authentication with JWT
Security is paramount. My system employs JWT (JSON Web Token) authentication, offering a secure and efficient method to authorize users, ensuring that only authenticated users access my system's resources.

## Rate Limit and Throttling for Enhanced Control
To maintain optimal performance and prevent abuse, I've implemented a rate limit and throttling mechanism. Authenticated users can make up to 40 requests per minute, while non-authenticated users are limited to 20 requests per minute. These values are customizable, allowing fine-tuning as per application requirements, all managed conveniently within the settings file.

This setup not only guarantees security but also ensures a smooth, controlled flow of requests to maximize efficiency without compromising on user experience or system stability.

## API Endpoints
### Authentication Endpoints

POST /api/auth/signup: create a new user account.

POST /api/auth/login: log in to an existing user account and receive an access token.

### Note Endpoints

GET /api/notes: get a list of all notes for the authenticated user.

GET /api/notes/ get a note by ID for the authenticated user.

POST /api/notes: create a new note for the authenticated user.

PUT /api/notes/ update an existing note by ID for the authenticated user.

DELETE /api/notes/ delete a note by ID for the authenticated user.

POST /api/notes/:id/share/:user_id: share a note with another user for the authenticated user.

GET /api/search?q=:query: search for notes based on keywords for the authenticated user

## How to install and run it locally

### Download
To download/clone the this app, move to your desired directory where to want to put the app and run the following commands.
Note: Make sure you have git installed. You can install git with the following commands.

Ubuntu::

    sudo apt update
    sudo apt install git

CentOS/Fedora/RedHat::

    sudo yum update
    sudo yum install git

OSX::

    brew install git

Download/Clone the App inside the directory of your choice.

To download/clone the app::

    git clone https://github.com/moses-mugoya/Note-App.git

Install system required modules such as python, pip and postgresql::

    sudo apt install python3.10

    sudo apt install python3.10-pip python3.10-dev libpq-dev postgresql postgresql-contrib file
    
Before installing the required packages, it is recommended to create a virtual envirinment. The virtual environment for python 3.10 is created as follows.

    Install virtual environment for python 3.10 if you have not

    Install install virtualenv using pip3::

    sudo pip3 install virtualenv
    
Now move to the root directory of the downloaded project at create a virtual environment with your desired name. For instance::

    virtualenv --python=python3.10 venv
    
Active your virtual environment::

    source .venv/bin/activate

To install all the required packages, run the command in the root project folder::

    pip3 install -r requirements.txt
    
### Create database for Note App to use.

Create a database note_db::

    $ sudo -u postgres psql
    # CREATE DATABASE note_db;

Create a user for the Database and grant them privileges::

    # CREATE USER note_user WITH PASSWORD 'n0t3p@ss';
    # ALTER ROLE note_user SET client_encoding TO 'utf8';
    # ALTER ROLE note_user SET default_transaction_isolation TO 'read committed';
    # ALTER ROLE note_user SET timezone TO 'UTC+3';
    # GRANT ALL PRIVILEGES ON DATABASE note_db TO note_user;
    # ALTER USER note_user CREATEDB;

You can use different names for the user and database but be sure to change the same in the application settings file database section

## Basic Commands

### Database Migrations

    $ python3 manage.py migrate

### Run the Tests
    $ python3 manage.py test

    
### Create Superuser
    $ python3 manage.py createsuperuser

### Run the development server
    $ python3 manage.py runserver

This will open the development server on http://localhost:8000






