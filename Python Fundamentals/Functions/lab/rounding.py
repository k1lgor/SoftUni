def Rounding(numbers):
    rounded = [round(num) for num in numbers]
    print(rounded)
    return rounded
    
Rounding(numbers=list(map(float, input().split())))
