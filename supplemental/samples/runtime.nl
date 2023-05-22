
# nolout() is now a built-in function that takes one argument and prints it
nolout('hi??')

# nolin() is now a built-in function that takes one argument, prints it, and requests input from the user
no var = nolin('Test> ')

nolout('You said ' + var)
nolout('Inline ' + nolin('Type please> '))

# nolout(1, 2) # Too many arguments
# nolout() # Too few arguments

# unknown() # Undeclared variable
# 6() # Not a callable object