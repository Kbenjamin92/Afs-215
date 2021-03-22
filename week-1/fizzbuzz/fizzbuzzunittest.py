def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzBuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num


result = fizz_buzz(4)
print(result)