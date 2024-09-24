import random

#get ideas from https://www.reddit.com/r/DecidingToBeBetter/comments/v9c615/how_to_reward_yourself_without_food_or_shopping/

rewards = [
    "Get a meal at Mrs. Hen",
    "Get a meal at El Cocinero",
    "Get McGriddles",
    "Get some ice cream at the daily scoop at Bedok Reservoir",
    "Get a massage at a nearby massage place",
    "Light a scented candle",
    "Take a nice long bath",
    ]

question = input("What would you like to be rewarded today? (type 'exit' to quit): \n")
if question.lower() == 'exit':
    print ("Goodbye!")
    print ("Exiting program..")
else:
    print('Your reward for ' + question + ' is: ', random.choice(rewards))
    print ("Have a nice day!")
