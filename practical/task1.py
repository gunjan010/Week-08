# 
# File: task1.py
# Author: Gunjan Rajak
# Student Id: a3183498
# Description: aa class
# This is my own work as defined by the College's
# Academic Integrity Policy
#  

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
count = 0
dayCounter = 0
for days in week:
    for letter in days:
        count += 1
    dayCounter += 1
average = count / dayCounter
print("Average length of letters: ", average)
