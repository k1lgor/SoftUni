v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

P1 = p1 * h
P2 = p2 * h
pp = (P1 + P2)
if pp <= v:
    print(
        f'The pool is {(pp / v * 100):.2f}% full. Pipe 1: {(P1 / pp * 100):.2f}%. Pipe 2: {(P2 / pp * 100):.2f}%.')
else:
    print(f'For {h} hours the pool overflows with {abs(pp - v):.2f} liters.')
