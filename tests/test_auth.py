# Flask extensions
from flask import url_for
from flask_login import current_user

# App modules
from app.models import User
from app.factories import UserFactory

# Local scripts
from  .base import BaseTestCase


class AuthTestCase(BaseTestCase):
    
    def test_render_register_page(self):
        # Test render template auth/signup
        response = self.client.get(url_for('auth.signup_get'))
        self.assert200(response)
        self.assert_template_used('auth/signup.html')
    
    def test_register_new_user(self):
        
        # Create a new user
        new_user = UserFactory()
        post_new_user = {'username': new_user.username, 'email':new_user.email, 'password':'password'}

        # Create a client
        client = self.client
        print(post_new_user)
        response = client.post(
            url_for('auth.signup_post'),
            data = post_new_user,
            follow_redirects = True,
        )

        self.assert200(response)
        self.assertRedirects(response, url_for('home'))

        print(new_user)


    def test_render_login_page(self):
        # Test render template auth/login.html
        response = self.client.get(url_for('auth.login_get'))
        self.assert200(response)
        self.assert_template_used('auth/login.html')

    # def test_login_with_valid_credentiales(self):
    #     # Create a test user
    #     user = UserFactory()
    #     #self.assertTrue(user.check_password('password')) # Cosidering 'password' is the user's password 
    #     print('--------------------$$$$$$$$$$$$$$>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    #     print(user.username)

    #     # Create Self client
    #     client = self.client

        # Test logging in with valid credentials
        # response = client.post(
        #     url_for('auth.login_post'),
        #     data={'username': user.username, 'email': user.email, 'password': 'password'},
        #     follow_redirects = True
        # )
        # # Testing
        # #self.assertTrue(current_user.is_authenticated)
        # self.assert_message_flashed('Login successful!')
        # #self.assert_redirects(response, url_for('home'))