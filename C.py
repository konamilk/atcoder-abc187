N = int(input())

S = [input() for i in range(N)]

S = set(S)

# print(S)

Ans = ''

for s in S:
    flg1, flg2 = False, False
    if s in S:
        flg1 = True

    if '!' + s in S:
        flg2 = True

    if flg1 and flg2:
        Ans = s
        break

if Ans == '':
    Ans = 'satisfiable'

print(Ans)