#Greet the user
print("Hello, I am Eugene Junior.")

#Ask the user for their name and save input
first_name = input("What is your first name? \n")

#Ask the user for their last name and save input
last_name = input("What is your last name? \n")

#create intials from 0 pos
name=first_name[0]+"."+last_name[0]+"."+"!"

#greet the user
print("Hi "+name)

#Ask the user for the year save input
year = input("What year is this? \n")

#Ask the user for their age save input
age = input("What age are you? \n")

#Take the year and minus age to get year
birth_year=0
birth_year=int(year)-int(age)

#minus one for the before year
temp=birth_year-1


#Convert to string for subset
birth_year=str(birth_year)
temp=str(temp)

#Convert to string for print
year=temp+"/"+birth_year[2:4]

#print the answer
print("Okay, so you were born in "+ year + ".")

#ask how tall the user is
meters=float(input("How tall are you (metres)? \n"))

#Convert to inches and feet
meters_in_ft = round(meters // .3048)
meters_in_in = round(meters / .3048 % 1 * 12)
ans=str(meters_in_ft)+"'"+str(meters_in_in)+'"!'

#print the height in inches
print("That's "+ans)

#starwars name
print("I'm going to tell you your Star Wars name.")

#Ask the user for their moms name save input
mom_name = input("What's your mother's first name?\n")

#Ask the user for their city save input
city = input("What's the name of the city nearest to your place of birth?\n")

#calc star wars name
star_wars=last_name[0:3]+first_name[0:2]+" "+mom_name[-2::]+city[-3::]

#convert to lower case and upper case
star_wars=star_wars.lower()
star_wars=star_wars.title()

#convert first letter to upper

#give the user their last name
print("Your Star Wars name is "+star_wars + ".")


