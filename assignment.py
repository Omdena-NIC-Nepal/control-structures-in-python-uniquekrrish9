
# Task 1: while loop
def while_loop():
    number = 0
    while number <= 20:
        if number % 2 == 0:
            print(number)
        if number == 16:
            break
        number += 1
while_loop()


# Task 2: For loop with continue
def for_loop_continue():
    for num in range(1,16):
        if num % 3 == 0:
            continue
        print(num)
for_loop_continue()


# Task 3: if-else statement

import sys
def number_classification():
    try:
        n = int(sys.stdin.readline().strip())  # Use readline() instead of read()
    except ValueError:
        n = 0  # Default value if no input is provided
    
    if n < 0:
        print("negative")
    elif n == 0:
        print("zero")
    else:
        print("positive")




# Task 4: Nested loops
def multiplication_table():
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i} x {j} = {i * j}")
multiplication_table()