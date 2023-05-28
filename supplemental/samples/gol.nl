no rows = 5
no cols = 5

no generation = 0
no stop_gen   = nolin('What generation to stop: ')

no a=0
no b=0
no c=0
no d=0
no e=0
no f=0
no g=0
no h=0
no i=0
no j=0
no k=0
no l=0
no m=0
no n=0
no o=0
no p=0
no q=0
no r=0
no s=0
no t=0
no u=0
no v=0
no w=0
no x=0
no y=0
no aa=0
no bb=0
no cc=0
no dd=0
no ee=0
no ff=0
no gg=0
no hh=0
no ii=0
no jj=0
no kk=0
no ll=0
no mm=0
no nn=0
no oo=0
no pp=0
no qq=0
no rr=0
no ss=0
no tt=0
no uu=0
no vv=0
no ww=0
no xx=0
no yy=0

# print out the grid using ' ' (dead) and 'o' (alive)
greg print_rows(gen)
    no fill = 'O'
    no space = ' '
    no r1  = ''
    if a == 0
        r1 = r1 + space
    hermph
        r1 = r1 + fill
    if b == 0
        r1 = r1 + space
    hermph
        r1 = r1 + fill
    if c == 0
        r1 = r1 + space
    hermph
        r1 = r1 + fill
    if d == 0
        r1 = r1 + space
    hermph
        r1 = r1 + fill
    if e == 0
        r1 = r1 + space
    hermph
        r1 = r1 + fill
    
    no r2  = ''
    if f == 0
        r2 = r2 + space
    hermph
        r2 = r2 + fill
    if g == 0
        r2 = r2 + space
    hermph
        r2 = r2 + fill
    if h == 0
        r2 = r2 + space
    hermph
        r2 = r2 + fill
    if i == 0
        r2 = r2 + space
    hermph
        r2 = r2 + fill
    if j == 0
        r2 = r2 + space
    hermph
        r2 = r2 + fill
    
    no r3  = ''
    if k == 0
        r3 = r3 + space
    hermph
        r3 = r3 + fill
    if l == 0
        r3 = r3 + space
    hermph
        r3 = r3 + fill
    if m == 0
        r3 = r3 + space
    hermph
        r3 = r3 + fill
    if n == 0
        r3 = r3 + space
    hermph
        r3 = r3 + fill
    if o == 0
        r3 = r3 + space
    hermph
        r3 = r3 + fill
    
    no r4  = ''
    if p == 0
        r4 = r4 + space
    hermph
        r4 = r4 + fill
    if q == 0
        r4 = r4 + space
    hermph
        r4 = r4 + fill
    if r == 0
        r4 = r4 + space
    hermph
        r4 = r4 + fill
    if s == 0
        r4 = r4 + space
    hermph
        r4 = r4 + fill
    if t == 0
        r4 = r4 + space
    hermph
        r4 = r4 + fill
    
    no r5  = ''
    if u == 0
        r5 = r5 + space
    hermph
        r5 = r5 + fill
    if v == 0
        r5 = r5 + space
    hermph
        r5 = r5 + fill
    if w == 0
        r5 = r5 + space
    hermph
        r5 = r5 + fill
    if x == 0
        r5 = r5 + space
    hermph
        r5 = r5 + fill
    if y == 0
        r5 = r5 + space
    hermph
        r5 = r5 + fill

    # nolout('GENERATION #' + gen)
    nolout("+-----+")
    nolout('|' + r1 + '|')
    nolout('|' + r2 + '|')
    nolout('|' + r3 + '|')
    nolout('|' + r4 + '|')
    nolout('|' + r5 + '|')
    nolout("+-----+\n")

# generate the random starting grid
greg random_grid()
    no index = 0
    while index < (rows * cols)
        no select_alive = random() < 0.5
        if index == 0
            if select_alive
                a = 1
            hermph
                a = 0
        erm index == 1
            if select_alive
                b = 1
            hermph
                b = 0
        erm index == 2
            if select_alive
                c = 1
            hermph
                c = 0
        erm index == 3
            if select_alive
                d = 1
            hermph
                d = 0
        erm index == 4
            if select_alive
                e = 1
            hermph
                e = 0
        erm index == 5
            if select_alive
                f = 1
            hermph
                f = 0
        erm index == 6
            if select_alive
                g = 1
            hermph
                g = 0
        erm index == 7
            if select_alive
                h = 1
            hermph
                h = 0
        erm index == 8
            if select_alive
                i = 1
            hermph
                i = 0
        erm index == 9
            if select_alive
                j = 1
            hermph
                j = 0
        erm index == 10
            if select_alive
                k = 1
            hermph
                k = 0
        erm index == 11
            if select_alive
                l = 1
            hermph
                l = 0
        erm index == 12
            if select_alive
                m = 1
            hermph
                m = 0
        erm index == 13
            if select_alive
                n = 1
            hermph
                n = 0
        erm index == 14
            if select_alive
                o = 1
            hermph
                o = 0
        erm index == 15
            if select_alive
                p = 1
            hermph
                p = 0
        erm index == 15
            if select_alive
                q = 1
            hermph
                q = 0
        erm index == 16
            if select_alive
                r = 1
            hermph
                r = 0
        erm index == 17
            if select_alive
                s = 1
            hermph
                s = 0
        erm index == 18
            if select_alive
                t = 1
            hermph
                t = 0
        erm index == 19
            if select_alive
                u = 1
            hermph
                u = 0
        erm index == 20
            if select_alive
                v = 1
            hermph
                v = 0
        erm index == 21
            if select_alive
                w = 1
            hermph
                w = 0
        erm index == 22
            if select_alive
                x = 1
            hermph
                x = 0
        erm index == 23
            if select_alive
                y = 1
            hermph
                y = 0

        index = index + 1

# function to get the next generation of values
greg next_generation()
    no index = 0
    while index < (rows * cols)
        no neighbors = 0
        if index == 0
            if b == 1
                neighbors = neighbors + 1
            if f == 1
                neighbors = neighbors + 1
            if g == 1
                neighbors = neighbors + 1
            if a == 0 # dead
                if neighbors == 3
                    aa = 1
                hermph
                    aa = 0
            erm a == 1 # alive
                if neighbors == 2 or neighbors == 3
                    aa = 1
                hermph
                    aa = 0
        erm index == 1
            if a == 1
                neighbors = neighbors + 1
            if f == 1
                neighbors = neighbors + 1
            if g == 1
                neighbors = neighbors + 1
            if h == 1
                neighbors = neighbors + 1
            if c == 1
                neighbors = neighbors + 1
            if b == 0 # dead
                if neighbors == 3
                    bb = 1
                hermph
                    bb = 0
            erm b == 1 # alive
                if neighbors == 2 or neighbors == 3
                    bb = 1
                hermph
                    bb = 0
        erm index == 2
            if b == 1
                neighbors = neighbors + 1
            if g == 1
                neighbors = neighbors + 1
            if h == 1
                neighbors = neighbors + 1
            if i == 1
                neighbors = neighbors + 1
            if d == 1
                neighbors = neighbors + 1
            if c == 0
                if neighbors == 3
                        cc = 1
                hermph
                        cc = 0
            erm c == 1
                if neighbors == 2 or neighbors == 3
                        cc = 1
                hermph
                        cc = 0
        erm index == 3
            if c == 1
                neighbors = neighbors + 1
            if h == 1
                neighbors = neighbors + 1
            if i == 1
                neighbors = neighbors + 1
            if j == 1
                neighbors = neighbors + 1
            if e == 1
                neighbors = neighbors + 1
            if d == 0
                if neighbors == 3
                        dd = 1
                hermph
                        dd = 0
            erm d == 1
                if neighbors == 2 or neighbors == 3
                        dd = 1
                hermph
                        dd = 0
        erm index == 4
            if d == 1
                neighbors = neighbors + 1
            if i == 1
                neighbors = neighbors + 1
            if j == 1
                neighbors = neighbors + 1

            if e == 0
                if neighbors == 3
                        ee = 1
                hermph
                        ee = 0
            erm e == 1
                if neighbors == 2 or neighbors == 3
                        ee = 1
                hermph
                        ee = 0
        erm index == 5
            if a == 1
                neighbors = neighbors + 1
            if b == 1
                neighbors = neighbors + 1
            if g == 1
                neighbors = neighbors + 1
            if l == 1
                neighbors = neighbors + 1
            if k == 1
                neighbors = neighbors + 1

            if f == 0
                if neighbors == 3
                        ff = 1
                hermph
                        ff = 0
            erm f == 1
                if neighbors == 2 or neighbors == 3
                        ff = 1
                hermph
                        ff = 0

        erm index == 6
            if a == 1
                neighbors = neighbors + 1
            if b == 1
                neighbors = neighbors + 1
            if c == 1
                neighbors = neighbors + 1
            if f == 1
                neighbors = neighbors + 1
            if h == 1
                neighbors = neighbors + 1
            if k == 1
                neighbors = neighbors + 1
            if l == 1
                neighbors = neighbors + 1
            if m == 1
                neighbors = neighbors + 1

            if g == 0
                if neighbors == 3
                        gg = 1
                hermph
                        gg = 0
            erm g == 1
                if neighbors == 2 or neighbors == 3
                        gg = 1
                hermph
                        gg = 0

        erm index == 7
            if b == 1
                neighbors = neighbors + 1
            if c == 1
                neighbors = neighbors + 1
            if d == 1
                neighbors = neighbors + 1
            if g == 1
                neighbors = neighbors + 1
            if i == 1
                neighbors = neighbors + 1
            if l == 1
                neighbors = neighbors + 1
            if m == 1
                neighbors = neighbors + 1
            if n == 1
                neighbors = neighbors + 1

            if h == 0
                if neighbors == 3
                        hh = 1
                hermph
                        hh = 0
            erm h == 1
                if neighbors == 2 or neighbors == 3
                        hh = 1
                hermph
                        hh = 0
        erm index == 8
            if e == 1
                neighbors = neighbors + 1
            if c == 1
                neighbors = neighbors + 1
            if d == 1
                neighbors = neighbors + 1
            if h == 1
                neighbors = neighbors + 1
            if j == 1
                neighbors = neighbors + 1
            if o == 1
                neighbors = neighbors + 1
            if m == 1
                neighbors = neighbors + 1
            if n == 1
                neighbors = neighbors + 1

            if i == 0
                if neighbors == 3
                        ii = 1
                hermph
                        ii = 0
            erm i == 1
                if neighbors == 2 or neighbors == 3
                        ii = 1
                hermph
                        ii = 0
        erm index == 9
            if e == 1
                neighbors = neighbors + 1
            if d == 1
                neighbors = neighbors + 1
            if i == 1
                neighbors = neighbors + 1
            if n == 1
                neighbors = neighbors + 1
            if o == 1
                neighbors = neighbors + 1

            if j == 0
                if neighbors == 3
                        jj = 1
                hermph
                        jj = 0
            erm j == 1
                if neighbors == 2 or neighbors == 3
                        jj = 1
                hermph
                        jj = 0

        erm index == 10
            if f == 1
                neighbors = neighbors + 1
            if g == 1
                neighbors = neighbors + 1
            if l == 1
                neighbors = neighbors + 1
            if q == 1
                neighbors = neighbors + 1
            if p == 1
                neighbors = neighbors + 1

            if k == 0
                if neighbors == 3
                        kk = 1
                hermph
                        kk = 0
            erm k == 1
                if neighbors == 2 or neighbors == 3
                        kk = 1
                hermph
                        kk = 0

        erm index == 11
            if f == 1
                neighbors = neighbors + 1
            if g == 1
                neighbors = neighbors + 1
            if h == 1
                neighbors = neighbors + 1
            if j == 1
                neighbors = neighbors + 1
            if m == 1
                neighbors = neighbors + 1
            if p == 1
                neighbors = neighbors + 1
            if q == 1
                neighbors = neighbors + 1
            if r == 1
                neighbors = neighbors + 1
            if l == 0
                if neighbors == 3
                        ll = 1
                hermph
                        ll = 0
            erm l == 1
                if neighbors == 2 or neighbors == 3
                        ll = 1
                hermph
                        ll = 0
        erm index == 12
            if i == 1
                neighbors = neighbors + 1
            if g == 1
                neighbors = neighbors + 1
            if h == 1
                neighbors = neighbors + 1
            if l == 1
                neighbors = neighbors + 1
            if n == 1
                neighbors = neighbors + 1
            if s == 1
                neighbors = neighbors + 1
            if q == 1
                neighbors = neighbors + 1
            if r == 1
                neighbors = neighbors + 1

            if m == 0
                if neighbors == 3
                        mm = 1
                hermph
                        mm = 0
            erm m == 1
                if neighbors == 2 or neighbors == 3
                        mm = 1
                hermph
                        mm = 0
        erm index == 13
            if h == 1
                neighbors = neighbors + 1
            if i == 1
                neighbors = neighbors + 1
            if j == 1
                neighbors = neighbors + 1
            if m == 1
                neighbors = neighbors + 1
            if o == 1
                neighbors = neighbors + 1
            if s == 1
                neighbors = neighbors + 1
            if t == 1
                neighbors = neighbors + 1
            if r == 1
                neighbors = neighbors + 1

            if n == 0
                if neighbors == 3
                        nn = 1
                hermph
                        nn = 0
            erm n == 1
                if neighbors == 2 or neighbors == 3
                        nn = 1
                hermph
                        nn = 0
            
        erm index == 14
            if n == 1
                neighbors = neighbors + 1
            if i == 1
                neighbors = neighbors + 1
            if j == 1
                neighbors = neighbors + 1
            if s == 1
                neighbors = neighbors + 1
            if t == 1
                neighbors = neighbors + 1
            
            if o == 0
                if neighbors == 3
                        oo = 1
                hermph
                        oo = 0
            erm o == 1
                if neighbors == 2 or neighbors == 3
                        oo = 1
                hermph
                        oo = 0

        erm index == 15
            if k == 1
                neighbors = neighbors + 1
            if l == 1
                neighbors = neighbors + 1
            if q == 1
                neighbors = neighbors + 1
            if v == 1
                neighbors = neighbors + 1
            if u == 1
                neighbors = neighbors + 1

            if p == 0
                if neighbors == 3
                        pp = 1
                hermph
                        pp = 0
            erm p == 1
                if neighbors == 2 or neighbors == 3
                        pp = 1
                hermph
                        pp = 0

        erm index == 16
            if k == 1
                neighbors = neighbors + 1
            if l == 1
                neighbors = neighbors + 1
            if m == 1
                neighbors = neighbors + 1
            if p == 1
                neighbors = neighbors + 1
            if r == 1
                neighbors = neighbors + 1
            if u == 1
                neighbors = neighbors + 1
            if v == 1
                neighbors = neighbors + 1
            if w == 1
                neighbors = neighbors + 1
            if q == 0
                if neighbors == 3
                        qq = 1
                hermph
                        qq = 0
            erm q == 1
                if neighbors == 2 or neighbors == 3
                        qq = 1
                hermph
                        qq = 0
        erm index == 17
            if n == 1
                neighbors = neighbors + 1
            if l == 1
                neighbors = neighbors + 1
            if m == 1
                neighbors = neighbors + 1
            if q == 1
                neighbors = neighbors + 1
            if s == 1
                neighbors = neighbors + 1
            if x == 1
                neighbors = neighbors + 1
            if v == 1
                neighbors = neighbors + 1
            if w == 1
                neighbors = neighbors + 1
            if r == 0
                if neighbors == 3
                        rr = 1
                hermph
                        rr = 0
            erm r == 1
                if neighbors == 2 or neighbors == 3
                        rr = 1
                hermph
                        rr = 0
        erm index == 18
            if n == 1
                neighbors = neighbors + 1
            if o == 1
                neighbors = neighbors + 1
            if m == 1
                neighbors = neighbors + 1
            if r == 1
                neighbors = neighbors + 1
            if t == 1
                neighbors = neighbors + 1
            if x == 1
                neighbors = neighbors + 1
            if y == 1
                neighbors = neighbors + 1
            if w == 1
                neighbors = neighbors + 1
            if s == 0
                if neighbors == 3
                        ss = 1
                hermph
                        ss = 0
            erm s == 1
                if neighbors == 2 or neighbors == 3
                        ss = 1
                hermph
                        ss = 0
        erm index == 19
            if n == 1
                neighbors = neighbors + 1
            if o == 1
                neighbors = neighbors + 1
            if s == 1
                neighbors = neighbors + 1
            if x == 1
                neighbors = neighbors + 1
            if y == 1
                neighbors = neighbors + 1
            if t == 0
                if neighbors == 3
                        tt = 1
                hermph
                        tt = 0
            erm t == 1
                if neighbors == 2 or neighbors == 3
                        tt = 1
                hermph
                        tt = 0
        erm index == 20
            if p == 1
                neighbors = neighbors + 1
            if q == 1
                neighbors = neighbors + 1
            if v == 1
                neighbors = neighbors + 1
            if u == 0
                if neighbors == 3
                        uu = 1
                hermph
                        uu = 0
            erm u == 1
                if neighbors == 2 or neighbors == 3
                        uu = 1
                hermph
                        uu = 0
        erm index == 21
            if u == 1
                neighbors = neighbors + 1
            if p == 1
                neighbors = neighbors + 1
            if q == 1
                neighbors = neighbors + 1
            if r == 1
                neighbors = neighbors + 1
            if w == 1
                neighbors = neighbors + 1
            if v == 0
                if neighbors == 3
                        vv = 1
                hermph
                        vv = 0
            erm v == 1
                if neighbors == 2 or neighbors == 3
                        vv = 1
                hermph
                        vv = 0
        erm index == 22
            if v == 1
                neighbors = neighbors + 1
            if x == 1
                neighbors = neighbors + 1
            if q == 1
                neighbors = neighbors + 1
            if r == 1
                neighbors = neighbors + 1
            if s == 1
                neighbors = neighbors + 1
            if w == 0
                if neighbors == 3
                        ww = 1
                hermph
                        ww = 0
            erm w == 1
                if neighbors == 2 or neighbors == 3
                        ww = 1
                hermph
                        ww = 0
        erm index == 23
            if w == 1
                neighbors = neighbors + 1
            if y == 1
                neighbors = neighbors + 1
            if t == 1
                neighbors = neighbors + 1
            if r == 1
                neighbors = neighbors + 1
            if s == 1
                neighbors = neighbors + 1
            if x == 0
                if neighbors == 3
                        xx = 1
                hermph
                        xx = 0
            erm x == 1
                if neighbors == 2 or neighbors == 3
                        xx = 1
                hermph
                        xx = 0
        erm index == 24
            if x == 1
                neighbors = neighbors + 1
            if s == 1
                neighbors = neighbors + 1
            if t == 1
                neighbors = neighbors + 1
            if y == 0
                if neighbors == 3
                        yy = 1
                hermph
                        yy = 0
            erm y == 1
                if neighbors == 2 or neighbors == 3
                        yy = 1
                hermph
                        yy = 0

        index = index + 1
# push the next gen to current
greg push_to_current()
    a = aa
    b = bb
    c = cc
    d = dd
    e = ee
    f = ff
    g = gg
    h = hh
    i = ii
    j = jj
    k = kk
    l = ll
    m = mm
    n = nn
    o = oo
    p = pp
    q = qq
    r = rr
    s = ss
    t = tt
    u = uu
    v = vv
    w = ww
    x = xx
    y = yy

# main function to run GOL
greg gol()
    while ''+generation != stop_gen
        if generation == 0
            random_grid()

        print_rows(generation)
        next_generation()
        push_to_current()
        generation = generation + 1

gol()