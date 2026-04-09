import random
import string

def generate_unique_email(first_name="test", last_name="testov", cohort="5"):
    random_digits = ''.join(random.choices(string.digits, k=3))
    email = f"{first_name}_{last_name}_{cohort}_{random_digits}@yandex.ru"
    return email

def generate_password(min_length=6):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=min_length))
    return password

def generate_short_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=5))
    return password

def generate_name():
    name = ''.join(random.choices(string.ascii_letters, k=6))
    return name