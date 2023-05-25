
greg foo()
    no x = 'balls'
    bar()

greg bar()
    # x should not be accessible from here!
    nolout('x is ' + x)

no y = 'hi'
greg foo2()
    # y should be accessible from here!
    nolout('y is ' + y)

greg foo3()
    # strange, but z is accessible from here!
    nolout('z is ' + z)

# foo()
foo2()

no z = 8
foo3()

no a = 9
# no what = what # uhhh... yea you can't do this obviously

greg foo4()
    no a = 10
    nolout(a)
    bar2()

greg bar2()
    nolout(a)

bar2() # Should print 9
foo4() # Should print 10 and 9