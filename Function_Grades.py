def main():
    your_grade()


def your_grade():
    score = int(input("Enter your total score: "))
    if 400 <= score <= 500:
        print("Grade A")
    elif 300 <= score < 400:
        print("Grade B")
    elif 200 <= score < 300:
        print("Grade C")
    elif 100 <= score < 200:
        print("Grade D")
    else:
        print("You failed. Better luck next time.")


main()
