
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



   

            