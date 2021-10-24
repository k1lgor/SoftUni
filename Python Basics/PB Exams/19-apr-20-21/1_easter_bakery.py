flour = float(input()) # kg
kg_flour = float(input())
kg_sugar = float(input())
eggshell = int(input())
yeast_packets = int(input())

sugar = flour * 0.75
eggs = flour * 1.1
yeast = sugar * 0.2
ttl = flour * kg_flour + sugar * kg_sugar + eggshell * eggs + yeast * yeast_packets

print(f'{ttl:.2f}')