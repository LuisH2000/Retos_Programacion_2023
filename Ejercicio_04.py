'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
'''
import math

def isPrime(number: int):
    if number < 1:
        return False
    devider = number//2
    while devider > 1:
        if number % devider == 0:
            return False
        devider -= 1
    return True

def isEven(number: int):
    return number >= 0 and number % 2 == 0


def is_perfect_square(number):
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number

def isFibonacci(number: int):
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    return a == number
'''
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
'''

def the_number_is_prime_even_fibo(number: int):
    numberIs = f"The number {number} "
    if isEven(number):
        numberIs += "is Even, "
    else:
        numberIs += "is Not Even, "
    
    if isPrime(number):
        numberIs += "is Prime, "
    else:
        numberIs += "is Not Prime, "

    if isFibonacci(number):
        numberIs += "is Fibonacci"
    else:
        numberIs += "is Not Fibonacci"

    print(numberIs)

the_number_is_prime_even_fibo(2)
the_number_is_prime_even_fibo(7)
the_number_is_prime_even_fibo(0)
the_number_is_prime_even_fibo(1)
the_number_is_prime_even_fibo(-2)