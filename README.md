# flask_login_function (FLASK WebApp) 
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

-Use the Flask-Login library for session management
-Use the built-in Flask utility for hashing passwords
-Add protected pages to our app for logged in users only
-Use Flask-SQLAlchemy to create a user model
-Create sign up and login forms for our users to create accounts and login
-Flash error messages back to users when something goes wrong
-Use information from the user's account to display on the profile page
