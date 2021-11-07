# CP5639 2020-1 Assignment 1
# Program 1 - Pay Calculator
# Student Name: Jishnu Maharshi Yalamarthi
# Date Started: 09 - April - 2020

# Pseudo code
#   Set the base pay at experience level zero to 100
#   Get the number of hours worked.
#   Get the experience level.
#   Calculate the base pay according to the experience level: hourly_pay_rate = base_pay + (experience * 5)
#   Calculate the total pay: number of hours worked * hourly_pay_rate
#   Print the hourly pay rate
#   Print the total pay

# CODE
print("Experience Counts Pay Calculator")
base_pay_at_level_zero = 100.0  # Setting the base pay
number_of_hours_worked = int(input("Number of hours worked: "))
experience_level = int(input("Experience level: "))
hourly_pay_rate = base_pay_at_level_zero + (experience_level * 5)  # Calculating hourly pay rate according to experience
total_pay = float(number_of_hours_worked * hourly_pay_rate)  # Calculating total pay
print("Based on your experience level (", experience_level, ") :")
print("Your hourly pay rate is: ${:.2f}" .format(hourly_pay_rate))
print("Your total pay is: ${:.2f}".format(total_pay))
