# a
def prime(n):
    for i in range(1, n + 1):
        if n % i != 0:
            return False

    return True


# b
def select_primes(array):
    for number in array:
        if not prime(number):
            array.remove(number)

    return array


print(select_primes([3, 6, 11, 25, 19]))
