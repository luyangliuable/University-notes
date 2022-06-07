def single_knapsack(value: list, weight:list, capacity: int) -> int:
    v = value
    w = weight

    if len(value) != len(weight):
        raise Exception("not enough value for length")

    DP = [ [0 for _ in range(capacity+1)] for _ in range(len(weight)+1)]

    # Need to ignore when i == 0 on DP because
    # Need to ignoree when c == 0 because 0 capacity can't fit anything
    for i in range(len(weight)+1):
        for c in range(capacity+1):
            if i == 0 or c ==0:
                DP[i][c] = 0
            elif w[i-1] > c:
                DP[i][c] = DP[i-1][c]
            else:
                DP[i][c] = max(DP[i-1][c], v[i-1] + DP[i-1][c-w[i-1]])

            print_matrix(DP)
            print("\n")

    return DP[-1][capacity]


def unbounded_knapsack(value: list, weight:list, capacity: int) -> int:
    v = value
    w = weight

    DP = [0 for _ in range(capacity + 1)]

    for c in range(capacity + 1):
        for i in range(len(weight)):
            if c >= w[i]:
                DP[c] = max(DP[c], v[i] + DP[c-w[i]])

    return DP[-1]


def knapsack(val, wt, W):
    n = len(val)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]

def print_matrix(M):
    for l in M:
        print(str(l))


if __name__ == "__main__":
    value = [5, 6, 10, 20]
    w = [1, 3, 4, 8]
    capacity = 12

    # res = knapsack(value, w, capacity)
    # res = unbounded_knapsack(value, w, capacity)
    res = single_knapsack(value, w, capacity)
    print(res)
