# Print "Ping" for multiples of 3
# Print "Pong" for multiples of 5
# Print "PingPong" for multiples of 3 and 5
# If the number even contains 3 or 5, print "Ping" or "Pong" respectively

def ping_pong(n):
    for i in range(1, n + 1):
        result = ""
        if i % 3 == 0 or "3" in str(i):
            result += "Ping"
        if i % 5 == 0 or "5" in str(i):
            result += "Pong"
        if result == "":
            result = str(i)
        print(result)

ping_pong(100)
