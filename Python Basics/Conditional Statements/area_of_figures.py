import math

fig = input()
if fig == "square":
    print(float(input()) ** 2)
elif fig == "rectangle":
    print(float(input()) * float(input()))
elif fig == "circle":
    print(math.pi * (float(input())) ** 2)
elif fig == "triangle":
    print(float(input()) * float(input()) / 2)