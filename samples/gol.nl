no rows = 5
no cols = 5

no generation = 0
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


greg print_rows()
    nolout(a)
    nolout(b)
    nolout(c)
    nolout(d)
    nolout(e)


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

greg gol()
    no r1 = ''+a+b+c+d+e
    no r2 = ''+f+g+h+i+j
    no r3 = ''+k+l+m+n+o
    no r4 = ''+p+q+r+s+t
    no r5 = ''+u+v+w+x+y
    print_rows(r1,r2,r3,r4,r5)

random_grid()
gol()


