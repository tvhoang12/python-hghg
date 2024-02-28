#-----------------------
from json import load
from urllib import response


def newGame():
    guesse = []
    correct = 0
    question_num = 1
    
    for key in question:
        print("-----------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter your answer: ")
        guesse.append(guess)
        
        correct += loadGame(question.get(key), guess)
        question_num += 1
        
    showScore(correct, guesse)
    playAgain()
#-----------------------
def loadGame(answer, guess):
    if answer == guess:
        print("correct!")
        return 1
    else:
       print("incorrect!")
       return 0 
#-----------------------
def showScore(correct, answers):
    print("-----------------------")
    your_score = correct / len(question) * 100
    print("Your score is: " + str(your_score) + "%")
    print("-----------------------")
#-----------------------
def playAgain():
    response  = input("Do you want to play again? (y/n): ")
    
    if response == "y":
        newGame()
    elif response == "n":
        print("Goodbye!")
#-----------------------


question = {
    "What is the capital of France?\n": "Paris",
    "What is the capital of Germany?\n": "Berlin",
    "What is the capital of Italy?\n": "Rome",
"What is the capital of Spain?\n": "Madrid",
    "What is the capital of the United Kingdom?\n": "London",
    "What is the capital of the United States?\n": "Washington D.C.",
    "What is the capital of Canada?\n": "Ottawa",
    "What is the capital of Mexico?\n": "Mexico City",
    "What is the capital of Brazil?\n": "Brasilia",
    "What is the capital of Argentina?\n": "Buenos Aires",
}

options = [
    ["Paris", "London", "Berlin", "Rome"],
    ["Berlin", "Paris", "London", "Rome"],
    ["Rome", "Berlin", "Paris", "London"],
    ["Madrid", "Paris", "London", "Berlin"],
    ["London", "Paris", "Berlin", "Rome"],
    ["Washington D.C.", "New York", "Los Angeles", "Chicago"],
    ["Ottawa", "Toronto", "Vancouver", "Montreal"],
    ["Mexico City", "Guadalajara", "Monterrey", "Puebla"],
    ["Brasilia", "Rio de Janeiro", "Sao Paulo", "Salvador"],
    ["Buenos Aires", "Cordoba", "Rosario", "Mendoza"]
]

newGame()