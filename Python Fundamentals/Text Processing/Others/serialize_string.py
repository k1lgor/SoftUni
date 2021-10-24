string = input()
total_indexes = []

for i in string:
    index = 0
    start = 0
    letter = ''
    indexes = []
    while start < len(string):
        
        index = string.find(i, start)
        total_indexes.append(index)
        if index != -1:
            start = index + 1
            indexes.append(index)
        if indexes in total_indexes:
            break
        else:
            break
    print(f'{i}:' + '/'.join([str(x) for x in indexes]))
        
        
        
    
    