from app import app, db, User  # Import the app, db, and User from app.py
from werkzeug.security import generate_password_hash

# Define the users to be added
users = [
    {"username": "Vaibhav", "password": generate_password_hash("password1")},
    {"username": "Rishikesh", "password": generate_password_hash("password2")},
    {"username": "Namandeep", "password": generate_password_hash("password3")},
    {"username": "Agnibha", "password": generate_password_hash("password4")},
]

# Use the application context to interact with the database
with app.app_context():
    for user_data in users:
        user = User(**user_data)
        db.session.add(user)
    db.session.commit()

print("Users added successfully!")
