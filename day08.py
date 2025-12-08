import re
from networkx.utils import UnionFind

def extract_integers(s, allow_negative=False):
    pattern = r"-?\d+" if allow_negative else r"\d+"
    return [int(x) for x in re.findall(pattern, s)]

with open("input.txt","r") as f:
    inp = [line.strip() for line in f]

pts = []
for line in inp:
    nums = extract_integers(line)
    if len(nums) == 3:
        pts.append(tuple(nums))

n = len(pts)

# build  distances
dists = []
for i in range(n):
    x1, y1, z1 = pts[i]
    for j in range(i + 1, n):
        x2, y2, z2 = pts[j]
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        dists.append((dx*dx + dy*dy + dz*dz, i, j))

dists.sort(key=lambda x: x[0])


#part1
uf1 = UnionFind(range(n))
for _, a, b in dists[:1000]:
    uf1.union(a, b)

sizes = sorted([sum(1 for i in range(n) if uf1[i] == r) for r in set(uf1[i] for i in range(n))], reverse=True)
part1 = sizes[0] * sizes[1] * sizes[2]


#part2
uf2 = UnionFind(range(n))
comp = n
last = None

for _, a, b in dists:
    if uf2[a] != uf2[b]:
        uf2.union(a, b)
        comp -= 1
        last = (a,b)
        if comp == 1:
            break


x1 = pts[last[0]][0]
x2 = pts[last[1]][0]
part2 = x1 * x2



print(part1)
print(part2)
