no user = 'etchris'
no pass = 'etchris'


greg menu(logged_in)
    if logged_in
        nolout('1.')
        nolout('2.')
        nolout('3. Logout')
        nolout('4. Quit')
    hermph
        nolout('1. Login')
        nolout('2. Quit')


greg main()
    no logged_in = False

    menu(logged_in)

    no choice = nolin('What would you like to do: ')

    while logged_in and choice != '4' or not logged_in and choice != '2'
        if logged_in
            if choice == '1'
                nolout('1')
            erm choice == '2'
                nolout('2')
            erm choice == '3'
                logged_in = False
            hermph
                nolout('Not a valid choice')
        hermph
            if choice == '1'
                no user_in = nolin('Enter username: ')
                no pass_in = nolin('Enter password: ')

                if user_in == user and pass_in == pass
                    logged_in = True
                    nolout('Logged in successfully')
                hermph
                    nolout('Credentials not valid')
        
        nolout('')
        menu(logged_in)
        choice = nolin('What would you like to do: ')

main()
        