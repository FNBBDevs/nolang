# Arrays are created through array initializers
nolout('\n===== Arrays are created through array initializers =====')

no arr1 = []
no arr2 = [ 1, 2, 3 ]
no arr3 = [ 'nulzo', 'likes', 'cock' ]

nolout('arr1 = ' + arr1)
nolout('arr2 = ' + arr2)
nolout('arr3 = ' + arr3)

# Individual array elements can be accessed
nolout('\n===== Individual array elements can be accessed =====')

nolout('arr2[1] = ' + arr2[1])
nolout('arr3[2] = ' + arr3[2])

# Individual array elements can be assigned
nolout('\n===== Individual array elements can be assigned =====')

nolout('Before: ' + arr3)
nolout('arr3[0] = ' + (arr3[0] = 'yo'))
nolout('After: ' + arr3)

# Array-related errors

# 6[1] # not allowed!
# 'hi'[0] # not allowed!

# Index out of bounds
# arr1[0] # Out of bounds!!
# arr2[3] # Out of bounds!!
# arr3[-1] # Out of bounds!!