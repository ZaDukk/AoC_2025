import re

def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    return [int(x) for x in re.findall(pattern, input_string)]

with open("input.txt") as f:
    inp = f.read().strip()


nums = extract_integers(inp)
ranges = [range(nums[i], nums[i+1] + 1) for i in range(0, len(nums), 2)]

p = re.compile(r"^(\d+)\1+$")

part1 = 0
part2 = 0

for r in ranges:
    for id in r:
        s = str(id)
        mid = len(s) // 2

        if len(s) % 2 == 0 and s[:mid] == s[mid:]:
            part1 += id

        if p.match(s):
            part2 += id

print(f"P1: {part1}")
print(f"P2: {part2}")
