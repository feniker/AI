s = input()
sMin = s
sMax = s
while s!='стоп':
    if len(sMax)<len(s):
        sMax = s
    if len(sMin)>len(s):
        sMin = s
    s = input()
if set(sMin).issubset(set(sMax)):
    print('ДА')
else:
    print('НЕТ')