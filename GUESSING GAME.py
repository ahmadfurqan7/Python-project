"""
BUILD GUESSING GAME
THAT GIVE THE USER 3 TRIES
TO GUESS A NUMBER
BETREEN 1 AND 10
"""

#START

secret_number = 8
#u can change anytime
guess=0
tries=0

while tries<3 and guess != secret_number:
    guess=int(input("Guess the number between 1 and 10 :"))
    tries=tries+1

if guess==secret_number:
    print("RIGHT NUMBER!!, COONGRATSS")
else:
    print("LOSER :p")


#THATSS IT :)