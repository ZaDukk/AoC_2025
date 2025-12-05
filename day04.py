from collections import deque
vectorsD = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]



with open("in.txt", "r") as f:
    inp = [line.rstrip("\n") for line in f]


grid = [list(line) for line in inp]
H = len(grid)



def neighbors(g, r, c):
    for dr, dc in vectorsD:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(g) and 0 <= nc < len(g[nr]):
            yield nr, nc


adj = [[0]*len(row) for row in grid]
q = deque()
for r in range(H):
    for c in range(len(grid[r])):
        if grid[r][c] == '@':
            a = 0
            for nr, nc in neighbors(grid, r, c):
                if grid[nr][nc] == '@':
                    a += 1
            adj[r][c] = a
            if a < 4:
                q.append((r, c))

# part 1
part1 = sum(1 for r in range(H) for c in range(len(grid[r])) if grid[r][c] == '@' and adj[r][c] < 4)

# part 2
g2 = [row[:] for row in grid]
removed = 0
while q:
    r, c = q.popleft()
    if g2[r][c] != '@':
        continue
    g2[r][c] = '.'
    removed += 1
    for nr, nc in neighbors(g2, r, c):
        if g2[nr][nc] == '@':
            adj[nr][nc] -= 1
            if adj[nr][nc] == 3:   # just became removable
                q.append((nr, nc))

print(part1)
print(removed)
