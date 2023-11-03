inputs = []
for n in range(5):
    num = float(input(f"Enter number {n + 1}: "))
    inputs.append(num)

total_sum = sum(inputs)
average = total_sum / 5

print(f"Sum: {total_sum}")
print(f"Average: {average}")