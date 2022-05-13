class Matrix:
    def __init__(self, n: int = 5, m: int = 5, data = None):
        # data not in arguments because list is mutable object
        if not data:
            data = [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]

        self.data = data
        self.n = n
        self.m = m

    def __str__(self):
        return '\n'.join([str(row) for row in self.data])


def max_matrix_element(matrix: Matrix):
    return max(map(max, matrix.data))


def min_matrix_element(matrix: Matrix):
    return min(map(min, matrix.data))


def sum_matrix_elements(matrix: Matrix):
    return sum(map(sum, matrix.data))


matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]
n = 3
m = 3
if __name__ == '__main__':
    mat = Matrix(data=matrix_data, n=n, m=m)

    print(mat)  # str
    print(max_matrix_element(mat))  # 9
    print(min_matrix_element(mat))  # 1
    print(sum_matrix_elements(mat))  # 45
