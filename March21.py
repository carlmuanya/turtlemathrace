import turtle
import random

#Create the race line
line = turtle.Turtle()
line.hideturtle()
line.penup()
line.goto(260,250)
line.pendown()
line.goto(260,-250)
turtle.done


#Create first turtle
firstplayer = turtle.Turtle()
firstplayer.shape('turtle')
firstplayer.color('blue')
firstplayer.penup()
firstplayer.goto(-280,-280)
firstplayer.pendown()

#Create Second Turtle
secondplayer = turtle.Turtle()
secondplayer.shape('circle')
secondplayer.color('red')
secondplayer.penup()
secondplayer.goto(-280,-0)
secondplayer.pendown()

#Create Second Turtle
thirdplayer = turtle.Turtle()
thirdplayer.shape('square')
thirdplayer.color('green')
thirdplayer.penup()
thirdplayer.goto(-280,280)
thirdplayer.pendown()

#Random Number Generator

numberone = random.randint(1,10)
numbertwo = random.randint(1,10)

numberone2 = random.randint(1,10)
numbertwo2 = random.randint(1,10)

numberone3 = random.randint(1,10)
numbertwo3 = random.randint(1,10)

#Variables to have the program stop
playeronecount = 0
playertwocount = 0
playerthreecount = 0

#Beginning of While loop
#Player 1
count = 0
while count < 20:
    randomnumber = random.randrange(1, 10)
    coin = 1 + (randomnumber % 3)
    if coin == 1:
        total = numberone + numbertwo
        answer1 = input(f"Player one, you have the luck of the coin. Answer the Question.\n What is the answer to " + str(numberone) + "+" + str(numbertwo) + "? ")
        if int(total) == int(answer1):
            firstplayer.forward(60)
            print(f"Very good, your answer is correct")
            print("---------------------------------------------------------------")
            playeronecount += 1
            if playeronecount == 9:
                print("Player one has one the game!")
                turtle.done()
        else:
            print("Nice try, but the correct answer is " + str(total))
            print("---------------------------------------------------------------")


#Player 2
    elif coin == 2:
        total2 = numberone2 + numbertwo2
        answer2 = input(f"Player two, you have the luck of the coin. Answer the Question.\n What is the answer to " + str(numberone2) + "+" + str(numbertwo2) + "? ")
        if int(total2) == int(answer2):
            secondplayer.forward(46)
            print(f"Very good, your answer is correct")
            print("---------------------------------------------------------------")
            playertwocount += 1
            if playertwocount == 9:
                print("Player two has one the game!")
                turtle.done()
        else:
            print("Nice try, but the correct answer is " + str(total2))
            print("---------------------------------------------------------------")

# Player 3
    elif coin == 3:
        total3 = numberone3 + numbertwo3
        answer3 = input(f"Player three, you have the luck of the coin. Answer the Question.\n What is the answer to " + str(numberone3) + "+" + str(numbertwo3) + "? ")
        if int(total3) == int(answer3):
            thirdplayer.forward(60)
            print(f"Very good, your answer is correct")
            print("---------------------------------------------------------------")
            playerthreecount += 1
            if playerthreecount == 9:
                print("Player three has one the game!")
                turtle.done()
        else:
            print("Nice try, but the correct answer is " + str(total3))
            print("---------------------------------------------------------------")
