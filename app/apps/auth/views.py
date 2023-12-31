# Flask extensions
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

# App modules
from app.models.auth import User

# Local scripts
from app.forms import LoginForm, RegistrationForm
from . import auth

@auth.route('/signup')
def signup_get():
    # If the user is alreaafy authenticated, redirect to the main.home page 
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    # Create a Register Form
    register_form = RegistrationForm()

    # Prepare the context for rendering the registration page
    context = {
        'register_form': register_form,
    }

    # Render the Registration page with Register form
    return render_template('auth/signup.html', **context)

@auth.route('/signup', methods=['POST'])
def signup_post():
    # Create a Register form
    register_form = RegistrationForm()

    # Check if the form is correct
    if register_form.validate_on_submit():
        # Create a instance to new user
        new_user = User(username =register_form.username.data,
                        email=register_form.email.data,
                        password=register_form.password.data)
        # Check if the username and email are unique
        existing_user_username = User.get_by_username(username=register_form.username.data)
        existing_user_email = User.get_by_email(email=register_form.email.data)

        if existing_user_username:
            flash('Username already taken. Please choose another.','danger')
        elif existing_user_email:
            flash('Email adddress already registered. Please use another.','danger')
        else:
            # Create a new user
            new_user.save()
            
            # Login with new user
            login_user(new_user)

            # Message of congratulations
            flash('Congratulations, you are now registered user!')
            # Redirect to main.home
            return redirect(url_for('main.home'))
    
    # Prepare the context for rendering Register page
    context = {
        'register_form': register_form,
    }

    # Render Register page with a Register form
    return render_template('auth/signup.html', **context)

@auth.route('/login', methods=['GET'])
def login_get():
    # If the user is alreaafy authenticated, redirect to the main.home page 
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    # Create a login form
    login_form = LoginForm()
    # Prepare context for rendering the login page
    context = {
        'login_form': login_form,
    }

    # Render the login page with the login form
    return render_template('auth/login.html', **context)

@auth.route('/login', methods=['POST'])
def login_post():
    # If the user is alreaafy authenticated, redirect to the main.home page 
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    # Create a login form
    login_form = LoginForm()

    # Validate the login form on submission
    if login_form.validate_on_submit():
        # Query the database for the user based on the provided username
        user = User.query.filter_by(username = login_form.username.data).first()

        # Check if the user exists and the passwrod is correct
        if user and user.check_password(login_form.password.data):
            # Login in the user
            login_user(user)
            flash('Login successful!')
            return redirect(url_for('main.home'))
        else:
            # Flash an error message if login fails
            flash('Login failed. Check your username & password')

    # Prepare context for rendering the login page with the login form
    context = {
        'login_form': login_form,
    }

    # Render the login page with the login form
    return render_template('auth/login.html', **context)

@auth.route('/logout')
@login_required
def logout():
    # Logout the user
    logout_user()

    # Redirect on the url Index
    return redirect(url_for('auth.login_get')) 