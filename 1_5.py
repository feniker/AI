from itertools import chain
s = input()
sMod = list(chain(*[[ch,ch] for ch in s]))
print(''.join(sMod))