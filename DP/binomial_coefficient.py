def binomial_coefficient(n, k):
    """
    n choose k
    """
    if n == k or k == 0:
        return 1
    table = [[1] * (n + 1) for _ in range(k + 1)]

    # Walk down the table in the top right quadrant
    row = 1
    while row < len(table):
        col = row + 1

        while col < len(table[0]):
            top_left = table[row][col - 1]
            top_right = table[row - 1][col - 1]
            table[row][col] = top_left + top_right

            col += 1

        row += 1
    return table[k][n]
