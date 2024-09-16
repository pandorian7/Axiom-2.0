import re
from collections import namedtuple

component = namedtuple("comp", 'sym,config')

patt = re.compile(r'^\("([YK])","(.*)"\)$')


def parse(string):
    return component(*patt.match(string).groups())


def tog_sym(string):
    if string == "K":
        return "Y"
    elif string == "Y":
        return "K"
    else:
        assert False


def tostr(comp):
    return f'("{comp.sym}","{comp.config}")'


n = int(input())
m = int(input())


def symMap(comp): return comp.sym


comps_in = []

for i in range(n):
    tmp_comps = list(map(parse, input().split()))
    comps_in.append(tmp_comps)

for i, row in enumerate(comps_in):
    out = []
    for j in range(m):
        sym = comps_in[0][j].sym
        if (i % 2 != 0):
            sym = tog_sym(sym)
        com_index = list(map(symMap, row)).index(sym)
        out.append(tostr(row[com_index]))
    print(" ".join(out))
