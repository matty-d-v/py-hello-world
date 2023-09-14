# It may not seem obvious why you'd want to do this right now, but this is a really useful
# feature. At least understanding what's happening will be useful to know.

# A normal function that upper cases a some text, using a function of text, don't worry about 
# how this works, we'll come back to it.
def shout(text): 
    return text.upper() 
  
# A normal function that lower cases a some text, using a function of text, don't worry about 
# how this works, we'll come back to it.
def whisper(text): 
    return text.lower() 
  
# This is the next level on using functions. This function accepts a function as an argument
# and let's this function call/execute/invoke the function that was passed to it.
def greet(func, text):
    print(func(text))
  
# As the greet function to call the function shout with the text provdied.
greet(shout, "where are you Mike") 

# As the greet function to call the function whisper with the text provdied.
greet(whisper, "be CAReFUL, someone is watching us..") 