#pitamo korisnika kako se zove
print("HELLO CONTESTANT!!")

def name():
    name = input("what is your name? ")
    print("hello," ,name)
    intro()

 
#neki lagani uvod
def intro():
    ready = input("This is a game of wits, are you ready?? (yes/no) ")
    if ready.lower() == "yes":
        print("So, you chose to continue...")
        begin()
    elif ready.lower() == "no":
        print("ha! You pussy!!")
        print("come back when you grow a pair!")
    else:
        print("invalid input type yes or no! idiot...")
        intro()

#postavimo pitanja

def begin():
    score = 0
    c = "correct"
    f = "wrong, muthafucka"
    print("here comes the first question.")
    question = input("What is the capital of Croatia? ")
    if question.lower() == "zagreb":
        print(c)
        score += 1
    else:
        print(f)

    print("second question.")
    question = input("Where do swallows fly in the winter? ")
    if question.lower() == "south":
        print(c)
        score += 1
    else:
        print(f)
    
    print("third question.")
    question = input("What's the capital of Finland? ")
    if question.lower() == "helsinki":
        print(c)
        score += 1
    else:
        print(f)

    print("fourth question.")
    question = input("Which Austrian painter didn't get the recognition he deserved? ")
    if question.lower() == "hitler":
        print(c)
        score += 1
    elif question.lower() == "adolf hitler":
        print(c)
        score += 1
    else:
        print(f)

    print("fifth and final question")
    question = input("From what grain is Japanese spirit sake maid? ")
    if question.lower() == "rice":
        print(c)
        score += 1
    else:
        print(f)

    print("you got " + str(score) + " correct answers!")
     
#ocijenimo test




name()
