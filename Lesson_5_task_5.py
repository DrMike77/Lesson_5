from random import randrange
n = [randrange(1, 100) for i in range(10)]
a = open('n_05.txt', 'w')
a.write(" ".join(map(str, n)))
with open('n_05.txt') as b:
    numbers = b.read().split()
print(sum(float(x) for x in n))