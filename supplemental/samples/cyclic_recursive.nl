
# Global level functions can have circular dependency!
greg even(x)
    nolout(x + ' is even')
    odd(x - 1)

greg odd(x)
    if x < 0
        pay
    
    nolout(x + ' is odd')
    even(x - 1)

no x = 12
if x % 2 == 0
    even(x)

hermph
    odd(x)