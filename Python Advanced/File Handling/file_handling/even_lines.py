def replace(result):
    for char in ["-", ",", ".", "!", "?"]:
        result = result.replace(char, "@")
    return result


def reverse(even_lines):
    for row in even_lines:
        for char in row:
            result = ' '.join(reversed(char.strip().split()))
            print(replace(result))


def reader_even_lines():
    even_lines = []
    with open('text.txt', 'r') as file:
        even_lines.extend([line]
                          for row, line in enumerate(file) if row % 2 == 0)
    return reverse(even_lines)


reader_even_lines()
