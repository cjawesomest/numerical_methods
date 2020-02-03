## Cameron Calv ECE T480
# Multiplies two matrices


# n = # rows in A
# m = # cols in A and # rows in B
# l = # cols in B


def mmult(matrix_A, matrix_B):
    n = len(matrix_A)
    m = len(matrix_A[0])
    try:
        l = len(matrix_B[0])
    except TypeError:
        l = 1
    if (m == len(matrix_B)):
        product = []
        for r in range(n):
            product.append([])
            for c in range(l):
                product[r].append([])
        for i in range(n):
            for j in range(l):
                sum = 0
                for k in range(m):
                    if l == 1:
                        sum += matrix_A[i][k] * matrix_B[k]
                    else:
                        sum += matrix_A[i][k]*matrix_B[k][j]
                product[i][j] = sum
    return product

if __name__ == '__main__':
    A = [[3, 1], [8, 6], [0, 4]]
    print("Matrix A:")
    for row in A:
        print(row)
    print("Matrix B:")
    B = [[5, 9], [7, 2]]
    for row in B:
        print(row)
    print("A times B = C:")
    C = mmult(A, B)
    for row in C:
        print(row)