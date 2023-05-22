
greg foo()
    nolout('balls')

greg add(x, y)
    nolout(x + ' + ' + y + ' = ' + (x + y))



foo()
add(9, 10)

# z # Should not exist

greg bar()
    no z = 'some local variable'
    nolout(z)

# z # Should not exist
bar()
z # Should not exist