n = int(input())
p = int(input())
courses = 0
if n <= p:
    courses += 1
while n >= p:
    courses += 1
    n -= p
    if n < p:
        if n == 0:
            break
        else:
            courses += 1
print(courses)