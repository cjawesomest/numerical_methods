## Cameron Calv ECE T480
# Transposes a matrix or vector
# Works for vectors and symmetrically-dimensioned matrices

def tpose(matrix_or_vector):
    transpose = []
    try:
        for r in range(len(matrix_or_vector[0])):
            transpose.append([])
            for c in range(len(matrix_or_vector)):
                transpose[r].append([])
    except TypeError:
        for r in range(len(matrix_or_vector)):
            transpose.append([matrix_or_vector[r]])
        return transpose
    row_number = 0
    for row in matrix_or_vector:
        col_number = 0
        for element in row:
            transpose[col_number][row_number] = element
            col_number += 1
        row_number += 1
    return transpose


if __name__ == '__main__':
    print("Our matrix!")
    matrix = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]
    for row in matrix:
        print(row)
    transpose = tpose(matrix)
    print("Our transposed matrix!")
    for row in transpose:
        print(row)

    print("Our vector!")
    vector = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    for row in vector:
        print(row)
    transpose_v = tpose(vector)
    print("Our transposed vector!")
    for row in transpose_v:
        print(row)
