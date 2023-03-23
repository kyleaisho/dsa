def edit_distance(word1, word2):
    # Setup a (n + 1) by (m + 1) table
    memo = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    num_rows = len(memo)
    num_cols = len(memo[0])

    # Base Case: Comparing each string prefix with an empty string
    #
    # Top row is comparing word2 to the empty string
    # So for each prefix it takes len(prefix) edits of the empty string
    for i in range(num_cols):
        memo[0][i] = i
    # Left col is comparing word1 to the empty string
    # So for each prefix it takes len(prefix) edits of the empty string
    for i in range(num_rows):
        memo[i][0] = i

    # Already populated row 0 and col 0 so start from index 1
    for row in range(1, num_rows):
        for col in range(1, num_cols):
            # The table has one more row and col than the length
            # of the words for the empty string comparison (base case)
            letter_1 = word1[row - 1]
            letter_2 = word2[col - 1]

            # Subproblem how memo[row][col] is related to previous edit costs
            if letter_1 == letter_2:
                # If the two letters we are looking at match then there is no cost
                # to move from the previous prefix cost to the current
                # previous prefix is diagonal and to the left so [row - 1] <- Left
                # and col - 1 ^ Up. memo[row - 1][col -1]
                memo[row][col] = memo[row - 1][col - 1]
            else:
                # If the letters don't match we will incur a cost to edit, in this case
                # 1 +
                # And it is 1 plus the minimum of the minimum cost of edits so far
                # Previous prefix cost memo[row - 1][col - 1]
                # Delete from word1 memo[row - 1][col]
                # Delete from word2 memo[row][col - 1]
                # A delete from one word is the same as an insert to the second word
                memo[row][col] = 1 + min(
                    memo[row - 1][col - 1], memo[row - 1][col], memo[row][col - 1]
                )
    return memo[-1][-1]
