# All Employee information BY OLAWALE I.
employees = [
    {"name": "John", "age": 65, "experience": 15},
    {"name": "Sam", "age": 72, "experience": 10},
    {"name": "Sarah", "age": 60, "experience": 6},
    {"name": "Lester", "age": 70, "experience": 9},
    {"name": "Doreen", "age": 65, "experience": 5}
]

# Authentication Process by NAOMI O.
attempts = 0
while attempts <5:
    access_code = input("Enter access code: ")
    if access_code != "4563":
        print("Error: Wrong Access Code. Please try again!")
        attempts += 1
    else:
        portal_code = input("Enter portal code for authentication: ")
        if portal_code != "2487":
            print("Error: Wrong Portal Code. Please try again!")
            attempts += 1
        else:
            print("Authentication successful. Access granted.")
            break
else:
    print("Error: You have exceeded the maximum attempts. Access Denied!")
    exit()

# Function to check individual eligibility BY SYLVESTER N.
def check_eligibility(employee_name):
    employee_found = False
    for employee in employees:
        if employee["name"] == employee_name:
            employee_found = True
            if employee["age"] >= 65:
                if employee["experience"] >= 8:
                    print(employee['name'] + "is eligible for $20,000 in retirement benefit and a $2000 bonus")
                else:
                    print(employee['name'] + "is eligible for $20,000 in retirement benefit only")
            else:
                print(employee['name'] + "is not eligible for the retirement benefit and bonus")
            break

    if not employee_found:
        print("Name is not found in the employee list")


# Check individual eligibility BY OLAWALE I., NAOMI O., AND SYLVESTER N.
check_count=0
while check_count < 6:
    employee_to_check = input("Enter the name of the employee to check eligibility: ")
    if employee_to_check == "exit":
        break
    else:
        check_eligibility(employee_to_check)
        check_count += 1
else:
    print("Maximum limit of checks reached (6 times). Exiting...")