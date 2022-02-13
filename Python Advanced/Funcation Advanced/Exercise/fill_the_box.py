def fill_the_box(h, l, w, *args):
    volume = h * l * w
    cubes = 0
    for x in args:
        if x == 'Finish':
            volume -= cubes
            if volume > 0:
                return f"There is free space in the box. You could put {volume} more cubes."
            else:
                return f"No more free space! You have {abs(volume)} more cubes."
        else:
            cubes += x


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
