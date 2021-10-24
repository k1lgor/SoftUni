string = [ele for ele in input().split()]
pali = input()

print([ele for ele in string if ele == ele[::-1]])
print(f'Found palindrome {string.count(pali)} times')
