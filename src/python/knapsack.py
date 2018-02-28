# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    keep = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Build table K[][] in bottom up manner
    for i in range(0, n):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i] <= w and (val[i] + K[i - 1][w - wt[i]] > K[i - 1][w]):
                K[i][w] = val[i] + K[i - 1][w - wt[i]]
                keep[i][w] = 1
            else:
                K[i][w] = K[i - 1][w]
                keep[i][w] = 0

    F = W
    items = []
    for i in range(n-1, 0, -1):
        if keep[i][F] == 1:
            items.append(i)
            F -= wt[i]
    return items, K[n][W]