"""

Program Name: Lab 6 - User Login System

Name: Elijah Drakeford

Purpose: Simulates a user login system using a dictionary to store usernames and passwords 

Date: Feb 20, 2026

"""

# creating dictionary of username and password
users = {
    'guest': 'guest',
    'elijah': 'goodPassword1',
    'adam': 'EasyHack!',
    'johnny': 'Cougars1963!'
}

username = input("Enter username: ")

if username not in users:
    print("User not found. Exiting.")
else:
    password = input("Enter password: ")

