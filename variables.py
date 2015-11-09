# Variables.py
# Temperature converter
# Eirik Hansen Rynning - Noroff 2015

temp_type = input("Which type temperature type do you want to convert from? Please enter C or F: ")

if temp_type == "C":
    #print("It is C")                #Used to check functionality
    temp_input = input("Enter the temperature in Celcius as an integreter (default value: 20): ")
    if temp_input == "":
        temp_input = 20
    print (temp_input, "degrees in Celsius, converts to ", 9/5 * int(temp_input) +32, "degrees Fahrenheit")
elif temp_type == "F":
    #print("It's actually F")        #Used to check functionality
    temp_input = input("Enter the temperature in Fahrenheit as an integreter (default value: 85): ")
    if temp_input == "":
        temp_input = 85
    print(temp_input, "degrees in Fahrenheit, converts to ", 5/9 * (int(temp_input) -32), "degrees Celcius")
else:
    #print("It is not C or F")            #Used to check functionality
    print("You specified ", temp_type, "as the type of temperature.")
    print("The temperature type is invalid.")
    print("Please keep in mind that the only allowed inputs are C or F. (CaSe-SenSiTivE!)")