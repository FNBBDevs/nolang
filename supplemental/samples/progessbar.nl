greg char_builder(char, count)
    no x = 0
    no out = ""
    while x < count
        out = out + char
        x = x + 1
    pay out

greg progress_bar()
    no x = 0
    no left = ""
    no right = ""
    bounce
        x = x + 1
        left = char_builder("=", x)
        right = char_builder(" ", 100 - x)
        nolout(char_builder("\n", 30))
        nolout("[" + left + right + "]")
        sleep(0.05)
    while x < 100

progress_bar()