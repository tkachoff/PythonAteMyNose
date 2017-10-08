"""
Implement a Matrix class which supports operations:
    addition, multiplication, equality comparison.

Client code should look like this:
a = Matrix([[1, 3], [2, 5]])
b = Matrix([[1, 0], [0, 1]])

assert a * b == a
assert b * b == b
assert a + b = Matrix([[2, 2], [3, 6]])

---------------------------------------

Implement handy functions for matrix creation. We need to be able to do this:
i = Matrix.Identity(3, 3) #  Creates an identity matrix 3x
z = Matrix.Zeros(3, 3) #  Create a zero matrix 3x3

"""


def Identity(n):
    matrix = Zeros(n, n)
    for i in range(n):
        matrix[i][i] = 1
    return matrix


def Zeros(n, m):
    return Matrix([[0] * m for _ in range(n)])


class Matrix:
    def __init__(self, d_list):
        self.__validate(d_list)
        self.d_list = d_list
        self.shape = len(d_list), len(d_list[0])

    def __validate(self, d_list):
        msg = "arg have to be rectangle double list e.g. [[1, 3, 5], [2, 5, 6]]"

        if not isinstance(d_list, list):
            raise ValueError(msg)

        first_row_len = len(d_list[0])
        for i in range(len(d_list)):
            if not isinstance(d_list[i], list) or len(
                    d_list[i]) != first_row_len:
                raise ValueError(msg)

    @property
    def rows(self):
        return self.shape[0]

    @property
    def cols(self):
        return self.shape[1]

    def __getitem__(self, key):
        return self.d_list[key]

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError('Shapes of matrices have to be similar')
        return Matrix([[sum(x) for x in zip(self[i], other[i])] for i in
                       range(self.rows)])

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('argument have to be Matrix instance')
        if other.rows != self.cols:
            raise ValueError('self.cols != other.rows')

        result = Zeros(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(other.rows):
                    result[i][j] += self[i][k] * other[k][j]
        return result

    def __str__(self):
        return '\n'.join(map(str, self.d_list))

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    a = Matrix([[1, 3], [2, 5]])
    b = Matrix([[1, 0], [0, 1]])
    print(a)
    print(b)
    c = a + b
    print(c)
    print(a * b)
    print(Identity(5))
    print(Zeros(5, 5))
