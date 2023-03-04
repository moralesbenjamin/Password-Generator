import string
import secrets

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            break
    return password

if __name__ == '__main__':
    password = generate_password()
    print(f"Your new password is: {password}")
This password generator creates a string of characters consisting of lowercase letters, uppercase letters, digits, and punctuation marks. It then checks if the generated password contains at least one lowercase letter, at least one uppercase letter, at least one digit, and at least one punctuation mark. If the generated password meets all of these criteria, it is returned as the result. If not, the process repeats until a suitable password is generated. The default length of the password is 12 characters, but you can specify a different length by passing a parameter to the generate_password function.




benji m
Build a python password generator without using the secrets module

Sure, here's an example of a password generator in Python that doesn't use the secrets module:

python
Copy code
import random
import string

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            break
    return password

if __name__ == '__main__':
    password = generate_password()
    print(f"Your new password is: {password}")
