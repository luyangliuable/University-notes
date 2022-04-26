import math

def coin_change(c, v: int) -> int:
    memo = [None]*(v+1)
    if v == 0:
        return 0

    if memo[v] == None:
        min_coins = math.inf
        for i in range(len(c)):
            if c[i] <= v:
                min_coins = min(min_coins, 1 + coin_change(c, v-c[i]))


        memo[v] = min_coins

    return memo[v]

