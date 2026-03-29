# FizzBuzz with a Twist
# Write a Python function called fizzbuzz that takes a number n as input and prints numbers from 1 to n with these rules:

# Print "Fizz" for multiples of 3
# Print "Buzz" for multiples of 5
# Print "FizzBuzz" for multiples of both 3 and 5
# Print "AntiFizz" for multiples of 7
# Print the number itself if none of the above apply
 
def fizzbuzz(n):
    if n <= 0:
        print("Invalid Input")
        return  

    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:  # check first! 
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 7 == 0:
            print("AntiFizz")
        else:
            print(num)

n = 20
fizzbuzz(n) 
