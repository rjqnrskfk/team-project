# team-project

Auto Timetable Generator
Generates optimized timetables based on a list of subjects

Cool timetable generator built using Streamlit and Google OR-Tools.

This project lets users generate a valid timetable by solving a constraint satisfaction problem.
It’s inspired by real scheduling challenges many students face when trying to avoid time conflicts while taking multiple classes.

Key Points

Core Concepts

Streamlit is used to provide a simple user interface.

Users can generate timetables with a single button click.

The scheduling algorithm uses OR-Tools CP-SAT solver to assign subjects to timeslots without conflicts.

Scheduling Rules

Each subject must be assigned exactly one timeslot.

No two subjects can occupy the same timeslot.

The result is a conflict-free timetable.

How It Works

Subjects and timeslots are defined in Python lists.

CP-SAT constructs a boolean variable for each subject×timeslot pair.

Constraints enforce valid assignments only.

Solver finds a feasible timetable.

Requirements

You will need:

Python (3.7+ recommended)

streamlit

ortools

Install dependencies:

pip install streamlit ortools

Commands to Run the App

From your project src folder, run:

streamlit run main.py


This will launch the web app in your browser.
Click “시간표 생성” (Generate Timetable) to see results.

Example UI Behavior

Simple button to trigger timetable creation.

Display of assigned timeslots for each subject.

No conflict schedules generated instantly.

Limitations

Currently uses a fixed list of subjects and timeslots in code.

Does not yet support file upload for custom inputs (JSON/CSV).

Timeslot preferences (e.g., morning/afternoon) are not yet considered.

About

This project was created to demonstrate how optimization libraries like OR-Tools can be combined with Python UI tools like Streamlit to solve practical scheduling problems.
Future work may include CSV/JSON input support and a more flexible user interface.
