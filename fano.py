from collections import defaultdict

def fano(symbols):
    freq_dict = defaultdict(int)
    for symbol in symbols:
        freq_dict[symbol] += 1

    symbols = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    if len(symbols) == 1:
        code = {symbols[0][0]: '0'}
        return code

    total_freq = sum([freq for _, freq in symbols])

    group_freq = 0
    for i, (_, freq) in enumerate(symbols):
        if group_freq >= total_freq / 2:
            break
        group_freq += freq

    left_symbols = dict(symbols[:i])
    right_symbols = dict(symbols[i:])

    left_code = fano(left_symbols)
    right_code = fano(right_symbols)

    code = {}
    for symbol, freq in left_symbols.items():
        code[symbol] = '0' + left_code[symbol]
    for symbol, freq in right_symbols.items():
        code[symbol] = '1' + right_code[symbol]

    return code