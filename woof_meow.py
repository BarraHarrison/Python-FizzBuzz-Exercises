# For multiples of 2 print "Woof"
# For multiples of 4 print "Meow"
# Any multiple fo 4 will be a multiple of 2 anyways
# For multiples of 2 and 4 print"WoofMeow"

def woof_meow(n):
    for i in range(1, n + 1):
        if i % 4 == 0:
            print("WoofMeow")
        elif i % 2 == 0:
            print("Woof")
        else:
            print(i)

woof_meow(60)