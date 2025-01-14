# For prime numbers, print "Prime" instead of the number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_buzz(n):
    for i in range(1, n + 1):
        if is_prime(i):
            print("Prime")
        else:
            print(i)

prime_buzz(50)