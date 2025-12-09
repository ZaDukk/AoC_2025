import re
from shapely.geometry import Polygon, box
from time import process_time

def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers



start = process_time()
with open("input.txt","r") as f:
    inp = [extract_integers(line) for line in f.readlines()]


part1 = 0
for i, a in enumerate(inp):
    for j, b in enumerate(inp):
        if i == j:
            continue
        part1 = max(part1,(abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1))


print(part1)
print(f"{process_time()-start}s")


#qutie slow, takes about 70 seconds for me

part2 = 0
# close the polygon
poly_coords = inp + [inp[0]]
polygon = Polygon(poly_coords)

for i, a in enumerate(inp):
    for j, b in enumerate(inp):
        if i == j:
            continue
        rect = box(min(a[0], b[0]), min(a[1], b[1]),
                   max(a[0], b[0]), max(a[1], b[1]))
        if rect.within(polygon):
            part2 = max(part2,(abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1))


print(part2)
print(f"{process_time() - start}s")
