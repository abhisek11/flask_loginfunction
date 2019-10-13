# flask_loginfunction
This is boilerplate application for flask login logout function,
The Base code for login and signup is done with very simple and sofisticated manner ,
so that Developer can use it for the development of their products and projects

We've done it! We have used Flask-Login and Flask-SQLAlchemy to build a very basic login system for our app. We covered how to authenticate a user by first creating a user model and storing the user information to later. Then we had to verify the user's password was correct by hashing the password from the form and comparing it to the one stored in the database. Finally, we added authorization to our app by using the @login_required decotor on a profile page so only logged in users can see that page.

## Features

- [x] User account sign up, sign in, password reset, all through asynchronous email confirmation.
- [x] Form generation.
- [x] Error handling.
- [x] HTML macros and layout file.
- [x] "Functional" file structure.
- [x] Python 3.x compliant.
- [] Administration panel.
- [x] Logging.
- [ ] Stripe subscriptions. (WIP)
- [ ] RESTful API for payments.
- [ ] Simple RESTful API to communicate with your app.


## Libraries

### Backend

- [Flask](http://flask.pocoo.org/), obviously.
- [Flask-Login](https://flask-login.readthedocs.org/en/latest/) for the user accounts.
- [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/) interacting with the database.
- [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/) and [WTForms](https://wtforms.readthedocs.org/en/latest/) for the form handling.
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/) for sending mails.
- [itsdangerous](http://pythonhosted.org/itsdangerous/) for generating random tokens for the confirmation emails.
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.org/en/latest/) for generating secret user passwords.
- [Flask-Admin](https://flask-admin.readthedocs.org/en/latest/) for building an administration interface.
- [Flask-Script](https://flask-script.readthedocs.io/en/latest/) for managing the app.
- [structlog](http://structlog.readthedocs.io/en/stable/) for logging.
- [Flask-DebugToolBar](https://flask-debugtoolbar.readthedocs.io/en/latest/) for adding a performance toolbar in development.
- [gunicorn](http://gunicorn.org/) for acting as a reverse-proxy for Nginx.
- [Flask-Stripe](http://stripe.com/) for subscription billing.
