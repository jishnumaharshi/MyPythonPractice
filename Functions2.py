# def calculate_dog_years(age, initial_dog_years):
#     if age > 2:
#         age -= 2
#         age *= 4
#         age = (initial_dog_years * 2) + age
#     elif age == 2:
#         age *= initial_dog_years
#     elif age == 1:
#         age = initial_dog_years
#     return age
#
#
# def main():
#     first_dog_year = 10.5
#     human_age = int(input("Enter age in human years: "))
#     dog_age = calculate_dog_years(human_age, first_dog_year)
#     print(f"{human_age} years old human is {dog_age} years old in dog age ")
#
#
# main()
#

# import random

# print(random.randint(5, 11*10))


# def main():
#     x = do_something(3)
#     y = do_something(x)
#     print(x+y)
#
#
# def do_something(a):
#     x = a - 1
#     b = a * 2
#     return b
#
#
# main()
#


def main():
    age = get_age()
    print(f"at {age}, you are half way to {age * 2}")


def get_age():
    x = int(input("Age: "))
    return x


main()


