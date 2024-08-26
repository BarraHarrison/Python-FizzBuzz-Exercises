# FizzBuzz
def fizz_buzz(n):
    # Define the mapping dictionary
    fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}

    # Iterate over the range from 1 to n (inclusive)
    for i in range(1, n + 1):
        result = ""

        # Check if it is divisible based on dictionary keys
        for key in fizz_buzz_dict:
            if i % key == 0:
                result += fizz_buzz_dict[key]

        # If the result is empty, it's neither Fizz or Buzz so return the number 
        if result == "":
            result = str(i)

        print(result)

# Example usage:
if __name__ == "__main__":
    fizz_buzz(100)