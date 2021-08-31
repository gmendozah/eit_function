import math


def eit(x):
    if x <= 0 or x - x > 0:
        return 0
    else:
        return 1


xrange = range

# x = pow(10, 25)
x = 100

aa = (2 * x + pow(-1, x - 1)) / 6
a = math.trunc(aa)

cc = ((-1 + (math.sqrt(-2 + 3 * aa))) / 3)
c = -math.trunc((cc * (-1)))
m = c
n = a - 1
sum = 0
k = 0
t = 0

for j in range(8, n):
    for i in range(1, m):
        r = eit((4 * j - ((-1) ^ j) + ((2 * i + 1) * pow(-1, i + j) + ((2 * i - 1) * pow(-1, i) - (12 * i * i) + 5) / (
                12 * i + 6 - (2 * pow(-1, i))))))
        k = k + r
    sum = sum + eit(k)
    k = 0

pp = (2 * x + pow(-1, x) - 6 * sum + 5) / 6
p = math.trunc(pp)
print("valor de pi(x) = ", p)
