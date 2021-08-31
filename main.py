import math


def eit(number):
    if number <= 0 or number - int(number) > 0:
        return 0
    else:
        return 1


# x = pow(10, 25)
x = 1000

aa = (2 * x + pow(-1, x) - 1) / 6
a = round(aa, 0)

cc = ((-1 + (math.sqrt(-2 + 3 * aa))) / 3)
c = -round(cc * -1, 0)
m = c
n = a - 1
s = 0
k = 0
t = 0

for j in range(8, int(n)):
    for i in range(1, int(m)):
        r = eit(
            (4 * j - pow(-1, j) + ((2 * i + 1) * pow(-1, i + j)) + ((2 * i - 1) * pow(-1, i)) - (12 * i * i) + 5) / (
                    12 * i + 6 - (2 * pow(-1, i))))
        k = k + r
    s = s + eit(k)
    k = 0

pp = (2 * x + pow(-1, x) - 6 * s + 5) / 6
p = math.trunc(pp)
print("valor de pi(x) = ", p)
