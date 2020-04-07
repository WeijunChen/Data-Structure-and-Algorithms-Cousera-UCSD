
import sys


# Fibonacci Number

def calc_fib(n):
    num_list = [0, 1]
    
    if n <= 1:
        return n
    else:
        for i in range(2,n+1):
            num_list.append(num_list[i-1] + num_list[i-2])
            
    return num_list[n]

n = int(input())
print(calc_fib(n))


# Last Digit of a Large Fibonacci Number

def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n
    
    previous = 0
    current = 1
    for i in range(n):
        previous, current = current % 10, (previous + current) % 10
    return current

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_fast(n))



# Greatest Common Divisor

def gcd_naive(a, b):
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(gcd_naive(a, b))


def gcd_fast(a, b):
    dividend = a if (a >= b) else b
    divisor = a if (a <= b) else b

    while divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return dividend

   
# Least Common Multiple
def lcm_naive(a, b):
    for i in range(1, a*b+1):
        if i % a == 0 and i % b ==0:
            return i 
    return a*b

def lcm_fast(a, b):
    return (a * b) // gcd_fast(a, b) 


