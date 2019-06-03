#The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.

def get_change(m):
    coins = 0
    for coin in [10,5,1]:
        coins += m//coin
        m %= coin
    coins
    return coins
