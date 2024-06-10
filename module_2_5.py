def get_matrix(n, m, value):
    matrix = []

    for row in range(n):
        one_row_of_matrix = []

        for col in range(m):
            one_row_of_matrix.append(value)

        matrix.append(one_row_of_matrix)
    return(matrix)

my_matrix = get_matrix(4, 5, 11)

for row in my_matrix:

    print(row)