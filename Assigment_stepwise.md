# Assignment Report

## 1. Title Page

**Project:** Student Record Management System
**Subject:** Python Programming & Relational Database
**Assignment:** Assignment 1 – Mini Project
**Course:** MCA Semester I

---

## 2. Introduction

Managing records manually — on paper or in scattered spreadsheets — is slow and error-prone. This project, the **Student Record Management System**, is a console-based Python application that allows an educational institution (or a student practicing Python) to store, view, search, update, and delete student records in an organized and reliable way.

The application is built entirely using Python's standard library. It demonstrates how fundamental programming concepts taught in Semester I — variables, conditionals, loops, functions, exception handling, and file handling — can be combined to build a small but genuinely useful program.

## 3. Problem Statement

Maintaining student information manually leads to several problems:

- Records can be lost, duplicated, or become inconsistent.
- Searching for a specific student's information is slow and tedious.
- Updating or correcting a record often requires rewriting large portions of a register.
- There is no validation, so incorrect or incomplete data (e.g., missing email, invalid age) can easily creep in.

The **Student Record Management System** solves these problems by providing a simple, menu-driven program that:

- Stores every student as a structured record (dictionary) inside a list.
- Validates input before saving, reducing bad data.
- Persists all data in a JSON file, so nothing is lost between sessions.
- Lets the user add, view, search, update, and delete records instantly through a clear menu.

## 4. Objectives

1. Build a working, menu-driven console application in Python.
2. Represent structured data using Python data types: strings, integers, dictionaries, and lists.
3. Apply conditional statements and loops to control program flow.
4. Organize the program into clear, reusable functions.
5. Validate all user input and handle errors gracefully using exception handling.
6. Implement persistent storage using File I/O and the `json` module.
7. Produce clean, readable, well-commented code suitable for a Semester I viva.

## 5. Technologies Used

- **Python 3** — the core programming language used for all program logic.
- **JSON / File I/O** — Python's built-in `json` module is used to serialize the list of student dictionaries to a text file (`students.json`) and deserialize it back into Python objects when the program starts. This provides persistent storage without needing an external database engine, which keeps the assignment focused on core File I/O concepts.

No external frameworks, GUI toolkits, or databases were used — only the Python standard library (`json`, `os`).

## 6. Python Concepts Used

**Data Types and Variables**
Each student is represented as a `dict` containing `str` values (id, name, gender, course, email, phone) and an `int` value (age). All students together are stored in a `list` of dictionaries, which lives in memory while the program runs and is saved to/loaded from JSON.

**Conditional Statements**
`if` / `elif` / `else` statements drive the menu routing in `main()`, decide whether validation passes (e.g., `if age <= 0`), and check whether a searched student was found (`if student is None`).

**Loops**
A `while` loop (controlled by the `program_running` flag) keeps the menu displaying until the user selects Exit. `for` loops iterate over the student list in `find_student()`, `view_students()`, and the name-search feature.

**Functions**
The program is split into focused functions, each with a single responsibility: `load_records()`, `save_records()`, `display_menu()`, `add_student()`, `view_students()`, `search_student()`, `update_student()`, `delete_student()`, `find_student()`, and the `validate_*()` helpers (`validate_student_id`, `validate_name`, `validate_age`, `validate_gender`, `validate_course`, `validate_email`, `validate_phone`).

**Exception Handling**
`try` / `except` / `finally` blocks are used in `load_records()` (to catch `json.JSONDecodeError` and `IOError`/`OSError`), in `save_records()` (to catch write errors), in `validate_age()` (to catch `ValueError` when converting text to an integer), and in `main()` (to catch `KeyboardInterrupt` and any other unexpected exception), so the program never crashes with a raw traceback.

**File I/O**
`students.json` is read using `json.load()` when the program starts and written using `json.dump()` after every add, update, or delete. If the file does not exist yet, the program starts with an empty list and the file is created automatically the first time a record is saved.

**Menu-driven Design**
`display_menu()` prints a numbered list of operations, and `main()` reads the user's choice on each loop iteration and calls the matching function, continuing until the user chooses option 6 (Exit).

## 7. Features

- **Add Student** — Collects all seven fields from the user, validates each one (non-empty ID, unique ID, non-empty name, positive integer age, non-empty gender/course, valid-looking email, valid-length numeric phone), and only saves the record if every check passes.
- **View All Students** — Prints every record in a numbered, labeled format, or a friendly "No student records found." message if the list is empty.
- **Search Student** — Supports searching by Student ID (exact match, case-insensitive) or by Name (partial, case-insensitive match) and reports "Student not found." when there is no match.
- **Update Student** — Finds a student by ID, then lets the user update any field, keeping the existing value if the user leaves a prompt blank. Each new value is re-validated before being applied.
- **Delete Student** — Finds a student by ID, displays the record, and only deletes it after the user explicitly confirms with `y`.

## 8. System Workflow

```
Start
 ↓
Load records (from students.json)
 ↓
Display menu
 ↓
User selects operation
 ↓
Perform operation (Add / View / Search / Update / Delete)
 ↓
Save changes (to students.json)
 ↓
Return to menu
 ↓
Exit (when user chooses option 6)
```

This loop repeats for every menu choice except Exit, so the in-memory list and the JSON file are always kept in sync after any change.

## 9. Data Structure

- **Dictionary** — Each student is one dictionary with fixed keys: `id`, `name`, `age`, `gender`, `course`, `email`, `phone`. This mirrors how a single row/record would look in a database table.
- **List of Dictionaries** — All students are stored together in a single Python `list`, e.g. `students = [ {...}, {...}, {...} ]`. This list is the in-memory "table" that every feature (add, view, search, update, delete) reads from and writes to. It is passed as an argument into each function, keeping the functions decoupled from global state.

## 10. File Handling

`students.json` stores the entire `students` list as a JSON array of objects, for example:

```json
[
    {
        "id": "101",
        "name": "Rajat Sonar",
        "age": 22,
        "gender": "Male",
        "course": "MCA",
        "email": "rajat@example.com",
        "phone": "9876543210"
    }
]
```

- **On startup**, `load_records()` opens the file (if it exists) and uses `json.load()` to convert the JSON text back into a Python list of dictionaries.
- **After every change** (add, update, delete), `save_records()` uses `json.dump()` with `indent=4` to write the current list back to the file in a readable, indented format.
- **If the file is missing**, the program simply starts with an empty list; the file is created automatically the first time a record is saved.
- **If the file is corrupted** (invalid JSON), `load_records()` catches the error, warns the user, and starts with an empty list instead of crashing.

## 11. Exception Handling

The following situations are specifically handled so the program never crashes or shows a raw Python traceback:

- Invalid menu choice (non-numeric or out-of-range) → handled with `if`/`elif`/`else` in `main()`.
- Non-numeric age → `ValueError` caught in `validate_age()`.
- Empty required fields (ID, name, gender, course) → checked explicitly before saving.
- Duplicate Student ID → checked in `validate_student_id()` before adding.
- Student ID not found → checked using `find_student()` returning `None` in search/update/delete.
- Invalid email format → checked in `validate_email()`.
- Invalid phone number (non-digits or wrong length) → checked in `validate_phone()`.
- Missing data file → handled in `load_records()` with `os.path.exists()`.
- Invalid/corrupted JSON file → `json.JSONDecodeError` caught in `load_records()`.
- File read/write errors → `IOError`/`OSError` caught in `load_records()` and `save_records()`.
- Keyboard interrupt (Ctrl+C) and any other unexpected runtime error → caught in the main loop with a general `except Exception` block.

## 12. Testing

| Test Case | Input | Expected Output | Actual Output | Status |
|---|---|---|---|---|
| Add valid student | ID 101, valid fields | "Student added successfully!" | "Student added successfully!" | Pass |
| Add duplicate Student ID | ID 101 again | "Error: A student with this Student ID already exists." | Same | Pass |
| Add empty name | Name = "" | "Error: Name cannot be empty." | Same | Pass |
| Add invalid age | Age = "abc" | "Error: Age must be a valid whole number..." | Same | Pass |
| Add invalid email | Email = "invalidemail" | "Error: Email must contain exactly one '@' symbol." | Same | Pass |
| Add invalid phone | Phone = "12345" | "Error: Phone number must be between 10 and 15 digits long." | Same | Pass |
| View with no records | Menu option 2 (empty list) | "No student records found." | Same | Pass |
| View with multiple records | Menu option 2 (2 students) | Both records listed, "Total Students: 2" | Same | Pass |
| Search existing Student ID | ID 101 | Full record displayed | Same | Pass |
| Search non-existing Student ID | ID 999 | "Student not found." | Same | Pass |
| Search by name (partial match) | "Priya" | Matching record(s) displayed | Same | Pass |
| Update existing student | ID 101, new name/gender | "Student record updated successfully!" | Same | Pass |
| Update non-existing student | ID 999 | "Student not found." | Same | Pass |
| Delete with confirmation | ID 102, confirm "y" | "Student record deleted successfully!" | Same | Pass |
| Delete without confirmation | ID 101, confirm "n" | "Deletion cancelled." | Same | Pass |
| Delete non-existing student | ID 999 | "Student not found." | Same | Pass |
| First run, no JSON file | Program start, no students.json | Program starts normally with empty list | Same | Pass |
| Corrupted JSON file | students.json contains invalid text | Warning shown, program starts with empty list | Same | Pass |
| Restart and verify persistence | Add student, exit, restart, view | Previously added student still present | Same | Pass |
| Invalid menu option | Choice = "9" | "Invalid choice. Please enter a number between 1 and 6." | Same | Pass |
| Non-numeric menu input | Choice = "abc" | "Invalid choice. Please enter a number between 1 and 6." | Same | Pass |

All test cases above were executed against the actual program (by simulating console input) and passed as expected.

## 13. Sample Output

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
Enter your choice: 3

---------------- SEARCH STUDENT ----------------
1. Search by Student ID
2. Search by Name
Enter your choice (1 or 2): 1
Enter Student ID to search: 101

Student Found:
----------------------------------------
Student ID : 101
Name       : Rajat Sonar
Age        : 22
Gender     : Male
Course     : MCA
Email      : rajat@example.com
Phone      : 9876543210
```

## 14. Screenshots

_Screenshots of each menu option in action should be added here, and saved inside the `screenshots/` folder._

![Main Menu](screenshots/01-main-menu.png)
![Add Student](screenshots/02-add-student.png)
![View Students](screenshots/03-view-students.png)
![Search Student](screenshots/04-search-student.png)
![Update Student](screenshots/05-update-student.png)
![Delete Student](screenshots/06-delete-student.png)

## 15. Conclusion

Building the Student Record Management System reinforced several core Python programming concepts in a practical setting. Structuring each student as a dictionary and storing many students in a list showed how Python's built-in data structures can model real-world records. Writing separate, single-purpose functions for each operation made the code easier to test, debug, and explain. Implementing input validation and exception handling highlighted the importance of anticipating bad input rather than assuming users will always provide correct data. Finally, using the `json` module for File I/O demonstrated how a program can persist data between runs without requiring a full database system — an important stepping stone before working with relational databases later in the course.

## 16. GitHub Repository

GitHub Repository:
[Add repository link here]