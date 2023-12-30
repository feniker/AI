N = int(input())
arrS = []
for _ in range(N):
    s = input()
    arrS.append(s)
for i in range(len(arrS)):
    s = arrS[i]
    if ('к' in s) and ('о' in s) and ('т' in s):
        print("МЯУ")
        break
    if i == N-1:
        print("НЕТ")