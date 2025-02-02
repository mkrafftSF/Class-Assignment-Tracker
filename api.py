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
