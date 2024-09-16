from functools import reduce


def numbers():
    return map(int, input().split())


def show(lst):
    return f"[{', '.join(map(str, lst))}]"


def rotate(lst, laps):
    laps = laps % len(lst)
    for i in range(laps):
        lst = [lst[-1]] + lst[:-1]
    return lst


def unique(lst):
    return reduce(lambda res, val: res if val in res else res+[val], lst, [])


def isSemetric(lst):
    return lst == lst[::-1]


n_rows, = numbers()
rotations, = numbers()

lst = []

for i in range(n_rows):
    comm, val = numbers()

    if comm:
        lst = [val, *lst]
    else:
        lst = [*lst, val]

# lst = [1, 2, 3, 2, 1]

print(f"Original linked list: {show(lst)}")
rotated = rotate(lst, rotations)
print(f"Rotated linked list: {show(rotated)}")
print(f"Linked list after removing duplicates: {show(unique(rotated))}")
print(f"The linked list is {'' if isSemetric(lst) else 'not '}symmetric.")
