"""
This script populates the database with sample data from a CSV file.
"""
# Import the necessary modules
import csv
from models import Assignment
from datetime import datetime

# Open the CSV file containing the sample assignments
with open('assignments.csv', 'r') as file:
    reader = csv.DictReader(file)

    # Loop through each row in the CSV
    for row in reader:
        # Convert the row data to an Assignment object
        assignment = Assignment(
            name=row['name'],
            due_date=datetime.strptime(row['due_date'], '%Y-%m-%d'),
            status=row['status']
        )
        db.session.add(assignment)  # Add to the session

# Commit the changes to save to the database
db.session.commit()
