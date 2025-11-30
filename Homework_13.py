matrix = [ [1, 2, 3], [4, 5, 6] ]

def task_8(matrix):
    row_sums = [sum(row) for row in matrix]
    print(*row_sums)


    num_columns = len(matrix[0])
    # создаём список, элементы которого ноль, длиной в количество столбов
    column_sums = [0] * num_columns

    for row in matrix:
        for j in range(num_columns):
            column_sums[j] += row[j]
    print(*column_sums)


    rows = len(matrix)
    cols = len(matrix[0])
    # Создаем пустую транспонированную матрицу
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    print(transposed)


    double = list(map(lambda row: [x * 2 for x in row], matrix))
    print(double)

task_8(matrix)











