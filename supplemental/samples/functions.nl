
greg foo()
    nolout('balls')

greg add(x, y)
    nolout(x + ' + ' + y + ' = ' + (x + y))

greg count(n)
    if n > 0
        nolout(n)
        count(n - 1)

foo()
add(9, 10)
count(10)

# foo(69) # Too many arguments
# add(420) # Too few arguments
# unknown() # Undeclared function
# 6() # Not a callable object

# z # Should not exist

greg bar()
    no z = 'some local variable'
    nolout(z)

# z # Should not exist
bar()
# z # Should not exist