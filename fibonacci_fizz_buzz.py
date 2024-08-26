# "Fizz" for multiples of 3
# "Buzz" for multiples of 5
# "FizzBuzz" for both

def fibonacci_fizzbuzz(n):
    a, b = 0, 1
    for _ in range(n):
        result = ""
        if a % 3 == 0:
            result += "Fizz"
        if a % 5 == 0:
            result += "Buzz"
        if result == "":
            result = str(a)
        print(result)
        a, b = b, a + b

fibonacci_fizzbuzz(60)