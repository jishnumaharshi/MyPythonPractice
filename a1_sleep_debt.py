# CP5639 2020-1 Assignment 1
# Program 3 - Sleep Debt Calculator
# Student Name: Jishnu Maharshi Yalamarthi
# Date Started: 09 - April - 2020


# Pseudo code
# Set the number of workdays to 5
# Declare the total sleep hours and Ideal sleep hours variables
# for each day in the week
#   get the hours slept on the day
#   Until the hours are not less than zero and not greater than 24
#       prompt input as invalid hours
#       get the hours slept on that day
#   Add all the hours slept on each day
#   Calculate the recommended hours of sleep with respect to how many days slept and hours of ideal sleep time each day
#   if the sleep time is well over recommended
#       print "You're getting enough sleep, Keep it up!" and print the total debt
#   else
#       print the total sleep debt and total hours of sleep


# CODE
print("Sleep Debt Calculator")
number_of_work_days = 5  # number of work days that can be changed later
total_sleep_hours = 0
ideal_sleep_hours = 8
for day in range(number_of_work_days):  # using loop for iteration on days
    sleep_hours_in_a_day = float(input("Night {} hours of sleep: ".format(day + 1)))  # Obtaining input of sleep hours in a day
    while sleep_hours_in_a_day <= 0 or sleep_hours_in_a_day >= 24:  # Using while for checking invalid input
        print("Invalid number of hours")
        sleep_hours_in_a_day = float(input("Night {} hours of sleep: ".format(day + 1)))
    total_sleep_hours = float(
        total_sleep_hours + sleep_hours_in_a_day)  # Calculating total sleep hours over the count of days
recommended_hours_of_sleep = number_of_work_days * ideal_sleep_hours  # Calculating recommended hours of sleep
print("Recommended total sleep is: ", recommended_hours_of_sleep)
if total_sleep_hours >= recommended_hours_of_sleep:
    print("Your total hours of sleep:", total_sleep_hours)
    print("You're getting enough sleep, Keep it up!")
else:
    print("Your total hours of sleep: ", total_sleep_hours)
    print("Your sleep debt over this time is: ", recommended_hours_of_sleep - total_sleep_hours)
