# Arrays can contain functions
nolout('\n===== Arrays can contain functions =====')

greg foo(a, b)
    pay a + b

greg bar(a, b)
    pay a * b

no callbacks = [ foo, bar ]
no idx = 0

nolout('callbacks = ' + callbacks)

while idx < 2
    nolout('callbacks[' + idx + '](1, 5) = ' + callbacks[idx](1, 5))
    idx = idx + 1

# Arrays are mutable
nolout('\n===== Arrays are mutable =====')

greg takes_an_array(arr)
    arr[0] = 1

no my_arr = ['a', 'b', 'c']
nolout('My array before: ' + my_arr)

takes_an_array(my_arr)
nolout('My array after: ' + my_arr)

# Functions can return arrays
nolout('\n===== Functions can return arrays =====')

greg create_loggers(name_of_app)
    greg info(msg)
        nolout('['+ name_of_app + '] INFO: ' + msg)

    greg warn(msg)
        nolout('['+ name_of_app + '] WARN: ' + msg)

    greg error(msg)
        nolout('['+ name_of_app + '] ERROR: ' + msg)

    pay [ info, warn, error ]

no loggers = create_loggers('horny dudes app')

idx = 0
while idx < 3
    loggers[idx]('This is a message')
    idx = idx + 1
