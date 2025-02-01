import matplotlib.pyplot as plt
import pandas as pd

def generate_progress_chart(assignments_df):
    """
    Generate a bar chart showing the count of assignments in each category:
    - Completed
    - Overdue
    - Pending
    """
    # Ensure the DataFrame has a 'status' column, where status can be "Completed", "Overdue", or "Pending"
    summary = assignments_df['status'].value_counts()
    categories = ['Completed', 'Overdue', 'Pending']
    counts = [summary.get(cat, 0) for cat in categories]
    
    plt.figure(figsize=(6, 4))
    plt.bar(categories, counts, color=['green', 'red', 'blue'])
    plt.title('Assignment Progress')
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.ylim(0, max(counts) + 2)
    plt.tight_layout()
    plt.show()
