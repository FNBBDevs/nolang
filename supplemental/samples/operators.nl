
# Addition: +, -
greg addition()
    nolout('\nADDITION: +, -\n=================\n')
    nolout('3 + 3 = ' + (3 + 3))
    nolout('3 + 3.2 = ' + (3 + 3.2)) # ints are promoted to floats when added with floats
    nolout('3.2 + 3 = ' + (3.2 + 3))
    nolout('1.1 + 1.1 = ' + (1.1 + 1.1))
    nolout('3 - 3 = ' + (3 - 3))
    nolout('3 - 3.2 = ' + (3 - 3.2))
    nolout('3.2 - 3 = ' + (3.2 - 3))
    nolout('1.1 - 1.1 = ' + (1.1 - 1.1))

    nolout('\'hi\' + \' there\' = ' + ('hi' + ' there')) # strings can be concatenated with strings or any other type
    nolout('\'hi\' + nol = ' + ('hi' + nol))
    nolout('\'hi\' + True = ' + ('hi' + True))
    nolout('\'hi\' + 3.2 = ' + ('hi' + 3.2))
    nolout('3 + \'hi\' = ' + (3 + 'hi'))
    nolout('\'hi\' + 3 = ' + ('hi' + 3))

    # nolout((3 + nol)) # Addition only supports numbers or strings
    # nolout((nol + 3))
    # nolout((True + True))
    # nolout(('hi' - 3)) # Can't subtract strings???
    # nolout(('hi' - ' there'))

# Multiplication: *, /, %
greg multiplication()
    nolout('\nMULTIPLICATION: *, /, %\n=================\n')
    nolout('3 * 3 = ' + (3 * 3))
    nolout('3 * 3.2 = ' + (3 * 3.2)) # ints are promoted to floats when multiplied with floats
    nolout('3.2 * 3 = ' + (3.2 * 3))
    nolout('3 / 3 = ' + (3 / 3)) # Only integers results in int division
    nolout('3 / 3.2 = ' + (3 / 3.2)) # Otherwise float division
    nolout('3.2 / 3 = ' + (3.2 / 3)) 
    nolout('1.1 / 1.1 = ' + (1.1 / 1.1))
    nolout('4 % 3 = ' + (4 % 3))

    # nolout((True * 3)) # Multiplication only supports numbers
    # nolout((nol * 3))
    # nolout(('hi' * 3))
    # nolout((True / 3))
    # nolout((nol / 3))
    # nolout(('hi' / 3))
    # nolout((1 / 0)) # Divide by zero!!!
    # nolout((1 / 0.0))
    # nolout((4.2 % 3)) # Modulus only supports integers
    # nolout(('hi' % 3))

# Exponentiation: **
greg exp()
    nolout('\nEXPONENTIATION: **\n=================\n')
    nolout('3 ** 2 = ' + (3 ** 2))
    nolout('2 ** 0.5 = ' + (2 ** 0.5)) # ints are promoted to floats when exponentiated with floats
    nolout('0.5 ** 3 = ' + (0.5 ** 2))
    nolout('2 ** 3 ** 3 == (2 ** (3 ** 3)) = ' + (2 ** 3 ** 3 == (2 ** (3 ** 3)))) # Exponentiation is right associative

    # nolout((True ** 3)) # Exponentiation only supports numbers
    # nolout((nol ** 3))
    # nolout(('hi' ** 3))

# Equality: ==, !=
greg equality()
    nolout('\nEQUALITY: ==, !=\n=================\n')
    nolout('3 == 2 = ' + (3 == 2)) # Equality works with any types and results in bool
    nolout('3 != 2 = ' + (3 != 2))
    nolout('3.2 == 3 = ' + (3.2 == 3))
    nolout('3.2 != 3 = ' + (3.2 != 3))
    nolout('3.2 == 3.2 = ' + (3.2 == 3.2))
    nolout('3.2 != 3.2 = ' + (3.2 != 3.2))
    nolout('0.1 + 0.2 == 0.3 = ' + (0.1 + 0.2 == 0.3)) # Careful with floats!
    nolout('0.1 + 0.2 != 0.3 = ' + (0.1 + 0.2 != 0.3)) 
    nolout('nol == nol = ' + (nol == nol))
    nolout('nol != nol = ' + (nol != nol))
    nolout('nol == 1 = ' + (nol == 1))
    nolout('nol != 1 = ' + (nol != 1))
    nolout('True == False = ' + (True == False))
    nolout('True != False = ' + (True != False))
    nolout('\'yo\' == \'yo\' = ' + ('yo' == 'yo'))
    nolout('\'yo\' != \'yo\' = ' + ('yo' != 'yo'))
    nolout('\'no\' == \'NO\' = ' + ('no' == 'NO'))
    nolout('\'no\' != \'NO\' = ' + ('no' != 'NO'))

# Relational: <, >, <=, >=
greg relational()
    nolout('\nRELATIONAL: <, >, <=, >=\n=================\n')
    nolout('3 < 2 = ' + (3 < 2)) # Relational operators work with numbers or strings and result in bool
    nolout('3 > 2 = ' + (3 > 2))
    nolout('3 <= 2 = ' + (3 <= 2))
    nolout('3 >= 2 = ' + (3 >= 2))
    nolout('2 < 2.001 = ' + (2 < 2.001))
    nolout('2.001 > 2 = ' + (2.001 > 2))
    nolout('\'adam\' < \'bert\' = ' + ('adam' < 'bert'))
    nolout('\'adam\' < \'Bert\' = ' + ('adam' < 'Bert'))

    # nolout((True < 3)) # Relational operators only support numbers or strings
    # nolout((True > 3))
    # nolout((True <= 3))
    # nolout((True >= 3))
    # nolout((nol < 1))
    # nolout((1 > nol))
    # nolout(('hi' < 3)) # Both operands must be strings for string comparison

# Logical: and, or, not
greg logical()
    nolout('\nLOGICAL: and, or, not\n=================\n')
    nolout('True and True = ' + (True and True)) # Logical operators work with any type and result in bool
    nolout('True and False = ' + (True and False))
    nolout('False and True = ' + (False and True))
    nolout('False and False = ' + (False and False))
    nolout('True or True = ' + (True or True))
    nolout('True or False = ' + (True or False))
    nolout('False or True = ' + (False or True))
    nolout('False or False = ' + (False or False))
    nolout('not True = ' + (not True))
    nolout('not False = ' + (not False))

    # nol, 0 and False are false, anything else is true
    nolout('1 and nol = ' + (1 and nol))
    nolout('1 and 0 = ' + (1 and 0))
    nolout('1 and False = ' + (1 and False))
    nolout('\'true\' and 1 = ' + ('true' and 1))
    nolout('not nol = ' + (not nol))
    nolout('not 1 = ' + (not 1))
    nolout('not \'true\' = ' + (not 'true'))

    greg foo()
        nolout(('SIDE-EFFECT!!!!!!'))
        pay True

    # Logical operators are short-circuited!
    nolout('False and foo() = ' + (False and foo())) # no side-effect
    nolout('True and foo() = ' + (True and foo()))
    nolout('True or foo() = ' + (True or foo())) # no side-effect
    nolout('False or foo() = ' + (False or foo()))

# Unary: +, -
greg unary()
    nolout('\nUNARY: +, -\n=================\n')
    nolout('-3 = ' + (-3))
    nolout('+3 = ' + (+3))
    nolout('-0 = ' + (-0))
    nolout('-3.2 = ' + (-3.2))
    nolout('+3.2 = ' + (+3.3))
    nolout('-0.0 = ' + (-0.0))

    # nolout((-'hi')) # Unary operators only support numbers
    # nolout((+False))
    # nolout((-nol)) 

greg misc()
    nolout('\nMISC\n=================\n')
    no a = True
    no b = False
    no x = 9
    no y = 10
    no s = 'hi'
    no t = 'there'
    no f = 9.2
    no g = 3.3
    no n

    greg foo()
        pay

    greg bar()
        pay

    nolout((f + g + x + y))
    nolout((f - g - x - y))
    nolout((f / g / x / y))
    nolout((f * g * x * y))
    nolout((x % y))
    nolout((f ** g + x ** y))
    nolout((s + ' ' + t))
    nolout((s + ' ' + x))
    nolout((s + ' ' + y))
    nolout((a == b))
    nolout((a and b))
    nolout((a and n))
    nolout((not n))
    nolout((not y))
    nolout((a and x))
    nolout((a and f))
    nolout((s < t))
    nolout((t >= s))
    nolout((f < g))
    nolout((g >= f))
    nolout((-x))
    nolout((+x))
    nolout((-y))
    nolout((+y))
    nolout((foo == foo))
    nolout((foo != foo))
    nolout((foo == bar))
    nolout((foo != bar))
    
    # The following should be erroneous
    # nolout((a + b))
    # nolout((a * x))
    # nolout((s / x))
    # nolout((s ** x))
    # nolout((n % x))
    # nolout((foo < x))
    # nolout((y > bar))
    # nolout((bar * foo))
    # nolout((foo ** bar))
    # nolout((bar + x))
    # nolout((x + bar))

addition()
multiplication()
exp()
equality()
relational()
logical()
unary()
misc()