from collections import defaultdict
from fano import fano
from shennon import shannon
from huffman import huffman

symbols = "AAAABBBBBBCCDDDEEEEE"
freq_dict = defaultdict(int)
for symbol in symbols:
    freq_dict[symbol] += 1

code = fano(symbols)

print('Алгоритм Фано:')
print(code)
print()

symbols = "AAAABBBBBBCCDDDEEEEE"
freq_dict = defaultdict(int)
for symbol in symbols:
    freq_dict[symbol] += 1

code = shannon(symbols)

print('Алгоритм Шеннона:')
print(code)
print()

symbols = "AAAABBBBBBCCDDDEEEEE"
freq_dict = defaultdict(int)
for symbol in symbols:
    freq_dict[symbol] += 1

code = huffman(symbols)

print('Алгоритм Хаффмана:')
print(code)