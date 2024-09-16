matrix = []
validChars = True


def invalid():
    print('invalid')
    exit(0)


while True:
    rowStr = input()
    if rowStr == '-1':
        break
    try:
        row = list(map(int, rowStr.split()))
    except:
        validChars = False
    matrix.append(row)

if len(set(list(map(len, matrix)))) != 1 or not validChars:
    invalid()

T = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

for j in range(len(matrix)):
    for i in range(len(matrix[0])):
        T[i][j] = matrix[j][i]

print("\n".join([" ".join(map(str, row)) for row in T]))
