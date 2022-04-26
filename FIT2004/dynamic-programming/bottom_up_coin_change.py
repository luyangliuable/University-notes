import math


def coin_change(c, V: int):
    # min_coins = [( math.inf, [] )]*(V)
    min_coins = [(math.inf, []) for i in range(V+1)]

    min_coins[0] = (0, [])

    for v in range(V+1):
        for i in range(len(c)):
            if c[i] <= v:
                if min_coins[v][0] < 1 + min_coins[v-c[i]][0]:
                    pass
                else:

                    min_coins[v] = (1 + min_coins[v-c[i]][0], min_coins[v-c[i]][1] + [ c[i] ])

    # V-1 because 0 is for making coins so V-1 is for V number of coins
    return min_coins[V]

coins = [1,2,3,4]
v = 12

res = coin_change(coins, v)
print('It takes', res[0], 'coins to make', v, 'amount')

print("It requires", end=" ")

for i in range(len(res[1])):
    print(res[1][i], "$" + str(coins[i]), "coins", end=", ")

print("to make this happen")



