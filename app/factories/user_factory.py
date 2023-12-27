# Other libraries
from factory import  Sequence, LazyAttribute
from werkzeug.security import generate_password_hash

# App modules/scripts
from app.models import User, db

# Local scripts
from . import BaseFactory

class UserFactory(BaseFactory):
    class Meta:
        # Take a model User
        model = User

    # Define factory attributes
    username = Sequence(lambda n: f'user{n}')
    email = Sequence(lambda n: f'user{n}@example.com')
    
    @LazyAttribute
    def password(self):
        return generate_password_hash('password')
    
    # @classmethod
    # def generate_user(cls, **kwargs):
    #     return cls.build(**kwargs)
    
    # @classmethod
    # def create(cls, **kwargs):
    #     user = cls._meta.model(**kwargs)
    #     db.session.add(user)
    #     db.session.commit()
    #     return user
    