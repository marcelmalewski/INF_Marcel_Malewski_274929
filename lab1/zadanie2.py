import math
import random

# a ----------------------
v1 = [3, 8, 9, 10, 12]
v2 = [8, 7, 7, 5, 6]

v_sum = []

# sumowanie
for i in range(len(v1)):
    v_sum.append(v1[i] + v2[i])
print(v_sum)

# pow wsporzednych
v_iloczyn_wspolrzedne = []
for i in range(len(v1)):
    v_iloczyn_wspolrzedne.append(v1[i] * v2[i])
print(v_iloczyn_wspolrzedne)

# b ------------------------------------------
# iloczyn
v_iloczyn = 0
for i in range(len(v1)):
    v_iloczyn += v1[i] * v2[i]
# print(v_iloczyn)


# c ------------------------------------------
def zrob_dlugosc_euklidesowa(wektor):
    result = 0
    for number in wektor:
        result += number * number
    return math.sqrt(result)


# print(zrob_dlugosc_euklidesowa(v1))
# print(zrob_dlugosc_euklidesowa(v2))

# d ------------------------------------------------
# print(random.randint(1, 100))
randomNumbers = [random.randint(1, 100) for i in range(0, 50)]
print(randomNumbers)

# e --------------------------------------------------
random_min = min(randomNumbers)
random_max = max(randomNumbers)

print(random_min)
print(random_max)


