import math

def coin_change(c, v: int) -> tuple:
    memo = [( None, [] )]*(v+1)
    coins = []
    if v == 0:
        return [0, []]

    if memo[v][0] == None:
        min_coins = (math.inf, [])
        for i in range(len(c)):
            if c[i] <= v:
                tmp = coin_change(c, v-c[i])
                min_coins = (1 + tmp[0], tmp[1] + [ c[i] ])

        memo[v] = min_coins

    return memo[v]

coins = [1,2,3,4]
v = 12

res = coin_change(coins, v)
print('It takes', res, 'coins to make', v, 'amount')
