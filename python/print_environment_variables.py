import os

# Comment out these two lines if you don't want to use the .env file
from dotenv import load_dotenv
load_dotenv()

environment_variable1 = os.getenv('DOG')
environment_variable2 = os.getenv('CAT')
print(environment_variable1)
print(environment_variable2)
