import networkx as nx
from functools import lru_cache

G = nx.DiGraph()

with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]


for line in inp:
    parts = line.split()
    start = parts[0].replace(":", "")
    ends = parts[1:]

    for end in ends:
        G.add_edge(start, end)


part1 = sum(1 for _ in nx.all_simple_paths(G, source="you", target="out"))

#part2
@lru_cache()
def count(a, b):
    if a == b:
        return 1
    total = 0
    for nxt in G[a]:
        total += count(nxt, b)
    return total


svr_dac = count("svr", "dac")
dac_fft = count("dac", "fft")
fft_out = count("fft", "out")

svr_fft = count("svr", "fft")
fft_dac = count("fft", "dac")
dac_out = count("dac", "out")


part2 = svr_dac * dac_fft * fft_out + svr_fft * fft_dac * dac_out

print(part1)
print(part2)
