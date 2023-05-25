
# Bounce loops allow you to execute first before checking the conditions.
# Perfect for algorithms or general-use programs that require code to execute atleast once.

no choice
bounce
    nolout('Choose an item:')
    nolout('1. Nolan')
    nolout('2. Ethan')
    nolout('3. Klim')
    nolout('4. Quit')

    choice = int(nolin('> '))

    if choice == 1
        nolin('Wrong choice')
    
    erm choice == 2
        nolin('Wrong choice')

    erm choice == 3
        nolin('CORRECT!')

while choice != 4

nolout('Goodbye...')