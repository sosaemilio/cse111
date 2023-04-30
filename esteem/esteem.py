from ctypes import pointer
from operator import neg


def main():
    print("""This program is an implementation of the Rosenberg
    Self-Esteem Scale. This program will show you ten
    statements that you could possibly apply to yourself.
    Please rate how much you agree with each of the
    statements by responding with one of these four letters:

    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.""")

    questions = ["1. I feel that I am a person of worth, at least on an equal plane with others.", 
                 "2. I feel that I have a number of good qualities.",
                 "3. All in all, I am inclined to feel that I am a failure.",
                 "4. I am able to do things as well as most other people.",
                 "5. I feel I do not have much to be proud of.",
                 "I take a positive attitude toward myself.",
                 "On the whole, I am satisfied with myself.",
                 "I wish I could have more respect for myself.",
                 "I certainly feel useless at times.",
                 "At times I think I am no good at all."]

    global_score = 0
    for question in range(0,10):
        print(questions[question])
        score = str(input("Enter D, d, a, or A:"))
        if question == 0 or question == 1 or question == 3 or question == 5 or question == 6:
            global_score += positive_question(score)
        elif question == 2 or question == 4 or question ==  7 or question == 8 or question == 9:
            global_score += negative_question(score)

    print(f"Your score is {global_score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

def positive_question(score):
    positive_score = 0
    if score == "D":
        positive_score = 0
    elif score == "d":
        positive_score = 1
    elif score == "a":
        positive_score = 2
    elif score == "A":
        positive_score = 3
    return positive_score


def negative_question(score):
    negative_score = 0
    if score == "D":
        negative_score = 3
    elif score == "d":
        negative_score = 2
    elif score == "a":
        negative_score = 1
    elif score == "A":
        negative_score = 3
    return negative_score



if __name__ == "__main__":
    main()