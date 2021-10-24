def dataTypes():
    if ele1 == 'int':
        print(int(ele2) * 2)
    elif ele1 == 'real':
        print(f'{(float(ele2) * 1.5):.2f}')
    elif ele1 == 'string':
        print(f'${ele2}$')
        
ele1, ele2 = input(), input()
dataTypes()
