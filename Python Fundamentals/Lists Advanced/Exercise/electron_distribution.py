electrons = int(input())
n = 1
LIST = []
while electrons >= 2 * n ** 2:
    shell = 2 * n ** 2
    LIST.append(shell)
    electrons -= shell
    n += 1
if electrons != 0:
    LIST.append(electrons)    
print(LIST)