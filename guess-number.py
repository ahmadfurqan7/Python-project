# Guess Number 🔢
# from number 0-10

guess = 0
tries = 0

while guess != 7 and tries < 3:
  guess = int(input('Guess the number:  '))
  tries = tries + 1

if guess != 7:
  print('You ran out of tries.')
else:
  print('You got it!')