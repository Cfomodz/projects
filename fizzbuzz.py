# A basic fizzbuzz example written in Python 3
# Written orriginally by David Ashby
# Problem: "Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."
# Solution:

for i in range(0,100):
    string = ""
        if not i % 3 == 0 and not i % 5 == 0:
            print(str(i))
        else:
            if i % 3 == 0:
                string += "Fizz"
            if i % 5 == 0:
                string += "Buzz"
            print(string)

            

# Or if you do not recognize 0 as being divisible by 3 and/or 5:

for i in range(0,100):
    string = ""
    if i == 0:
        print(str(i))
    else:
        if not i % 3 == 0 and not i % 5 == 0:
            print(str(i))
        else:
            if i % 3 == 0:
                string += "Fizz"
            if i % 5 == 0:
                string += "Buzz"
            print(string)

# Or if the question in question were more complex and you needed more robust code that would allow you to execute more complex logic against a set of inputs that isn't so easily tested in 1 line:

for i in range(0,100):
    div_five = False
    div_three = False
    if i == 0:
        print(str(i))
    else:
        if i % 3 == 0:
            div_three = True
        if i % 5 == 0:
            div_five = True
        if div_three and not div_five:
            print("Fizz")
        if div_five and not div_three:
            print("Buzz")
        if div_three and div_five:
            print("FizzBuzz")
        if not div_three and not div_five:
            print(str(i))
