#function definition
def greeting(name): #(4) since we called that function, we now go to that function. now the name parameter is assigned to the passed in value of input name, which was Mike. 
    print('Hello', name) #(5)Then we go to the first line of the function which prints ('Hello', and the 'name' variable) so we see Hello Mike printed to the screen.   
#main program    
input_name = input('Enter your name:\n') #(1)the 1st line of code that isn't in a function definition is where the program starts, so Enter your name is printed to the screen. 
#(2)Then the user enters a name, which is saved to the input name variable. 
greeting(input_name) #(3)then we go to the next line of the program, which is a call to the greeting()function, and the value of the input name is passed in.  
#(6)so becuase line 8 has no more text, this will end the program, so the program stops executing.

