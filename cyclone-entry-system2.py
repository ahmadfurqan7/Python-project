# The Cyclone 🎢
'''They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits)
and need your help writing the program for it!'''

ride_is_open = True

height = int(input('What is your height (cm)? '))
credits = int(input('How many credits do you have? '))

tall_enough = height >= 137
enough_credits = credits >= 10

if ride_is_open and tall_enough and enough_credits:
  print("Enjoy the ride!")
elif not tall_enough or not enough_credits:
  print("You are either not tall enough to ride or you don't have enough credits.")
else:
  print("Sorry! The ride is currently closed!")