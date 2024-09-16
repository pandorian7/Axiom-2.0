import re


def shifter_ch(shift: int, ch: str):
    if not ch.isalpha():
        return ch
    islower = ch.islower()
    offset = ord(ch.upper())-65
    offset += shift
    offset = offset % 26
    offset += 65
    ret = chr(offset)
    if islower:
        ret = ret.lower()

    return ret


in1 = input()

res = re.match(r"^(\d+)(?:\s*)([a-zA-Z ]*)", in1)

shift, msg = res.groups()
shift = int(shift)
msg = msg[::-1]

for ch in msg:
    print(shifter_ch(shift, ch), end="")
