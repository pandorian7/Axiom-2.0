from itertools import permutations


def evaluate(vals: list[int]):
    if len(vals) >= 2:
        vals[-2] = vals[-2]-vals[-1]
        return evaluate(vals[:-1])
    else:
        return vals[0]


f_in = int(input())
f_out = int(input())

n_exilions = int(input())

coeffes = {}
exilions = []


def get_coeff(name): return coeffes[name]


for i in range(n_exilions):
    freq_name, coeff = input().split()
    coeff = int(coeff)
    coeffes[freq_name] = coeff
    exilions.append(freq_name)

for order in permutations(exilions):
    if evaluate([f_in, *map(get_coeff, order)]) == f_out:
        print(" ".join(order))
