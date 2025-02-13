while True:

    try:

        a = list(map(int,input("введите последовательность убывающих чисел a через пробел : ").split()))
        b = list(map(int,input("введите последовательность убывающих чисел b через пробел : ").split()))


        if len(a)!=len(b):
            print('Последовательности не одиноковой длинны!!!')

        a.extend(b)
        a.sort(reverse=True)
        print(a)
        break
    except:
        print("oшибка")