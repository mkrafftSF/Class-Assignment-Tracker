<<<<<<< HEAD
=======
<!-- Documentation Update for Assignment Table -->
The Assignment Table now includes enhanced sorting and filtering options for improved usability. Additional details have been added to explain how data is processed and displayed. Closes #18.

>>>>>>> eecba84cf4f8d372c389c01eae78fe86e7e63a57

# Class-Assignment-Tracker
A Python-based tool for automating and visualizing class assignment tracking using Plotly, Pandas, and IPywidgets
# Class Assignment Tracker Automation Tool

## Description
This project automates the tracking of assignments, visualizes progress with Plotly, and enables interactive updates with IPywidgets. It processes data stored in CSV format using Pandas.

## Team Members
- Michael A. Krafft, Ph.D.

## Technologies Used
- **Python**: Main programming language
- **Plotly**: For rendering final table visualization
- **Pandas**: For data processing
- **IPywidgets**: For interactive UI elements in Jupyter Notebook

Module 2: Find a Teammate Submission

To: Dr. Julia Damerow

From: Dr. Michael A. Krafft

Subject: M2 Assignment Submission – Class Project Proposal

Introduction

In the Spring of 2024, I collaborated with Annaka and Pradeesh on our CAS 502 class project, where we developed an Assignment and Deadline Tracker using a Jupyter Notebook. However, due to unforeseen circumstances, including the passing of a close family member and other personal challenges, I was unable to fully complete the course. This experience was difficult, but I’m grateful for the opportunity to retake the class in Spring 2025 and build upon the progress my team and I made.

Rather than starting a new group project, I’ve decided to continue developing our original project. This approach not only allows me to honor the hard work we put into the initial version but also gives me the chance to refine and enhance the tool in ways that reflect the lessons I’ve learned and my continued growth in this area.

Project Idea and Background
Project Name: Assignment and Deadline Tracker (Interactive Jupyter Notebook)

Objective: The Assignment and Deadline Tracker is designed to help students manage their assignments and deadlines by importing data from a CSV file, marking tasks as completed, and displaying the updated list with visual highlights for easy tracking.

Reason for Continuing the Project: I chose to continue this project because it directly aligns with the learning objectives of this course, and it offers a strong foundation for further development. Rather than starting from scratch, I can focus on enhancing the existing functionality to improve the user experience and apply more advanced techniques, such as data visualization and user input handling. This approach allows me to gain deeper programming and design experience while reinforcing lessons from the first attempt.

Contributions and Challenges in Spring 2024
In Spring 2024, I made significant contributions to the team's progress:

Data Loading and Task Updates: I ensured that the program could correctly import assignment data from a CSV file and save updated task statuses back to the file.
Debugging Input Errors: I helped resolve issues related to user inputs, ensuring the program handled task completion updates smoothly.
Improving the Display Format: I suggested formatting changes to make the output more user-friendly, such as highlighting completed tasks for easier identification.
However, our team encountered some challenges that limited the scope of the project:

Handling User Errors: The program occasionally crashes due to unexpected inputs, such as typos or missing information.
Limited Visualization: We initially wanted to include data visualizations to track progress, but we could not implement this due to time constraints.
Balancing Responsibilities: Our individual workloads outside the course made it difficult to finalize some features by the submission deadline.
These challenges highlighted areas where I can improve the project to ensure greater robustness and interactivity.

Planned Enhancements for Spring 2025
Progress Visualization
What: Add simple visual representations, such as bar charts or tables, to show the number of completed and remaining tasks.
Why: A visual summary provides a quick and intuitive way for users to understand their progress at a glance.
How: I plan to use Pandas to create summary tables and Matplotlib to generate basic bar charts that update as tasks are marked complete. The bar chart will display categories such as "Completed" and "Remaining" tasks, making the interface more engaging and informative.
Task Status Highlighting
What: Automatically highlight overdue tasks in a different color for easier tracking.
Why: Highlighting overdue tasks will help users prioritize their workload by drawing attention to assignments that need immediate attention.
How: I will use Pandas DataFrame styling to apply conditional formatting. The program will compare the current date to assignment deadlines and apply colors to overdue, completed, and pending tasks.
User-Friendly Input
What: Add prompts and input validation to ensure the program gracefully handles invalid or incomplete inputs.
Why: Input validation prevents the program from crashing due to typos or missing information and enhances user experience.
How: I will implement checks to verify that the user enters valid data (e.g., confirming the assignment name exists before marking it as complete). If the input is invalid, the program will display a helpful error message and prompt the user to try again.
Meeting Course Requirements
Discussion Post: This proposal describes the project idea and enhancements in detail and is my official post for the "Find a Teammate" discussion. Since continuing with a previous project, I will work independently and not seek a new team.
Enhancements and Additions: By implementing visualizations, conditional formatting, and input validation, I am adding new code and functionality to the existing project, meeting the requirement to contribute meaningful improvements.
Class Project Teams: Although I am working alone, I will ensure my project progress is documented and submitted as outlined in the course instructions.
Conclusion
I am excited to retake this course and apply the lessons I've learned to improve the Assignment and Deadline Tracker. This project aligns well with the course objectives by requiring practical programming, data management, and user interaction design. I look forward to demonstrating meaningful progress and delivering a more robust and user-friendly tool.

Please let me know if you have any questions or additional feedback.

Best regards,

Dr. Michael A. Krafft

# Assignment and Deadline Tracker

## Purpose
A project to track assignments, manage deadlines, and visualize progress interactively.

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
