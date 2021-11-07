def main():
    name = input("Your name?: ")
    print_count = int(input("How many times?: "))
    greetings(name, print_count)


def greetings(name, print_count):
    for count in range(print_count):
        print(name, end=' ')


main()
