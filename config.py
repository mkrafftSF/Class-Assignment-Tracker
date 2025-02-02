"""
This file configures the Flask app and sets up the database connection.
"""
# The URI for connecting to the SQLite database
DATABASE_URI = "sqlite:///assignments.db"

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)
