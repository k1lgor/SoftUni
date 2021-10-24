n = int(input())
s1 = 0
s2 = 0
s3 = 0
s4 = 0
avr = 0.0
for _ in range(1, n + 1):
    grade = float(input())
    avr += grade
    if 2.00 <= grade <= 2.99:
        s1 += 1
    if 3.00 <= grade <= 3.99:
        s2 += 1
    if 4.00 <= grade <= 4.99:
        s3 += 1
    if grade >= 5:
        s4 += 1
print(f'Top students: {(s4 / n * 100):.2f}%\nBetween 4.00 and 4.99: {(s3 / n * 100):.2f}%\nBetween 3.00 and 3.99: {(s2 / n * 100):.2f}%\nFail: {(s1 / n * 100):.2f}%\nAverage: {(avr / n):.2f}')
