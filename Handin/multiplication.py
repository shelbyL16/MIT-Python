#Ask the user for input n
n = input("Enter a value for n (not greater than 20):\n")

#check if digit
if (n.isdigit()==True):
  
  #check if in range
  n = int(n)
  if (0<n<=20):
    #convert to n to add 10
    n=int(n)
    n_to = n+10
    
    #convert back to string to put in answer
    n=str(n)
    n_to = str(n_to)
    
    #return the answer
    print("Table from " + n + " to " + n_to + ":")
    
    #convert back to int for multiplication table
    n=int(n)
    n_to = int(n_to)
    #this is the header of the table
    star='*'
    line = '|'
    print(star, end=' ')
    print('{:>2}'.format(line),end=' ')
    for i in range(n, n_to):
      print('{:>3d}'.format(i),end=" ")
    print()
    print("--------------------------------------------")
    
    #calculate the multiplication table of 10 with the appropriate format
    for i in range (n,n_to):
      print('{:<2d}'.format(i),end=" | ")
      for j in range (n,n_to):
        print('{:>3d}'.format(i*j),end=" ")
      print()
  #an integer but not in the range 
  else:
    print("Sorry, n must be an integer number in the range 1 to 20.")
    
#does not satisfy arguments
else:
  print("Sorry, n must be an integer number in the range 1 to 20.")