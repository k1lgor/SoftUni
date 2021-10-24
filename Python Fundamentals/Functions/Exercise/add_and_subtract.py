def add_and_subtract(a, b, c):
    def sum_numbers():
        return a + b
    sum_numbers()
    def subtract():
        print(sum_numbers() - c)
        return sum_numbers() - c
    subtract()
    
add_and_subtract(a=int(input()), b=int(input()), c=int(input()))
