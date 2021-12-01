data = input()

nums = [int(d) for i, d in enumerate(data) if d.isdigit()]
letters = [d for i, d in enumerate(data) if not d.isdigit()]

result = ''
for i, d in enumerate(str(x) for x in nums):
    if i % 2 == 0:
        result += ''.join(letters[:int(d)])
    letters = letters[int(d):]
print(result)
