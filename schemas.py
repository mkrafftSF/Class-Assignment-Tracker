"""
This file defines Marshmallow schemas for serializing and deserializing assignment data.
"""
class AssignmentSchema(ma.Schema):
    """
    Marshmallow schema for serializing Assignment objects.
    Fields:
        id (int): The unique ID of the assignment.
        name (str): The name of the assignment.
        due_date (str): The deadline for the assignment.
        status (str): The status of the assignment (e.g., 'pending' or 'completed').
    """
    class Meta:
        fields = ('id', 'name', 'due_date', 'status')  # Fields to include in serialization
