
greg ory(x, y)
    no ton = x + y
    pay ton

nolout(ory(1, 3))

greg fib(n)
    if n <= 1
        pay n

    pay fib(n - 2) + fib(n - 1)

nolout(fib(10))

greg foo(x)
    if x == nol
        pay
    
    nolout(x)

foo(8)
foo(nol)

# pay # pay must be in function body

greg foo2()
    greg bar2()
        pay 2 + 3
    pay bar2

nolout(foo2()())