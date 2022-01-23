import random

# TODO: Implement the Hilo class as follows...
class Card:

    
# 1) Add the class declaration. Use the following class comment.
    """Random Cards valued between 1 and 13

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.points = 300
        self.won=100
        self.loose=75
        self.card=0
        self.next_card=0    

# 3) Create the random(self) method. Use the following method comment.
    """Generates a new random value and calculates the points.
        
    Args:
        self (Card): An instance of Card.
    """
    def play(self):
        self.card = random.randint(1, 3)
        # Group of if statements to check the dice numbers according to the requirements. 
        print(f"The card is: {self.card}")
        choice = input("The number will be higher or lower? h/l ")
        self.next_card = random.randint(4,13)
        print(f"Next card was: {self.next_card}")
        if self.card>self.next_card and choice.lower()=="l" or self.next_card>self.card and choice.lower()=="h":
            self.points +=self.won
            print(f"This is the right answer")
            print(f"Your score is:{self.points}")
        else:
            self.points-=self.loose
            print(f"This is the Wrong answer")
            print(f"Your score is:{self.points}")   




    


