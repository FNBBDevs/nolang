
greg foo()
    no x = 'balls'
    bar()

greg bar()
    # x should not be accessible from here!
    nolout(x)

foo()