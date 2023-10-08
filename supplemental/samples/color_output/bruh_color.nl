
# Use the color() function to generate colored text objects!!!
# signature is: color(text: string, fg: string | int | nol, bg: string | int | nol)

nolout(color('This is some colored text', 'cyan', nol))

# Use color codes from 0-255 instead of color names
# See all possible colors: https://github.com/FNBBDevs/bruhcolor/blob/main/bruhcolor/bruhcolor.py#L103C5-L103C5
nolout(color('This is using color-id codes', 27, nol))

# Use it for logging messages
greg log_critical(msg)
    nolout(color('CRITICAL: ' + msg, 'white', 'red'))

log_critical('This is a fatal error!')

# Concatenate any combination of colored texts and strings 
nolout(color('This is colored', 'magenta', nol) + ' This is not')
nolout('This is not colored ' + color('This is', 'magenta', nol))
nolout(color('This is blue ', 'blue', nol) + color('and this is red', 'red', nol))