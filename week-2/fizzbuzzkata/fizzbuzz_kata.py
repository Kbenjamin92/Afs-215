def fizz_buzz_kata(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'fizzbuzz' 
    elif num % 3 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    elif num == 1:
        return 1
    elif num == 2:
        return 2
  

