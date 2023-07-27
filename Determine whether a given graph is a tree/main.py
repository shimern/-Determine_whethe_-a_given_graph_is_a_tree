import sys

v = []
sg = ""
st = set()
sk = []

flag = False

try:
    #The graph is read from a file, where it is presented as an adjacency table
    with open("...") as f:
        n = int(f.readline())

        for line in f:
            v.append(line.strip())

        # Вывод графа
        for i in range(1, n + 1):
            print(i, v[i])

        sk.append(0)
        st.add(1)

        for char in v[1]:
            sk.append(int(char))

        # Проверка на цикл
        while sk[-1]:
            i = sk.pop()

            c = 0
            for char in v[i]:
                if int(char) in st:
                    c += 1
                else:
                    sk.append(int(char))

                if int(char) == i:  # Проверка на петли
                    flag = True
                    break

            if c >= 2:
                flag = True
                break

            st.add(i)

        if len(st) != n:
            flag = True

        if flag:
            print("Граф - не дерево")
        else:
            print("Граф - дерево")

except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print("Произошла ошибка:", e)