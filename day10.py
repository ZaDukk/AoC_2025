import re
from itertools import combinations
from z3 import Optimize, Int, sat


#cool problem! I just brute forced part 1 and used z3 for part 2

def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers

with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]

part1 = 0
part2 = 0

for line in inp:
    # [.#...]
    m = re.search(r"\[([.#]+)\]", line)
    diag = m.group(1)

    # (a,b,c)
    buttontext = re.findall(r"\((.*?)\)", line)
    buttons = []
    for group in buttontext:
        buttons.append(extract_integers(group))

    # {t0,t1,...}
    t = re.search(r"\{(.*?)\}", line)
    targets = extract_integers(t.group(1))


    #part 1
    n = len(diag)
    target = [1 if c == "#" else 0 for c in diag]

    m_buttons = len(buttons)
    best = float("inf")


    for r in range(1, m_buttons + 1):

        for combo in combinations(range(m_buttons), r):
            state = [0] * n


            for i in combo:
                for light in buttons[i]:
                    state[light] ^= 1

            if state == target:
                best = min(best, r)

    if best != float("inf"):
        part1 += best

    #part 2
    k = len(targets)
    m_buttons = len(buttons)

    miniPekka = Optimize()

    xs = [Int(f"x_{i}") for i in range(m_buttons)]

    # all  presses >= 0
    for x in xs:
        miniPekka.add(x >= 0)

    # each counters target
    for counter in range(k):
        miniPekka.add(sum(xs[i] for i, btn in enumerate(buttons) if counter in btn) == targets[counter])

    # minimize presses
    miniPekka.minimize(sum(xs))

    if miniPekka.check() == sat:
        model = miniPekka.model()
        presses = sum(model.eval(x).as_long() for x in xs)
        part2 += presses

print(part1)
print(part2)
