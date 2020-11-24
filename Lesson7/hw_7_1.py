# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#
# Примеры матриц вы найдете в методичке.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix(object):
    __matrix = []
    def __init__(self, a:list):
        self.__matrix = a

    def __str__(self):
        res=""
        for el in self.__matrix:
            res += " ".join([str(e) for e in el])+'\n'
        return res

    def __len__(self):
        return len(self.__matrix)

    def __index__(self):
        return

    def __add__(self, other):
        new_matrix = []
        for i in range(0,len(self)):
            new_matrix += [[x+y for x, y in zip(self.__matrix[i], other.__matrix[i])]]
        return Matrix(new_matrix)

matr2x3 = Matrix([[31, 22, 37],[43, 51, 86]])
matr2x3_ = Matrix([[11, 22, 33],[14, 0, -100]])


print(f'{matr2x3}+\n{matr2x3_}=')
print(matr2x3+matr2x3_)

matr3x3 = Matrix([[3, 5, 32],[2, 4, 6],[-1, 64, -8]])
matr3x3_ = Matrix([[10, 15, 20],[22, 23, 24],[31, 32, 33]])

print(f'{matr3x3}+\n{matr3x3_}=')
print(matr3x3+matr3x3_)

matr2x4 = Matrix([[3, 5, 8, 3],[8, 3, 7, 1]])
matr2x4_ = Matrix([[-3, -5, -8, -3],[-8, -3, -7, -1]])

print(f'{matr2x4}+\n{matr2x4_}=')
print(matr2x4+matr2x4_)
