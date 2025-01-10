#Matthew Kim
#1/8/2025
#Multiplication Quiz
import random
correct = 0
rounds = 0

def quiz ():
    global correct
    global rounds

    print("Welcome to your Multiplication Quiz")
    difficulty = input("Enter difficulty: easy, medium, hard")

    if difficulty == "easy":
        q = int(input("How many questions do you want?"))
        #changes how many questions in the for loop
        for i in range (q):
            num1 = random.randint(1,5)
            num2 = random.randint(1,5)
            answer = int(input("What is " + str(num1) +" times "+ str(num2) + " ?" ))
            if answer == (num1*num2):
                print("True")
                correct = correct + 1
                rounds = rounds + 1
            else:
                print("False")
                rounds = rounds + 1
            print (str(correct) + " / " + str(rounds))
            #correct rounds/ total rounds


    if difficulty == "medium":
        q = int(input("How many questions do you want?"))
        for i in range (q):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            answer = int(input("What is " + str(num1) +" times "+ str(num2) + " ?" ))
            if answer == (num1*num2):
                print("True")
                correct = correct + 1
                rounds = rounds + 1
            else:
                print("False")
                rounds = rounds + 1
            print (str(correct) + " / " + str(rounds))

    if difficulty == "hard":
        q = int(input("How many questions do you want?"))
        for i in range (q):
            num1 = random.randint(1,20)
            num2 = random.randint(1,20)
            answer = int(input("What is " + str(num1) +" times "+ str(num2) + " ?" ))
            if answer == (num1*num2):
                print("True")
                correct = correct + 1
                rounds = rounds + 1
            else:
                print("False")
                rounds = rounds + 1
            print (str(correct) + " / " + str(rounds))

quiz()








