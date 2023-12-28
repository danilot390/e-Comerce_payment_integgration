# Other libraries
from faker import Faker
from factory import Factory, Faker as FakerFactory

# Initialize Faker with a specific seed for reproducibility
fake = Faker
FakerFactory.select_factory = fake

# Create a base factory class 
class BaseFactory(Factory):
    class Meta:
        abstract = True

from .user_factory import UserFactory