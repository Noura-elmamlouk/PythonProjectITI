import re
import json

#In the register_user function, the parameter users is used to represent the list of existing users. Here's the function definition
def register_user(users):
    print("Register:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    # Ensure a valid email is entered
    while True:
        email = input("Email: ")
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(email_regex, email):
            break
        else:
            print("Invalid email format. Please enter a valid email.")

    # Ensure a valid phone number is entered
    while True:
        mobile = input("Mobile Phone: ")
        phone_regex = r'^01[0-2]\d{8}$'
        if re.match(phone_regex, mobile):
            break
        else:
            print("Invalid mobile number. Please enter a valid Egyptian phone number.")

    password = input("Password: ")
    confirm_password = input("Confirm Password: ")

    if password != confirm_password:
        print("Passwords do not match.")
        return None
    #the next() function to find the first occurrence of a user in the users
    # list whose email matches the input email
    existing_user = next((user for user in users if user.get('email') == email), None)
    if existing_user:
        print("Email already exists. Please choose a different email.")
        return None

    user = {'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password, 'mobile': mobile}
    users.append(user)
    save_data(users)
    print("Registration successful.")
    return user

def login(users):
        print("Login:")
        email = input("Email: ")
        password = input("Password: ")

        for user in users:
            if user['email'] == email and user['password'] == password:
                print(f"Welcome, {user['first_name']} {user['last_name']}!")
                return user
        print("Invalid email or password.")
        return None

def save_data(users):
    try:
        with open('users.json', 'w') as file:
            json.dump(users, file, indent=2)
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data():
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
            return users
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON. File may be empty.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []