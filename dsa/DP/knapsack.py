def fill_knapsack(capacity, values, weights, index=0, memo={}):
    if index >= len(values) or capacity <= 0:
        return 0

    profits_include = 0
    if weights[index] <= capacity:
        profits_include = values[index] + fill_knapsack(
            capacity - weights[index], values, weights, index + 1, memo
        )

    profits_exclude = fill_knapsack(capacity, values, weights, index + 1, memo)

    memo[index] = max(profits_include, profits_exclude)

    return memo[index]
