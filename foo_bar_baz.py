# for multiples of 3 print "foo"
# for multiples of 5 print "bar"
# for multiples of 7 print "baz"
# for mutiples of both 3 and 5 print "foobar"
# for multiples of 3 and 7 print "foobaz"
# for multiples of 5 nd 7 print "barbaz"
# for mutiples of 3, 5 and 7 print "foobarbaz"

def foo_bar_baz(n):
    for i in range(1, n + 1):
        result = ""
        if i % 3 == 0:
            result += "Foo"
        if i % 5 == 0:
            result += "Bar"
        if i % 7 == 0:
            result += "Baz"
        if result == "":
            result = str(i)
        print(result)

foo_bar_baz(100)