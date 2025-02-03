# Placeholder for unit/integration tests for Assignment Table components. Closes #17.



"""
This file contains SQLAlchemy models for the Assignment Tracker.
"""
class Assignment(db.Model):
    """
    Represents an assignment in the database.
    Attributes:
        id (int): Unique identifier for the assignment.
        name (str): Name of the assignment.
        due_date (datetime): Deadline for the assignment.
        status (str): Status of the assignment (e.g., 'pending' or 'completed').
    """
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(100), nullable=False)  # Assignment name
    due_date = db.Column(db.DateTime, nullable=False)  # Due date
    status = db.Column(db.String(50), nullable=False)  # Task status
