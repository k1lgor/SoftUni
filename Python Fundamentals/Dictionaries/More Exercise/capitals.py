ZIP = {k: v for k, v in zip(input().split(', '), input().split(', '))}

for k, v in ZIP.items():
    print(f"{k} -> {v}")
