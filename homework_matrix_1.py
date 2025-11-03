n = int(input("количество строк: "))
m = int(input("количество столбцов: "))
mat = []
print("Введите элементы матрицы: ")
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input()))
    mat.append(row)
for row in mat:
    print(row)

transposed = []
for j in range(m):
    new_row = []
    for i in range(n):
        new_row.append(mat[i][j])
    transposed.append(new_row)

print("Транспонированная матрица:")
for new_row in transposed:
    print(new_row)
