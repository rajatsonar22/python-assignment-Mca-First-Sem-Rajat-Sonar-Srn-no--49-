import json
import os

DATA_FILE = "students.json"

def load_records():
\
\
\
\
\
\
\


    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            else:
                print("Warning: Data file format is invalid. Starting with empty records.")
                return []
    except json.JSONDecodeError:

        print("Warning: students.json is corrupted or invalid. Starting with empty records.")
        return []
    except (IOError, OSError):

        print("Warning: Could not read the data file. Starting with empty records.")
        return []

def save_records(students):
\
\
\

    try:
        with open(DATA_FILE, "w") as file:
            json.dump(students, file, indent=4)
    except (IOError, OSError):
        print("Error: Unable to save records to file. Please check file permissions.")
    finally:

        pass

def validate_student_id(student_id, students, is_update=False):
\
\
\
\
\

    if student_id.strip() == "":
        print("Error: Student ID cannot be empty.")
        return False

    if not is_update:
        existing = find_student(students, student_id)
        if existing is not None:
            print("Error: A student with this Student ID already exists.")
            return False

    return True

def validate_name(name):

    if name.strip() == "":
        print("Error: Name cannot be empty.")
        return False
    return True

def validate_age(age_str):
\
\
\

    try:
        age = int(age_str)
        if age <= 0:
            print("Error: Age must be a positive number.")
            return False, None
        if age > 100:
            print("Error: Age seems unrealistic. Please enter a valid age.")
            return False, None
        return True, age
    except ValueError:

        print("Error: Age must be a valid whole number (e.g., 21).")
        return False, None

def validate_gender(gender):

    if gender.strip() == "":
        print("Error: Gender cannot be empty.")
        return False
    return True

def validate_course(course):

    if course.strip() == "":
        print("Error: Course cannot be empty.")
        return False
    return True

def validate_email(email):
\
\
\
\
\
\
\
\
\

    email = email.strip()
    if email == "":
        print("Error: Email cannot be empty.")
        return False

    if email.count("@") != 1:
        print("Error: Email must contain exactly one '@' symbol.")
        return False

    username_part, domain_part = email.split("@")

    if username_part == "" or domain_part == "":
        print("Error: Email format is invalid.")
        return False

    if "." not in domain_part:
        print("Error: Email domain must contain a '.' (e.g., example.com).")
        return False

    return True

def validate_phone(phone):
\
\
\
\

    phone = phone.strip()
    if phone == "":
        print("Error: Phone number cannot be empty.")
        return False

    if not phone.isdigit():
        print("Error: Phone number must contain digits only.")
        return False

    if len(phone) < 10 or len(phone) > 15:
        print("Error: Phone number must be between 10 and 15 digits long.")
        return False

    return True

def find_student(students, student_id):
\
\
\
\

    for student in students:
        if student["id"].lower() == student_id.lower():
            return student
    return None

def add_student(students):
\
\
\

    print("\n---------------- ADD NEW STUDENT ----------------")

    student_id = input("Enter Student ID: ")
    if not validate_student_id(student_id, students):
        return

    name = input("Enter Name: ")
    if not validate_name(name):
        return

    age_input = input("Enter Age: ")
    is_valid_age, age = validate_age(age_input)
    if not is_valid_age:
        return

    gender = input("Enter Gender: ")
    if not validate_gender(gender):
        return

    course = input("Enter Course: ")
    if not validate_course(course):
        return

    email = input("Enter Email: ")
    if not validate_email(email):
        return

    phone = input("Enter Phone Number: ")
    if not validate_phone(phone):
        return

    new_student = {
        "id": student_id.strip(),
        "name": name.strip(),
        "age": age,
        "gender": gender.strip(),
        "course": course.strip(),
        "email": email.strip(),
        "phone": phone.strip()
    }

    students.append(new_student)

    save_records(students)

    print("\nStudent added successfully!")

def view_students(students):
\
\
\

    print("\n---------------- ALL STUDENT RECORDS ----------------")

    if len(students) == 0:
        print("No student records found.")
        return

    for index, student in enumerate(students, start=1):
        print(f"\nRecord #{index}")
        print("-" * 40)
        print(f"Student ID : {student['id']}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Gender     : {student['gender']}")
        print(f"Course     : {student['course']}")
        print(f"Email      : {student['email']}")
        print(f"Phone      : {student['phone']}")

    print("-" * 40)
    print(f"Total Students: {len(students)}")

def search_student(students):
\
\
\

    print("\n---------------- SEARCH STUDENT ----------------")
    print("1. Search by Student ID")
    print("2. Search by Name")
    search_choice = input("Enter your choice (1 or 2): ")

    if search_choice == "1":
        student_id = input("Enter Student ID to search: ")
        student = find_student(students, student_id)

        if student is None:
            print("Student not found.")
        else:
            print("\nStudent Found:")
            print("-" * 40)
            print(f"Student ID : {student['id']}")
            print(f"Name       : {student['name']}")
            print(f"Age        : {student['age']}")
            print(f"Gender     : {student['gender']}")
            print(f"Course     : {student['course']}")
            print(f"Email      : {student['email']}")
            print(f"Phone      : {student['phone']}")

    elif search_choice == "2":
        name_query = input("Enter Name to search: ").strip().lower()
        found_any = False

        for student in students:
            if name_query in student["name"].lower():
                if not found_any:
                    print("\nMatching Student(s):")
                print("-" * 40)
                print(f"Student ID : {student['id']}")
                print(f"Name       : {student['name']}")
                print(f"Age        : {student['age']}")
                print(f"Gender     : {student['gender']}")
                print(f"Course     : {student['course']}")
                print(f"Email      : {student['email']}")
                print(f"Phone      : {student['phone']}")
                found_any = True

        if not found_any:
            print("Student not found.")
    else:
        print("Invalid choice. Please select 1 or 2.")

def update_student(students):
\
\
\
\

    print("\n---------------- UPDATE STUDENT ----------------")
    student_id = input("Enter Student ID to update: ")
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    print("Leave a field blank and press Enter to keep the current value.")

    new_name = input(f"Enter new Name [{student['name']}]: ")
    if new_name.strip() != "":
        if validate_name(new_name):
            student["name"] = new_name.strip()
        else:
            return

    new_age = input(f"Enter new Age [{student['age']}]: ")
    if new_age.strip() != "":
        is_valid_age, age = validate_age(new_age)
        if is_valid_age:
            student["age"] = age
        else:
            return

    new_gender = input(f"Enter new Gender [{student['gender']}]: ")
    if new_gender.strip() != "":
        if validate_gender(new_gender):
            student["gender"] = new_gender.strip()
        else:
            return

    new_course = input(f"Enter new Course [{student['course']}]: ")
    if new_course.strip() != "":
        if validate_course(new_course):
            student["course"] = new_course.strip()
        else:
            return

    new_email = input(f"Enter new Email [{student['email']}]: ")
    if new_email.strip() != "":
        if validate_email(new_email):
            student["email"] = new_email.strip()
        else:
            return

    new_phone = input(f"Enter new Phone Number [{student['phone']}]: ")
    if new_phone.strip() != "":
        if validate_phone(new_phone):
            student["phone"] = new_phone.strip()
        else:
            return

    save_records(students)
    print("\nStudent record updated successfully!")

def delete_student(students):
\
\
\

    print("\n---------------- DELETE STUDENT ----------------")
    student_id = input("Enter Student ID to delete: ")
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nRecord to be deleted:")
    print("-" * 40)
    print(f"Student ID : {student['id']}")
    print(f"Name       : {student['name']}")
    print(f"Age        : {student['age']}")
    print(f"Gender     : {student['gender']}")
    print(f"Course     : {student['course']}")
    print(f"Email      : {student['email']}")
    print(f"Phone      : {student['phone']}")

    confirmation = input("\nAre you sure you want to delete this student? (y/n): ")

    if confirmation.strip().lower() == "y":
        students.remove(student)
        save_records(students)
        print("\nStudent record deleted successfully!")
    else:
        print("\nDeletion cancelled.")

def display_menu():

    print("\n====================================================")
    print("          STUDENT RECORD MANAGEMENT SYSTEM")
    print("====================================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("====================================================")

def main():
\
\
\
\
\


    students = load_records()

    program_running = True

    while program_running:
        display_menu()

        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                add_student(students)
            elif choice == "2":
                view_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                update_student(students)
            elif choice == "5":
                delete_student(students)
            elif choice == "6":
                print("\nThank you for using Student Record Management System. Goodbye!")
                program_running = False
            else:

                print("Invalid choice. Please enter a number between 1 and 6.")

        except KeyboardInterrupt:

            print("\n\nProgram interrupted by user. Exiting safely...")
            program_running = False
        except Exception as error:

            print(f"An unexpected error occurred: {error}")

if __name__ == "__main__":
    main()
