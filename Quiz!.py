#dictionary of quesion and answers
#have a variable that tracks the score
#loop thru the dictionary using the key value pairs
#display ques and input answer
#tell them if they r right or not
#show result


quiz = {
    "question1": {"question": "What is the capital of France?",
                 "answer": "Paris"},
    "question2": {"question": "What is the capital of germany?",
                 "answer": "Berlin"},
    "question3": {"question": "what is the capital of India?",
                   "answer": "New Delhi"},
    "question4": {"question": "what is the capital of Italy?",
                   "answer": "Rome"},
    "question5": {"question": "what is the capital of bangladesh?",
                   "answer": "Dhaka"},
    "question6": {"question": "what is the capital of russia?",
                   "answer": "Moscow"},
    "question7": {"question": "what is the capital of portugal?",
                   "answer": "Lisbon"},
    }
score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? : ")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score += 1
        print("Your score is : " + str(score))
        print("")
        print("")

    else:
        print("Wrong")
        print("The answer is " + value['answer'])
        print("Yon ur score is : " + str(score))
        print("")
        print("")

print("Your score is " + str(score) + " out of 7 questions")
print("Your percentage is " + str(int(score/7*100)) + "%")