
def div(number):
    if number/3:
        return "Fizz"
    elif number/5:
        return "Buzz"
    elif number/3 and number/5:
        return "FizzBuzz"
    else:
        return "Not a FizzBuzz number"
    
number = 15
div(number)