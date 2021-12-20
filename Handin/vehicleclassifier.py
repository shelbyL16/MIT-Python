#Ask the user for their vehicle weight
weight = input("What is the gross vehicle mass (in kg)? \n")

#Ask the user for their trailer
trailer = input("Does the vehicle have a trailer? \n")

#create variables and convert input to int
ans=0
class_=""
weight=int(weight)

if (trailer=='y'):
    #Ask the user for their trailer weight    
    trailer_weight = input("What is the gross vehicle mass of the trailer (in kg)?\n")
    trailer_weight = int(trailer_weight)
    
    #check trailer weight, if greater than 750 then special class E
    if (trailer_weight>750):
        ans =int(weight)
        #calculate the class weight    
        if (ans<=3500):
            class_="EB"
        
        if (3500<ans<=16000):
            class_="EC1"
            
        if (ans>16000):
            class_="EC"
            
    #check trailer weight, if less than 750 not a special class E   
    else:
        ans = int(weight)
        #calculate the class weight    
        if (ans<=3500):
            class_="B"
        
        if (3500<ans<=16000):
            class_="C1"
            
        if (ans>16000):
            class_="C"        

#if no trailer, ask if it articulated    
else:
    ans=int(weight)
    articulated = input("Is the vehicle articulated?\n")
    #if yes then there is a special class E
    if (articulated == 'y'):
        if (ans<=3500):
            class_="EB"
        
        if (3500<ans<=16000):
            class_="EC1"
            
        if (ans>16000):
            class_="EC"     
    
    #if no then it does not belong to special class
    if (articulated=='n'):
        ans=int(weight)
        if (ans<=3500):
            class_="B"
        
        if (3500<ans<=16000):
            class_="C1"
            
        if (ans>16000):
            class_="C"  

#print the class of the vehicle
print("This vehicle is class " + class_ +".")