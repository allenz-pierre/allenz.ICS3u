# 
#Allenz Alberson Pierre
#4 dec. 2020

#Demander Le nom
name = input("What is your name?: ")
print("hello:" + name)

#Validation de l'age
print("I will now see if you are allowed into the net.")
birth_year = input("Enter your birth year: ")
age = 2020 - int(birth_year)
print(age)
#Acceptation si l'age est plus que 17.
if age < 17:
  print("access denied.")
elif age >= 17:
  print("approved. welcome: " + name )
#Debut de L'application.
  input("what can we do for you today?: ")
  print("Loading.....")
joke = input("in the mean time, would you like to hear a joke?:")
if joke == "no":
  print("well we're still processing so you don't have a choice.")
elif joke == "yes":
  print("okay, one moment.")
number = input("please insert a number from 1 to 3: ")
if number == "1":
  print("What do you call an Alligator in a vest?")
  print(" AN INVESTIGATOR!!!!!")
elif number == "2":
  print("why was 8 so afraid of 7")
  number = input("BECAUSE 7 8 9")
elif number == "3":
  print("what the you call a book club that has been stuck on the same book for years")
  print(" A CHURCH!!!")
answer = input("we have finished processing, would you like to be redirected to your search?: ")
if answer == "yes": 
  print("okay good because we ran out of jokes.")
elif answer == "no": 
  print("too bad, we ran out of jokes. Anyways go find what you we're looking for.")
print("redirecting.")
