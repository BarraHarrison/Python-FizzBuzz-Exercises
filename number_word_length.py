# If the length is even, print "EvenLength"
# If the length is odd, print "OddLength"
# If the number is prime, print "PrimeLength"

import inflect

def number_word_length(n):
    p = inflect.engine()

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(1, n + 1):
        word = p.number_to_words(i)
        length = len(word.replace("-", "").replace(" ", ""))
        if is_prime(i):
            print(f"{i}: PrimeLength")
        elif length % 2 == 0:
            print(f"{i}: EvenLength")
        else:
            print(f"{i}: OddLength")

number_word_length(60)
