greg builtins(a, b)
    nolout('float(' + b +') -> ' + float(b))
    nolout('int(' + a + ') -> ' + int(a))
    nolout('rounddown(' + a + ') -> ' + rounddown(a))
    nolout('roundup(' + a + ') -> ' + roundup(a))

builtins(9.5, 2)