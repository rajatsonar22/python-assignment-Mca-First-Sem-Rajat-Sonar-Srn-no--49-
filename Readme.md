# Student Record Management System

## Project Description

The **Student Record Management System** is a console-based Python application that allows a user to manage student records — adding, viewing, searching, updating, and deleting them — entirely from the terminal.

It was created as **Assignment 1** for the **Python Programming & Relational Database** course (MCA Semester I). The goal of the assignment is to apply fundamental Python programming concepts — data types, conditionals, loops, functions, exception handling, and file I/O — to build a small but complete, real-world style application.

Instead of a database, the application uses a **JSON file (`students.json`)** as persistent storage, which keeps the project focused on core Python File I/O concepts rather than external database software.

## Features

- **Add Student** — Enter a new student's details with full input validation.
- **View All Students** — Display every saved student record in a readable format.
- **Search Student** — Look up a student by Student ID (mandatory) or by Name (optional extra feature).
- **Update Student** — Modify an existing student's details; unchanged fields can be skipped.
- **Delete Student** — Remove a student record after a confirmation prompt.
- **Persistent JSON Storage** — All records are saved to `students.json` and reloaded automatically the next time the program runs.
- **Input Validation** — Student ID, name, age, gender, course, email, and phone number are all validated before being saved.
- **Exception Handling** — Invalid input, missing files, and corrupted data are handled gracefully without crashing the program.
- **Menu-driven Interface** — A simple numbered menu that loops until the user chooses to exit.

## Technologies Used

- Python 3
- JSON (Python's built-in `json` module)
- Python File I/O
- Lists
- Dictionaries
- Functions
- Conditional Statements (`if` / `elif` / `else`)
- Loops (`for`, `while`)
- Exception Handling (`try` / `except` / `finally`)

## Python Concepts Demonstrated

1. **Data Types and Variables**
   Each student record uses a `dict` with `str` fields (ID, name, gender, course, email, phone) and an `int` field (age). Multiple records are stored as a `list` of dictionaries in memory.

2. **Conditional Statements**
   `if` / `elif` / `else` statements are used throughout — for menu routing (`main()`), for input validation (e.g. checking if age is positive, if email has an `@`), and for deciding whether a student was found.

3. **Loops**
   `while True`-style loops (via the `program_running` flag) keep the main menu running until the user exits. `for` loops are used to iterate over the student list when searching, displaying, or validating uniqueness of IDs.

4. **Functions**
   The program is broken into small, single-purpose functions such as `add_student()`, `view_students()`, `search_student()`, `update_student()`, `delete_student()`, `find_student()`, and several `validate_*()` helper functions, instead of one large script.

5. **Exception Handling**
   `try` / `except` / `finally` blocks handle invalid age input (`ValueError`), corrupted JSON files (`json.JSONDecodeError`), file read/write errors (`IOError`/`OSError`), keyboard interrupts, and any other unexpected errors — all without showing a raw Python traceback to the user.

6. **File I/O**
   `load_records()` reads `students.json` at startup using `json.load()`, and `save_records()` writes the current list back using `json.dump()` after every add, update, or delete operation. If the file doesn't exist, the program starts with an empty list and creates the file on first save.

7. **Menu-driven Application Design**
   `display_menu()` prints a numbered menu, and `main()` repeatedly reads the user's choice and dispatches it to the correct function, continuing until option 6 (Exit) is chosen.

## Project Structure

```
student-record-management/
│
├── main.py                 # The complete application source code
├── students.json            # JSON data file (auto-created/updated by the program)
├── README.md                 # Project documentation (this file)
├── Assignment_Report.md      # Full academic assignment report
│
└── screenshots/               # Folder for evaluation screenshots
    └── .gitkeep
```

- **main.py** — Contains all program logic: file I/O functions, validation helpers, the four CRUD features, the menu, and the `main()` entry point.
- **students.json** — Stores all student records as a JSON array of objects. Created automatically the first time a student is added, and updated after every change.
- **README.md** — This documentation file.
- **Assignment_Report.md** — The full written assignment report, including problem statement, objectives, testing table, and conclusion.
- **screenshots/** — Placeholder folder where evaluation screenshots can be added later.

## How to Run

**Requirements:** Python 3.6 or higher (no external libraries needed — only the Python standard library).

1. Open a terminal in the project folder.
2. Run the application:

```bash
python main.py
```

   (On some systems you may need to use `python3 main.py` instead.)

3. Follow the on-screen menu to add, view, search, update, or delete student records.
4. Choose option **6** to exit. Your data is automatically saved to `students.json` and will still be there the next time you run the program.

## Sample Usage

```
====================================================
          STUDENT RECORD MANAGEMENT SYSTEM
====================================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
====================================================
Enter your choice: 1

---------------- ADD NEW STUDENT ----------------
Enter Student ID: 101
Enter Name: Rajat Sonar
Enter Age: 22
Enter Gender: Male
Enter Course: MCA
Enter Email: rajat@example.com
Enter Phone Number: 9876543210

Student added successfully!
```

```
Enter your choice: 2

---------------- ALL STUDENT RECORDS ----------------

Record #1
----------------------------------------
Student ID : 101
Name       : Rajat Sonar
Age        : 22
Gender     : Male
Course     : MCA
Email      : rajat@example.com
Phone      : 9876543210
----------------------------------------
Total Students: 1
```

## Screenshots

_Add screenshots of the running application here to show each feature in action._

![Main Menu](screenshots/01-main-menu.png)
![Add Student](screenshots/02-add-student.png)
![View Students](screenshots/03-view-students.png)
![Search Student](screenshots/04-search-student.png)
![Update Student](screenshots/05-update-student.png)
![Delete Student](screenshots/06-delete-student.png)

## GitHub Repository

GitHub Repository:
[Add repository link here]