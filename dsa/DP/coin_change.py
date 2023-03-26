def coin_change(
    amount,
    coins,
):
    coins.insert(0, 0)
    num_coins = len(coins)
    enumerated_target = amount + 1  # + 1 to include the 0 target amount
    dp = [[float("inf")] * enumerated_target for _ in range(num_coins)]

    for row in range(1, num_coins):
        for target in range(enumerated_target):
            if target == 0:
                dp[row][0] = 0
                continue
            coin = coins[row]
            if target < coin:
                dp[row][target] = dp[row - 1][target]
                continue

            dp[row][target] = min(dp[row - 1][target], dp[row][target - coin] + 1)

    if dp[-1][-1] == float("inf"):
        return -1

    return dp[-1][-1]
