# Step 2
number1 = int(input('Enter a number: '))

# Step 3, 4, and 5
if number1 % 3 == 0 and number1 % 5 == 0:
    print(number1, 'Tic Tac')
elif number1 % 3 == 0:
    print(number1, 'Tic')
elif number1 % 5 == 0:
    print(number1, 'Tac')

# Step 6
x = 1
while x <= 20:
    print(x)
    x += 1

# Step 7
x = 1
while x <= 20:
    if x % 3 == 0 and x % 5 == 0:
        print(x, 'Tic Tac')
    elif x % 3 == 0:
        print(x, 'Tic')
    elif x % 5 == 0:
        print(x, 'Tac')
    else:
        print(x)
    x += 1

import random

# Step 8
random_number = random.randint(1, 100)

# Step 9
count = 0
while count < 5:
    user_digit = int(input("Please enter a value: "))
    if user_digit > 0:
        break
    else:
        print("The value entered is not greater than 0. Please enter again.")
        count += 1

# Step 10
if count < 5:
    random_number = random.randint(1, user_digit)
    print("Random number generated: ", random_number)
else:
    print("Failed to provide a valid input after 5 attempts.")
