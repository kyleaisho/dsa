def justify(text, width):
    matrix = generate_matrix(text, width)
    splits, cost = calculate_splits(matrix)
    unpadded_lines = get_unpadded_lines(text, splits)
    return pad_lines(unpadded_lines, width)


def get_padded_spaces(line, width):
    words = len(line)
    line_width = 0
    for word in line:
        line_width += len(word)
    natural_spaces = words - 1
    return width - (line_width + natural_spaces)


def badness(line, width):
    padded_spaces = get_padded_spaces(line, width)

    if padded_spaces < 0:
        return float("inf")

    return padded_spaces**2


def generate_matrix(text, width):
    n = len(text)
    matrix = [[float("inf")] * n for _ in range(n)]

    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            if j < i:
                continue
            words = text[i : j + 1]
            matrix[i][j] = badness(words, width)

    return matrix


def calculate_splits(matrix):
    n = len(matrix)
    costs = [float("inf")] * n
    costs.append(0)
    splits = [0] * n

    i = n - 1
    while i >= 0:
        j = n - 1
        min_cost = float("inf")
        end_interval = j + 1
        while j >= i:
            cost = matrix[i][j]

            curr_cost = cost + costs[j + 1]

            if curr_cost < min_cost:
                min_cost = curr_cost
                end_interval = j + 1
            j -= 1
        splits[i] = end_interval
        costs[i] = min_cost
        i -= 1

    return splits, costs


def get_unpadded_lines(text, splits):
    lines = []
    # Remove duplicates
    splits = list(dict.fromkeys(splits))
    prev_split = 0
    for split in splits:
        lines.append(text[prev_split:split])
        prev_split = split

    return lines


def pad_lines(text, width):
    lines = []

    for words in text:
        spaces = get_padded_spaces(words, width)
        num_word_seperators = len(words) - 1

        if num_word_seperators < 1:
            padding = width - len(words[0])
            line = [words[0], " " * padding]
            lines.append("".join(line))
            continue

        q = spaces // num_word_seperators
        line = []
        for idx, word in enumerate(words):
            line.append(word)

            if spaces > 0:
                padding = " "
                if spaces <= q:
                    padding = padding * spaces
                    spaces = 0
                else:
                    padding = padding * q
                    spaces -= q

                line.append(padding)
            if idx < len(words) - 1:
                line.append(" ")
        lines.append("".join(line))
    return lines


def justify_recursive(text, width):
    memo = {}
    memo[len(text)] = 0
    child = {}
    calculate_costs(text, width, 0, memo, child)

    splits = []
    index = 0
    while index < len(text):
        splits.append(child[index])
        index = child[index]

    unpadded_lines = get_unpadded_lines(text, splits)
    return pad_lines(unpadded_lines, width)


def calculate_costs(text, width, i, memo, child):
    if i in memo:
        return memo[i]
    n = len(text)
    memo[i] = float("inf")
    if i not in child:
        child[i] = None
    for j in range(i + 1, n + 1):
        line = text[i:j]
        cost = badness(line, width)
        j_cost = calculate_costs(text, width, j, memo, child)
        if cost + j_cost < memo[i]:
            memo[i] = cost + memo[j]
            child[i] = j
    return memo[i]
