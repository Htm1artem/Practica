from collections import defaultdict

def huffman(symbols):
    freq_dict = defaultdict(int)
    for symbol in symbols:
        freq_dict[symbol] += 1

    symbols = sorted(freq_dict.items(), key=lambda x: x[1])

    while len(symbols) > 1:
        symbol1, freq1 = symbols.pop(0)
        symbol2, freq2 = symbols.pop(0)

        new_symbol = symbol1 + symbol2
        new_freq = freq1 + freq2

        inserted = False
        for i, (symbol, freq) in enumerate(symbols):
            if new_freq < freq:
                symbols.insert(i, (new_symbol, new_freq))
                inserted = True
                break

        if not inserted:
            symbols.append((new_symbol, new_freq))

    code = {}
    build_code(symbols[0][0], '', code)

    encoded_code = {symbol: code[symbol] for symbol in freq_dict}

    return encoded_code

def build_code(symbol, prefix, code):
    if len(symbol) == 1:
        code[symbol] = prefix
    else:
        build_code(symbol[0], prefix + '0', code)
        build_code(symbol[1:], prefix + '1', code)