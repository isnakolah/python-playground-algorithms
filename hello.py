def fizz_buzz(limit):
    for num in range(limit):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 5 == 0:
            print("buzz")
        elif num % 3 == 0:
            print("fizz")
        else:
            continue


fizz_buzz(100)
