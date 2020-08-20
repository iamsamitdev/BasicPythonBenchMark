# age = int(input("Enter your age: "))
# print(age+5)

username = input("Enter username: ")
password = input("Enter password: ")

set_username = "admin"
set_password = "1234"

if username == set_username and password == set_password:
    print("Yah! Login successfully")
else:
    print("Opp! Login fail!")
