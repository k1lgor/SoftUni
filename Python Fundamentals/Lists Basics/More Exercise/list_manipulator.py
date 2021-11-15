import sys

numbers_as_string = input().split()
command = input()
numbers = [int(str_num) for str_num in numbers_as_string]
max_value = sys.maxsize
min_value = -sys.maxsize - 1

while command != "end":
    command = command.split()
    if command[0] == "exchange":
        index = int(command[1])
        if index < 0 or index >= len(numbers):
            print("Invalid index")
        elif index != len(numbers):
            first_half = numbers[:index+1]
            second_half = numbers[index + 1::]
            numbers = second_half + first_half

    elif command[0] == "max":
        current_max = min_value
        for i in range(len(numbers)):
            if command[1] == "odd":
                current_num = numbers[i]
                if current_num % 2 == 1 and current_num >= current_max:
                    max_index = i
                    current_max = current_num
            elif command[1] == "even":
                current_num = numbers[i]
                if current_num % 2 == 0 and current_num >= current_max:
                    max_index = i
                    current_max = current_num
        if current_max > min_value:
            print(max_index)
        else:
            print("No matches")

    elif command[0] == "min":
        current_min = max_value
        for i in range(len(numbers)):
            if command[1] == "odd":
                current_num = numbers[i]
                if current_num % 2 == 1 and current_num <= current_min:
                    min_index = i
                    current_min = current_num
            elif command[1] == "even":
                current_num = numbers[i]
                if current_num % 2 == 0 and current_num <= current_min:
                    min_index = i
                    current_min = current_num

        if current_min < max_value:
            print(min_index)
        else:
            print("No matches")

    if command[0] in ["first", "last"]:
        line_even = []
        line_odd = []
        num = int(command[1])

        if num > len(numbers):
            print("Invalid count")
        else:
            for i in numbers:
                if i % 2 == 0:
                    line_even.append(i)
                else:
                    line_odd.append(i)

            if command[2] == "even":
                if not line_even:
                    print(line_even)
                elif command[0] == "first":
                    print(line_even[:num])
                elif command[0] == "last":
                    if int(command[1]) >= len(line_even):
                        print(line_even)
                    else:
                        last_num = len(line_even) - num
                        print(line_even[last_num::])

            if command[2] == "odd":
                if not line_odd:
                    print(line_odd)
                elif command[0] == "first":
                    print(line_odd[:num])
                elif command[0] == "last":
                    if int(command[1]) >= len(line_odd):
                        print(line_odd)
                    else:
                        last_num = len(line_odd) - num
                        print(line_odd[last_num::])

    command = input()
print(numbers)