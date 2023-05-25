
greg add(x)
    greg _aux(y)
        pay x + y

    pay _aux

nolout(add(9))
nolout(add(9)(8))

no a = 'oops!'

if True
    greg foo()
        pay a

    nolout(foo() == 'oops!') # Should be true!
    no a = 'josh'
    nolout(foo() == 'oops!') # Should be true!