import string
import secrets

def generate_passwords():
    """Generate a specified number of random passwords with a specified length"""
    
    # Prompt the user for the desired number of passwords to generate
    num_passwords = int(input("Enter the desired number of passwords to generate: "))
    
    # Prompt the user for the desired password length
    length = int(input("Enter the desired password length: "))
    
    # Define the possible characters to use in the password
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Use secrets.choice() to select characters randomly
    passwords = []
    for i in range(num_passwords):
        password = ''.join(secrets.choice(chars) for j in range(length))
        passwords.append(password)
    
    return passwords

passwords = generate_passwords()
print('\n'.join(passwords))
