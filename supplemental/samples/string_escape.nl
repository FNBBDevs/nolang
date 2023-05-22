# Support the following character escape sequences:

# - \\ (escape single backslash)
nolout('\\') # Should print single backslash

# - \" (escape double quote)
nolout("\"")

# - \' (escape single quote)
nolout('\'')

# - \n (line feed)
nolout('hello\nman')

# - \r (carriage return)
nolout('mello\rman')

# - \b (backspace)
nolout('hello\bman')

# - \v (vertical tab)*
nolout('hello\vman')

# - \t (horizontal tab)
nolout('hello\tman')

# - \a (alert)
nolout('hello\aman')

nolout('hello\nthis\tstring\bhas\vescape\asequences')

# nolout('Unknown sequence should cause lexer error \?')

# nolout('Escaped quote causes unterminated string\')