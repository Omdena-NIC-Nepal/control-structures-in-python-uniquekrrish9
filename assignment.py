# Task 1: while loop
def while_loop():
    number = 0
    while number <= 20:
        if number % 3 == 0:
            print(number)
        number += 1

# Task 2: For loop with continue
def for_loop_continue():
    for num in range(1,16):
        if num % 3 == 0:
            continue
        print(num)

# Task 3: if-else statement
def number_classification():
    number = int(input("Enter a number: "))

    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
    else:
        print("zero")

# Task 4: Nested loops
def multiplication_table():
    for i in range(1, 6):  # Outer loop (rows)
        for j in range(1, 6):  # Inner loop (columns)
            print(f"{i} x {j} = {i * j}")  # Print multiplication result
        print() 
