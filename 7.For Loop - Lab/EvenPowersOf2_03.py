n = int(input())

# всички степени от 0 до n
# начало: 0
# край: n
# промяна: + 2
# повтаряме: печатаме 2 на дадената степен
for step in range(0, n + 1, 2):
    print(2 ** step)