#ce program represent une simulation d'un log in 
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
  print("Unaccessible.")
elif age >= 17:
  print("approved. welcome: " + name )
#Debut de L'application.
input("what can we do for you today?: ")
print("Loading.....")