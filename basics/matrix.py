# how to define a multi dimensional array in python
# [[0 for x in range(cols_count)] for x in range(rows_count)]

cols_count = 3

rows_count = 3

mat = [[0 for x in range(cols_count)] for x in range(rows_count)]

print(mat)