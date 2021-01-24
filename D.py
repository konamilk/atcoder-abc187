import numpy as np
N = int(input())
A, B = [], []
X, Y = [], []
Z = []

for i in range(N):
    a, b = map(int, input().split())
    # A.append(a)
    # B.append(b)
    # X.append(a + b)
    # Y.append(-b)
    Z.append([a+b, -a])


Z = sorted(Z, key=lambda x: (x[0], x[1]), reverse=True)


Znp = np.array(Z)


for i in range(N-1):
    AOKI = Znp[:, 1][i+1:].sum()
    TAKAHASHI = Znp[:, 0][:i+1].sum()

    if AOKI + TAKAHASHI > 0:
        print(i + 1)
        break
