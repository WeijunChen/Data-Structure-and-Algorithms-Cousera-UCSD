''' Maximum Pairwise Product Problem
Find the maximum product of two distinct num- bers in a sequence of non-negative integers.
'''




def max_pair_product(n, a):
    product = 0
    for i in range(n):
        for j in range(i+1, n):
            product = max(product, a[i]*a[j])
    return product

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == n)

    print(max_pair_product(n, a))



def max_pair_product_fast(n, numbers):
    max_index = 0
    for i in range(max_index+1, n):
        if numbers[i] > numbers[max_index]:
            max_index = i
            
    second_max_index = 0
    for j in range(second_max_index+1, n):
        if numbers[j] != numbers[max_index] and numbers[j] > numbers[second_max_index]:
            second_max_index = j
    return numbers[max_index] * numbers[second_max_index]

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == n)

    print(max_pair_product_fast(n, a))
        
