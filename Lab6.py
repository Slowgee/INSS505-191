def check_for_even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
def check_for_prime_or_nonprime(num):
    if num <= 1:
        return "nonprime"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "nonprime"
    return "prime"

while True:
    num = int(input("Enter a number: "))

    if num <= 0:
        print("Wrong input, enter number >0")
    else:
        num_type = check_for_even_or_odd(num)
        num_prime_nonprime = check_for_prime_or_nonprime(num)
        print(f"{num} is an {num_type} number and it is {num_prime_nonprime}.")

