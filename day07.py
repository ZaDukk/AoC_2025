from collections import deque
from functools import lru_cache

with open("input.txt", "r") as f:
    grid = [list(line.rstrip("\n")) for line in f.readlines()]

h = len(grid)

sr = sc = None
for r in range(h):
    for c in range(len(grid[r])):
        if grid[r][c] == "S":
            sr, sc = r, c
            break
    if sr is not None:
        break


q = deque([(sr, sc)])
visited = set()
splits = 0

while q:
    r, c = q.popleft()
    if (r, c) in visited:
        continue
    visited.add((r, c))

    nr = r + 1
    if nr >= h:
        continue
    if c >= len(grid[nr]):
        continue

    cell = grid[nr][c]

    if cell == ".":
        q.append((nr, c))

    elif cell == "^":
        splits += 1

        if c - 1 >= 0 and c - 1 < len(grid[nr]):
            q.append((nr, c - 1))
        if c + 1 < len(grid[nr]):
            q.append((nr, c + 1))

print(splits)


@lru_cache(maxsize=None)
def ways(r, c):
    if r >= h or c < 0 or c >= len(grid[r]):
        return 1

    ch = grid[r][c]

    if ch == '^':
        return ways(r + 1, c - 1) + ways(r + 1, c + 1)
    else:
        return ways(r + 1, c)


print(ways(sr + 1, sc))
