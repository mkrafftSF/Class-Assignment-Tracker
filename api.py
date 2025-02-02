# API integration for assignment data set up. Closes #15.
"""
This file contains Flask API endpoints for managing assignment and deadline tracking.
"""
from flask import Flask, jsonify
from models import Assignment, db  # Ensure models.py defines your Assignment model and db instance
from schemas import AssignmentSchema  # Ensure schemas.py defines AssignmentSchema

# Create the Flask application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///assignment_data.db"
# Initialize the database with the Flask app
db.init_app(app)

# Create an instance of the schema for serializing assignments
assignment_schema = AssignmentSchema(many=True)

@app.route("/assignments", methods=["GET"])
def get_assignments():
    """
    Fetches all assignments from the database.
    Returns:
        JSON: A list of all assignments.
    """
    # Dummy data for testing purposes
    assignments = [
        {"name": "Assignment 1", "due_date": "2025-02-10", "status": "pending"},
        {"name": "Assignment 2", "due_date": "2025-02-15", "status": "completed"}
    ]
    # Uncomment the following lines to use the database query once the database is set up:
    # assignments = Assignment.query.all()
    # return jsonify(assignment_schema.dump(assignments))
    return jsonify(assignments)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

