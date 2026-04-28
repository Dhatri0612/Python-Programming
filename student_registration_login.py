import re
student_name=input("Enter your name: ")
student_address=input("Enter your address: ")
student_id=input("Enter your student ID: ")
password = input("Enter your password: ")

name_pattern=r"^[A-Za-z ]{3,30}$"
address_pattern=r"^[a-zA-Z0-9 ,.\-/]{10,100}$"
id_pattern=r"^STU\d{4}$"
password_pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$"

if not re.fullmatch(name_pattern,student_name):
    print("Invalid Name! Only letters & spaces (3-30 chars allowed)")
elif not re.fullmatch(address_pattern,student_address):
    print("Invalid Address! Must be 10 to 100 chars with valid symbols")
elif not re.fullmatch(id_pattern,student_id):
    print("Invalid Student ID! Format should be STU1234")
elif not re.fullmatch(password_pattern,password):
    print("Invalid Password! Must contain uppercase, lowercase, digit, special char (8–16 chars)")
else:
    stored_id=student_id
    stored_password=password
    print("Registration Successful")
    
    login_id=input("Enter your student ID: ")
    login_password=input("Enter your student password: ")
    if login_id==stored_id and login_password==stored_password:
        print("Login Successful")
    else:
        print("Invalid Student ID or Password")