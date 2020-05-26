# Задание 1


class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


my_matrix = Matrix([[4, 13, 25, 1],
                    [6, 23, 18, 3],
                    [16, 6, 9, 8]],
                   [[4, 3, 18, 15],
                    [6, 7, 7, 0],
                    [2, 5, 9, 78]])
print(my_matrix.__add__())
