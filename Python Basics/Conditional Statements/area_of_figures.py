import math

fig = input()
if fig in ["square", "rectangle"]:
    print(float(input()) ** 2)
elif fig == "circle":
    print(math.pi * (float(input())) ** 2)
elif fig == "triangle":
    print(float(input()) ** 2 / 2)
