#Simple number printer
print("This section prints the numbers from 1 to 10.")
number = 0
while number < 10:
    number += 1
    print(number)

#Sum until zero
print("This section takes the numbers you enter, sum them up and give you the sum when you enter 0 as your number.")
number = 0
while True:
    user_input = int(input("Enter a number: "))
    if user_input != 0:
        number = number + user_input
    else:
       print(number)
       break
