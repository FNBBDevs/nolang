##### The following is a showcase of nolang's built-in runtime library #####

# nolout() is a built-in function that takes one argument and prints it
nolout('hi??')

# nolin() is a built-in function that takes one argument, prints it, and requests input from the user
no var = nolin('Test> ')

nolout('You said ' + var)
nolout('Inline ' + nolin('Type please> '))

greg builtins(a, b)
    nolout('float(' + b +') -> ' + float(b))
    nolout('int(' + a + ') -> ' + int(a))
    nolout('rounddown(' + a + ') -> ' + rounddown(a))
    nolout('roundup(' + a + ') -> ' + roundup(a))

builtins(9.5, 2)

# Instrumentation use `time()`

no MAX = 10000
nolout('Counting to ' + MAX + '...')
no start = time()

no x = 0
while x < MAX
    x = x + 1

no end = time() - start
nolout('Took ' + (end / 1000.0) + 's to count.')