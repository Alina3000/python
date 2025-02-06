while True:

    try:

        a = list(map(int,input("Заполните матрицу, через пробел : ").split()))
        n = int(input())
        matrix = []
        index = 0

        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[index])
                index += 1
            matrix.append(row)

        for row in matrix:
            print(row)

        break
    except:
        print('Ошибка входных данных')