unsatisfied = int(input())
taskname = ''
avr = 0
counter = 0
unsat_counter = 0
lastproblem = ''
while unsat_counter < unsatisfied:
    taskname = input()
    if taskname == 'Enough':
        print(
            f'Average score: {(avr / counter):.2f}\nNumber of problems: {counter}\nLast problem: {lastproblem}')
        break
    grade = int(input())
    if grade <= 4:
        unsat_counter += 1
    if unsat_counter >= unsatisfied:
        print(f'You need a break, {unsat_counter} poor grades.')
        break
    avr += grade
    lastproblem = taskname
    counter += 1
