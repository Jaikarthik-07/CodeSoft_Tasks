import random
import string

# Function to generate password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

# Main Program
print("===== PASSWORD GENERATOR =====")

length = int(input("Enter the desired password length: "))

if length <= 0:
    print("Please enter a valid password length.")
else:
    password = generate_password(length)
    print("\nGenerated Password:", password)
