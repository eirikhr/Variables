# FizzBuzz.py
# Flexible Variables
# Eirik Hansen Rynning - Noroff 2015
import time

print("Good evening. Welcome to the famous FizzBuzz application!")
print("Find the FizzBuzz number to win the GRAND PRIZE")
user_input = input("Please enter a positive integreter: ")
#print("Debug: The variable is an integreter: ", isinstance(user_input, int))
#print("Debug: The user input is: ", user_input)
time.sleep(1)
print("Will", user_input, "be the winning number???")
time.sleep(1)
print("Lets see then.")
time.sleep(.2)
print(".......")
time.sleep(.2)
print(".......")
time.sleep(.2)
print(".......")
time.sleep(.2)
print(".......")
time.sleep(.2)
print(".......")
time.sleep(.2)
print(".......")
time.sleep(.2)
print(".......")
time.sleep(.2)
print(".......")
time.sleep(1)

if int(user_input) % 3 == 0 and int(user_input) % 5 == 0:
    print("FizzBuzz!!!!!!!!!! WINNER DING DING DING DING DING DING DING *casino sounds*")
elif int(user_input) % 3 == 0:
    print("Fizz! Winner!")
elif int(user_input) % 5 == 0:
    print("Buzz! Buzzer-winner!")
else:
    print("Sorry, love. Your number isn't Fizz, or Buzz. Buzz off, please!")
