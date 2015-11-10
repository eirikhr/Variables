"""
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
"""
# Productivity Alarm
import time
import webbrowser
music_video = str(input("Paste link to media that will autoplay in your webbrowser upon activation"))
total_breaks = int(input("How many times will the media run?"))
s = int(input("How often in seconds?"))
break_count = 0
while int(break_count) < total_breaks:
    time.sleep(s)
    webbrowser.open(music_video)
    break_count += 1                            #Instead of break_count = break_count + 1