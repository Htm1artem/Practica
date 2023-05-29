from collections import defaultdict

def shannon(symbols):
    freq_dict = defaultdict(int)
    total_symbols = len(symbols)
    for symbol in symbols:
        freq_dict[symbol] += 1

    symbols = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    if len(symbols) == 1:
        code = {symbols[0][0]: '0'}
        return code

    total_prob = sum([freq / total_symbols for _, freq in symbols])

    group_prob = 0
    index = 0
    for i, (_, freq) in enumerate(symbols):
        if group_prob >= total_prob / 2:
            break
        group_prob += freq / total_symbols
        index = i

    left_symbols = [symbol for symbol, _ in symbols[:index+1]]
    right_symbols = [symbol for symbol, _ in symbols[index+1:]]

    left_code = shannon(left_symbols)
    right_code = shannon(right_symbols)

    code = {}
    for symbol in left_symbols:
        code[symbol] = '0' + left_code[symbol]
    for symbol in right_symbols:
        code[symbol] = '1' + right_code[symbol]

    return code