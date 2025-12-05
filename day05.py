import re

def extract_integers(s, allow_negative=False):
    pattern = r"-?\d+" if allow_negative else r"\d+"
    return [int(x) for x in re.findall(pattern, s)]


with open("input.txt","r") as f:
    inp = [line.strip() for line in f]

ranges = []
ids = []
i = 0

# ranges
while i < len(inp) and inp[i] != "":
    nums = extract_integers(inp[i])
    ranges.append((nums[0], nums[1]))
    i += 1

# ids
for j in range(i+1, len(inp)):
    nums = extract_integers(inp[j])
    if nums:
        ids.append(nums[0])

# merge ranges
ranges.sort()
merged = []
for a, b in ranges:
    if not merged or a > merged[-1][1] + 1:
        merged.append([a, b])
    else:
        if b > merged[-1][1]:
            merged[-1][1] = b

#p1

import bisect
starts = [r[0] for r in merged]
ends = [r[1] for r in merged]

fresh = 0
for x in ids:
    pos = bisect.bisect_right(starts, x) - 1
    if pos >= 0 and starts[pos] <= x <= ends[pos]:
        fresh += 1

print(fresh)

# p2
coverage = sum(b - a + 1 for a, b in merged)
print(coverage)
