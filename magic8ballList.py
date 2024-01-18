import random

while True:
    print("What is your question?" + "\n")
    question = input()

    messages = [
        "It's okay dude, you can do this",
        "Think about it for 5 minutes",
        "Yes, do it",
        "Definitely not",
        "Write it down first",
        "Think about destiny"
        ]

    # question = input()

    # print("your answer to " + question + "is " + random.choice(messages))
    print ("The 8-Ball says, " + random.choice(messages) + "\n")
    break

while True:
    for i in range(0, 3):
        print("Next question?")
        question = input()
        print ("The 8-Ball says, " + random.choice(messages) + "\n")
        continue
    else:
        print("Have a nice day")
        break
