def stair_climb(n, stair, memo):
    if stair in memo:
        return memo[stair]

    memo[stair] = 0
    if stair == n:
        memo[stair] = 1
        return memo[stair]
    if stair > n:
        memo[stair] = 0
        return memo[stair]

    # Climb one stair
    memo[stair] += stair_climb(n, stair + 1, memo)
    # Climb two stairs
    memo[stair] += stair_climb(n, stair + 2, memo)

    return memo[stair]
