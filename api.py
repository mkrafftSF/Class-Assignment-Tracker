# API integration for assignment data set up. Closes #15.

"""
This file contains Flask API endpoints for managing assignment and deadline tracking.
"""
@app.route('/assignments', methods=['GET'])
def get_assignments():
    """
    Fetches all assignments from the database.
    Returns:
        JSON: A list of all assignments.
    """
    # Use SQLAlchemy to query all assignments
    assignments = Assignment.query.all()
    return jsonify(assignments)


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/assignments', methods=['GET'])
def get_assignments():
    # Dummy data
    assignments = [
        {"name": "Assignment 1", "due_date": "2025-02-10", "status": "pending"},
        {"name": "Assignment 2", "due_date": "2025-02-15", "status": "completed"}
    ]
    return jsonify(assignments)

if __name__ == '__main__':
    app.run(debug=True)
