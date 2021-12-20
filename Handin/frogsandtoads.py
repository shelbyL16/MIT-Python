#Ask the user for frogs
frogs = input("Enter the number of frogs:\n")

#Ask the user for toads
toads = input("Enter the number of toads:\n")

#set up the puzzle
state = ['Frog']*int(frogs)+['']+['Toad']*int(toads)

#set up win
state_win = ['Toad']*int(toads)+['']+['Frog']*int(frogs)

#set count and com to 0 and empty strings
count=0
move=True

#print the positions
for i in state:
    count=count+1
    print('{:>3d}'.format((count)),end=".")
print()

#print the animals in the positions for the game
for i in state:
    if len(i)==0:
        print("    ",end="")
    else:   
        print('{:>4}'.format((i)),end="")

#take the input for the first move
com = input("\n>")
#continue doing this while the user hasnt quit the program
while com!="quit":
    count=0
    move = False #move hasnt happened yet
    length=len(state)-1
    pos=int(com)  #pos
    
   

    #PYTHON DOES THAT ANNOYING THING WHEN IT STARTS AT 0 
    
    #get the animal at the python position
    animal=state[pos-1]
    #print("Got the animal")
    
    #if the animal selected is a toad
    if animal=='Toad':
        #print("Got that the animal was a toad")
        
        #check to see if it is a one move with the space in front
        if state[0]=="" and move == False and state[pos]!="Frog": 
            #print("i am in the toad section and the space in the front")
            #swap around
            state[pos-1]="Toad"
            state[pos]=''
            #it is defintely changing it to the right things
            move = True #move is true
        #print("not a space in front")
            
        #check to see it is a leap over another
        if state[pos-2]=="Frog" and move==False and state[pos-2]!='' or state[pos-2]=="Toad" and move == False and state[pos-2]!='': 
            #print("am i in the toad section - it is a leap")
            #swap
            state[pos-3]="Toad"
            state[pos-1]=''
            #print("I have moved it")
            move = True #move is true                 
        #print("not a leap")
        
        #check to see it is a one move where the space is not at the front
        if state[length]!='' and move==False and state[pos-2]=="" or state[0]=='' and move==False and state[pos-2]=='': 
            #print("am i in the toad section - it is a spave move - 1")
            #swap
            state[pos-2]="Toad"
            state[pos-1]=''
            #print("I have moved it")
            move = True  #move is true    
        #print("one move")       

        
    #If the animal selected is a frog
    #PYTHON DOES THAT ANNOYING THING WHEN IT STARTS AT 0        
    #if the animal selected is a frog
    if animal=='Frog':
        #print("Got that the animal was a Frog")
        
        #check to see if it is a one move with the space in end
        if state[length]=="" and move == False and state[pos]!="Toad": 
            #print("i am in the frog section and the space in the back")
            #sswap
            state[length-1]="Frog"
            state[length-2]=''
            #it is defintely changing it to the right things
            move = True #move is true
            
            
        #check to see it is a leap over
        if state[pos-2]=="Frog" and move==False and state[pos]!='' or state[pos-2]=="Toad" and move==False and state[pos]!='': 
            #print("am i in the frog section - it is a leap over")
            #swap
            state[pos+1]="Frog"
            state[pos-1]=''
            #print("I have moved it")
            move = True   #move is true               
        
        
        #check to see it is a one move where the space is not at the front or end
        if state[length]!='' and move==False and state[pos]=="" or state[0]=='' and move==False and state[pos]=='': 
            #print("am i in the frog section - it is a space move - 1")
            #swap
            state[pos]="Frog"
            state[pos-1]=''
            #print("I have moved it")
            move = True  #move is true
        
    #if it has been moved and the pos at the front is a space
    if state[length]=="" and move==True or state[0]=="" and  move==True:
        for i in range (0,length):
            if state[i]=="Toad" and state[i+1]=="Frog" or state[i]=="Frog" and state[i+1]=="Toad":
                move=True
                #there are no more moves to make then it is gridlocked
            if state[i]=="Toad" and state[i+1]=="Toad" or state[i]=="Frog" and state[i+1]=="Frog":
                move=False#change move back to false to say lost and end the game

        
    
    #print the positions
    for i in state:
        count=count+1
        print('{:>3d}'.format((count)),end=".")
    print()
    
    #print the animals in the positions for the game
    for i in state:
        if len(i)==0:
            print("    ",end="")
        else:   
            print('{:>4}'.format((i)),end="")
    
    #If the player has won the game
    if state == state_win:
        print("\nCongratulations, you've won!") 
        break
    #if the player lost the game
    if move==False:
        print("\nSorry, you've lost.")
        break  
    #ask again for input
    com = input("\n>")