#WORD GUESSING GAME

import random
words=['apple','oracle','amazon','microsoft','orange','cat','dog']
guessed_word=random.choice(words)

hint=guessed_word[0]+"and"+guessed_word[-1]
store_g_1=[]
try_p=5

a=input("Enter your name : ")
print("Welcome to Word Guessing Game")
print("We are only gave you 5 attempt")

for guess in range(try_p):
    while True:
        letter=input("Guess the letter : ")
        if len(letter) == 1:
            break
        else:
            print("Oops! please guess a letter")

    if letter in guessed_word:
        print("Yes!")
        store_g_1.append(letter)
    else:
        print("No!")

    if guess == 3:
        print()
        clue_request=input("Would you like a clue? ")
        if clue_request.lower().startswith('y'):
            print()
            print("Clue : The first and last letter of the word is: ",hint)
        else:
            print("You're very confident!")

print()
print("Now, lets se what have you guessed so far. You have guessed : ",len(store_g_1),"Letter correctly.")
print("These letter are : ", store_g_1)

word_guess=input("Guess the whole word : ")
if word_guess.lower() == guessed_word:
    print("====================================================")
    print("Congrats you are correct!! thanks for playing "+a+" :)")
    print("====================================================")

else:
    print("====================================================")
    print("Sorry, the answer was : "+guessed_word+" :(")
    print("====================================================")

print()
print("Please enter to leave the program")
