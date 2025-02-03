import plotly.graph_objects as go
import pandas as pd
import ipywidgets as widgets
import datetime

# Define the file path to your CSV data
file_path = r"C:\Users\annak\CAS-502 Computation\GroupProject-1\GP1 Dataset_ Assignments.csv"
# Load the CSV file with a specified encoding
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Convert the DATE column to datetime objects
df['DATE'] = pd.to_datetime(df['DATE'], format='%m/%d/%Y')

# Define a function to calculate a pre-deadline date
def get_predeadline(deadline, buffer_days=1):
    predeadline = deadline - datetime.timedelta(days=buffer_days)
    return predeadline

# Calculate PREDEADLINE for each assignment date
df['PREDEADLINE'] = df['DATE'].apply(lambda x: get_predeadline(x, buffer_days=1))

# Rearrange columns so that PREDEADLINE comes after DATE
column_order = ['ITEM#', 'DATE', 'PREDEADLINE', 'WK#', 'COURSE', 'ASSIGNMENT NAME', 'DESCRIPTION', 'DONE']
df = df[column_order]

# Save the modified DataFrame to a new CSV file
original_file_path = file_path
new_file_name = "GP1 Dataset_ Assignments_PreDeadline.csv"
new_file_path = original_file_path.rsplit('\\', 1)[0] + '\\' + new_file_name
df.to_csv(new_file_path, index=False)
print(f"File saved as: {new_file_path}")

# Set up a Colors column for visual feedback (example: 'black' for open, 'red' for closed)
df['Colors'] = 'nil'
for index, row in df.iterrows():
    if row.get('Status', 'Open') == 'Open':  # Use 'Status' if available, default to 'Open'
        df.at[index, 'Colors'] = 'black'
    else:
        df.at[index, 'Colors'] = 'red'

# Create a list of assignment names for the dropdown widget, inserting a 'None' option at the beginning
a_list = list(df['ASSIGNMENT NAME'])
a_list.insert(0, 'None')

# Create interactive widgets: a dropdown for assignment names and a button to mark as complete
button = widgets.Button(description="Mark As Complete")
text = widgets.Dropdown(
    options=a_list,
    value=a_list[0],
    description='Assignment Name:',
    disabled=False,
)
output = widgets.Output()

# Define the function that is called when the button is clicked
def on_button_clicked(b):
    with output:
        output.clear_output()
        a_name = text.value
        if a_name != 'None':
            # Find the index of the selected assignment
            index_req = df.index[df['ASSIGNMENT NAME'] == a_name].to_list()
            if index_req:
                # Mark the assignment as closed and update the color
                df.at[index_req[0], 'Status'] = 'Closed'
                df.at[index_req[0], 'Colors'] = 'red'
                # Sort the DataFrame (e.g., by Status and DATE)
                df.sort_values(by=['Status', 'DATE'], inplace=True, ascending=[False, True])
        # Save the updated data to a test file
        df.to_csv('testdata.csv', columns=['DATE', 'WK#', 'COURSE', 'ASSIGNMENT NAME', 'DESCRIPTION', 'Status'], index=False)
        # Create a Plotly table to display the assignments
        fig = go.Figure(data=[go.Table(
            header=dict(
                values=["Date", "Week #", "Course", "Assignment Name", "Description", "Status"],
                line_color='white', fill_color='white',
                align='center', font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[df['DATE'], df['WK#'], df['COURSE'], df['ASSIGNMENT NAME'], df['DESCRIPTION'], df['Status']],
                align='center', font=dict(color=[df.Colors], size=11)
            )
        )])
        fig.show()

# Link the button to the click function
button.on_click(on_button_clicked)

# Create a layout for the widgets
list_button = widgets.HBox([text, button])
widgets.VBox([list_button, output])
