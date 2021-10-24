from math import floor as fl
word = input()
best_word = ''
asci_sum = 0
best_sum = 0
while word != 'End of words':
    name_len = len(word)
    for i, d in enumerate(word):
        asci_sum += ord(d)
    if word[0] in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
        asci_sum *= name_len
    else:
        asci_sum = fl(asci_sum / name_len)

    if asci_sum >= best_sum:
        best_sum = asci_sum
        best_word = word
    word = input()
    asci_sum = 0
print(f'The most powerful word is {best_word} - {best_sum}')
