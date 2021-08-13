# FizzBuzz
# Juha Raintor
# 21-07-2021 one late evening

def fizz(num):
    if num % 3 == 0:
        return True

def buzz(num):
    if num % 5 == 0:
        return True

def main():

    number = 1

    while number <= 100:

        if fizz(number) and buzz(number) == True:
            print("Fizz Buzz")
        
        elif fizz(number) == True:
            print("Fizz")

        elif buzz(number) == True:
            print('Buzz')

        else:
            print(number)

        number += 1


if __name__ == "__main__":
    main()