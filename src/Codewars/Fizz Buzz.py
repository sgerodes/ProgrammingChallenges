def solution(number):
    number-=1
    return [int(number/3*(4/5)),int(number/5*(2/3)),int(number/15)]

def fizzbuzz(n):
    return ["Fizz"[n%3*4:]+"Buzz"[n%5*4:] or n for n in range(1,n+1)]