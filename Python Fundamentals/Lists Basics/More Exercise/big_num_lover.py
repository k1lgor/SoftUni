string = input().split(' ')
largest = ''
string.sort(reverse=True)
largest = ''.join(string)
print(largest)
