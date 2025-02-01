import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Assignment': ['Assignment 1', 'Assignment 2', 'Assignment 3'],
    'Completion Rate': [85, 90, 78]
}

df = pd.DataFrame(data)

# Create a bar chart
fig = px.bar(df, x='Assignment', y='Completion Rate', title='Assignment Completion Rates')

# Show the plot
fig.show()
