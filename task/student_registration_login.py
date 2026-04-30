import re
import json
import os

class StudentSystem:
    FILE_NAME = "students.json"

    name_pattern = r"^[A-Za-z ]{3,30}$"
    address_pattern = r"^[A-Za-z0-9 ,.\-/]{10,100}$"
    id_pattern = r"^STU\d{4}$"
    password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$"

    # ------------------- REGISTRATION -------------------
    def register(self):
        print("---- Registration ----")

        name = input("Enter your name: ").strip()
        address = input("Enter your address: ").strip()
        student_id = input("Enter your student ID: ").strip()
        password = input("Enter your password: ").strip()

        # Validation
        if not re.fullmatch(self.name_pattern, name):
            print("Invalid Name!")
            return
        if not re.fullmatch(self.address_pattern, address):
            print("Invalid Address!")
            return
        if not re.fullmatch(self.id_pattern, student_id):
            print("Invalid Student ID!")
            return
        if not re.fullmatch(self.password_pattern, password):
            print("Invalid Password!")
            return

        # Load existing data safely
        data = {}
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = {}

        # Duplicate check
        if student_id in data:
            print("User already exists")
            return

        # Save user
        data[student_id] = password

        with open(self.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        print("Registration Successful")

    # ------------------- LOGIN -------------------
    def login(self):
        print("\n---- Login ----")

        login_id = input("Enter your student ID: ").strip()
        login_password = input("Enter your student password: ").strip()

        # File check
        if not os.path.exists(self.FILE_NAME):
            print("No users registered")
            return

        # JSON read
        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Data error")
            return

        if login_id in data and data[login_id] == login_password:
            print("Login Successful")
        else:
            print("Invalid Student ID or Password")


# ------------------- MAIN -------------------
system = StudentSystem()

print("1. Register")
print("2. Login")

choice = input("Enter choice: ")

if choice == "1":
    system.register()
elif choice == "2":
    system.login()
else:
    print("Invalid choice")