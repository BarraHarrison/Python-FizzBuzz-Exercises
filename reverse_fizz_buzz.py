# Given a list of strings containing "Fizz", "Buzz", "FizzBuzz", and numbers 
# return the corresponding original number list. For example, ["1", "2", "Fizz", "4", "Buzz"] should return [1, 2, 3, 4, 5].

def reverse_fizz_buzz(list):
    result = []
    for item in list:
        if item == "FizzBuzz":
            result.append(15)
        elif item == "Fizz":
            result.append(3)
        elif item == "Buzz":
            result.append(5)
        else:
            result.append(int(item))
        return result

print(reverse_fizz_buzz(["1", "2", "Fizz", "4", "Buzz"]))