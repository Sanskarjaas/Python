question_set=[
    {
        "Question":"what is your name ?",
        "Options":["A. Sanskar","B. Rohan","C. Akshay","D. Roshit"],
        "Answer":"b"
    },
    {
        "Question":"How old are you ?",
        "Options":["A. 18","B. 16","C. 26","D.69"],
        "Answer":"c"
    }
    ]

# print("Student Enrollement")
# studentname=input("Enter your Name ? ")
# studentId=input("Enter your Student Id  ? ")
# print(f"\nWelcome {studentname}! Let the Exam Begin. Best of Luck!\n")
# print("Let the Exam Begins Best Of Luck!!!")

score=0

for q in question_set:
    print("\n"+q["Question"])
    for options in q["Options"]:
        print(options)
    while True:
        answer=input("Choose your correct options: ").lower()
        valid_options = {"a", "b", "c", "d"}
        if answer in valid_options:
            break
        else:
            print("Invalid Input")
    if answer == q["Answer"]:
        print("correct ! Awesome Keep Going")
        score+=1
    else:
        print("Wrong Answer !! , Try to guess hard")
print("Your Score is "+score)



#question_options=list(question_set[0].keys())[1]
#question_options_value=question_set[0][question_options]
#print(question_options)
#print(question_options_value)



# question_answer =list(question_set[0].keys())[2]
# question_answer_value=question_set[0][question_answer]
# print(question_answer)
# print(question_answer_value)


# answer=input("Choose your correct options: ")
# valid_options = {"A", "B", "C", "D", "a", "b", "c", "d"}
# if answer.upper() not in valid_options:
#    print("Invalid Input")

# else:
#     if answer == question_answer_value.upper() or answer==question_answer_value.lower():
#         print(answer)
#     else:
#         print("Wrong Answer")