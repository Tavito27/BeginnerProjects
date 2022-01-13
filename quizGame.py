import random 
import pprint
print("Hello! Welcome to the quiz")

playing = input("Would you like to take the quiz?: ")
print("\n")

while (playing.lower() != "yes" and playing.lower() != "no"):
    print("Please enter a valid response ('yes' or 'no')")
    playing = input("Would you like to take the quiz?: ")
    print("\n")

if playing.lower() != "yes":
    print("LATER!\n")
    quit()
print("Alright! Lets start:")

#Create the questions for the quiz

questions_and_answers = {'What is the largest kind of bear?: ':'A polar bear', 
                         'What do you call a baby frog?: ': 'A tadpole', 
                         'What do you call a group of horses?: ': 'A herd', 
                         'What do you call a group of dolphins or whales?: ': 'A pod', 
                         'What animal is Timone in “The Lion King"?: ': 'A meerkat', 
                         'How many legs does an octopus have?: ': '8', 
                         'What food do pandas eat? : ': 'Bamboo', 
                         'What do you call a baby bear?: ': 'A cub', 
                         'Where can you find a cactus?: ': 'The desert', 
                         'What planet is closest to the sun?: ': 'Mercury'
}

#find the total number of qestions stored
totalQuestions = len(questions_and_answers)
#Correct answer tracker
correctAnswers = 0
#convert Dictionary into a list for random selection 
dictionaryList = list(questions_and_answers)

for x in range(1,totalQuestions+1): 
    question = random.choice(dictionaryList)
    dictionaryList.remove(question)
    

    answer = input(question)
    if answer.lower() == questions_and_answers[question].lower(): 
        correctAnswers += 1
        print("Correct!!")
    else: 
        print("That is not correct :( ")
    print("\n")



print("Total number correct: %d / %d" % (correctAnswers, totalQuestions) )
print("You scored a " + str((correctAnswers/totalQuestions)*100) + "\n")