# flask_login_function (FLASK WebApp) 
This is boilerplate application for flask login logout function,
The Base code for login and signup is done with very simple and sofisticated manner ,
so that Developer can use it for the development of their products and projects


I have used Flask-Login and Flask-SQLAlchemy to build a very basic login system for our app. We covered how to authenticate a user by first creating a user model and storing the user information to later. Then we had to verify the user's password was correct by hashing the password from the form and comparing it to the one stored in the database. Finally, we added authorization to our app by using the @login_required decotor on a profile page so only logged in users can see that page.

congrats We've done it! #Happy python coding .

## Features

- [x] User account sign up, sign in, password reset, all through asynchronous email confirmation.
- [x] Form generation.
- [x] Error handling.
- [x] HTML macros and layout file.
- [x] "Functional" file structure.
- [x] Python 3.x compliant.
- [x] Logging.
- [ ] Stripe subscriptions. (WIP)
- [ ] RESTful API for payments.
- [ ] Simple RESTful API to communicate with your app.


## Libraries
There are three main packages we need for our project:

-Flask.

-Flask-Login - to handle the user sessions after authentication.

-Flask-SQLAlchemy - to represent the user model and interface with our database.

## How to run 

for ubuntu user "export"  and for windows use "set":- 

-/user/flask_loginfunction$virtualenv -p python env

-/user/flask_loginfunction$pip install -r requirements.txt

-/user/flask_loginfunction$export FLASK_APP=flask_project.

-/user/flask_loginfunction$export FLASK_DEBUG=1.

-/user/flask_loginfunction$python

Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.

">>> from flask_project import db,create_app"

">>> db.create_all(app=create_app())"

-/user/flask_loginfunction$flask run

### Backend

-Use the Flask-Login library for session management.

-Use the built-in Flask utility for hashing passwords.

-Add protected pages to our app for logged in users only.

-Use Flask-SQLAlchemy to create a user model.

-Create sign up and login forms for our users to create accounts and login.

-Flash error messages back to users when something goes wrong.

-Use information from the user's account to display on the profile page.

for any kind of bug please open a PR or raise a issue thanks .
please feel free to use it , if anyone like to extend its features please feel free to mail me 
Abhisek singh .
@email :- raizadaabhi11@gmail.com.
