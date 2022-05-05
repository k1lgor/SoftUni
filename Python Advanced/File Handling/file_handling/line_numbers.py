from collections import Counter


def line_numbers():
    with open('text.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
        for row, line in enumerate(input_file, start=0):
            words_counter = (Counter(x for x in line if x.isalpha()))
            punc_marks = (Counter(x for x in line if x in [
                          "-", ",", ".", "!", "?", "'", "`"]))
            output_file.write(
                f"Line {row + 1}: {line} ({words_counter.total()})({punc_marks.total()})\n")


line_numbers()
