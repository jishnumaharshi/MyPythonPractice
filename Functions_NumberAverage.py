def main():
    age = get_age()
    average = get_average(age)
    print(f"The average is: {average}")


def get_age():
    age = int(input("Your age: "))
    while age < 0 or age > 120:
        print("Invalid age:")
        age = int(input("Your age:"))
    return age


def get_average(age):
    average = (7 + age) / 2
    return average


main()