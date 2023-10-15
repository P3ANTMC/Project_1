"""
text_analyzer.py: First Engeto Online Academy project

author: Petr Hrankay
email: pean.tmc@seznam.cz
discord: PETR H.
"""




users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }


line = "-" * 40

username = input("username: ".capitalize())
password = input("password: ".capitalize())
print(line)

if username in users.keys() and password in users.values():
    print(f"Welcome to the app, {username}")
    print