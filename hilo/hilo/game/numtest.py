import random


points = 300
won=100
lose=75
c = ""


while c.lower() !="n":
    
    num1 = random.randint(1,13)
    

    print(f"num 1: {num1}")
    choice = input("The number will be higher or lower? h/l ")

    num2 = random.randint(1,13)
    print(f"num 2: {num2}")
    if num1>num2 and choice.lower()=="l" or num2>num1 and choice.lower()=="h":
        print(f"This is the right answer")
        points +=won
        print(f"Your score is:{points}")
    else:
        print(f"This is the wrong answer")
        points-=lose 
        print(f"Your score is:{points}")

    if points<=0:
        print("Game Over!")
        break
    c = input("play? y / n ")
