
number = int(input("Enter a number:"))

def FizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0 :
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"  
    else:
      return "Not a Fizz-buzz number"

print(FizzBuzz(number))