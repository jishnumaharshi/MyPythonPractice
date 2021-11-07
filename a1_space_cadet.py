# CP5639 2020-1 Assignment 1
# Program 2 - Space Cadet Results
# Student Name: Jishnu Maharshi Yalamarthi
# Date Started: 09 - April - 2020


# Psuedocode
#   Get input of the cadet's practical score
#   Get input of the cadet's exam score
#   if the cadet's both exam and practical scores are individually less than 50
#       Add both exam and practical scores of cadets to total score
#       if the Cadet's total score is greater than 50
#           if the Cadet's exam score is greater than practical score
#               Print Cadet's score and Print they will become desk officer
#               if the cadet's total score is greater than 90
#                   Print they made it to the Honour roll
#           else if the Cadet's practical score is greater than exam score
#               print Cadet's score and print they will become a field agent
#               if the Cadet's total score is greater than 90
#                   Print they made it to the Honour roll
#       else
#           print the Cadet score
#           print the Cadet has failed and suggest to try next year.

# CODE
print("Welcome Trainee Space Cadet. How did you do?")
cadet_practical_score = int(input("Practical Score (0-50): "))
cadet_exam_score = int(input("Exam score (0-50): "))
if cadet_exam_score <= 50 and cadet_practical_score <= 50:
    cadet_total_score = cadet_practical_score + cadet_exam_score
    if cadet_total_score > 50:
        if cadet_exam_score > cadet_practical_score:
            print("Your total score is: ", cadet_total_score, "out of 100")
            print('You will become a desk officer')
            if cadet_total_score >= 90:
                print("Congratulations on making the honour roll!")
        elif cadet_practical_score > cadet_exam_score:
            print("Your total score is: ", cadet_total_score, "out of 100")
            print("You will become a field agent")
            if cadet_total_score >= 90:
                print("Congratulations on making the honour roll!")
    else:
        print("Your total score is: ", cadet_total_score, "out of 100")
        print("You failed, Please try again next year.")
print("You have entered incorrect scores. Please try again.")