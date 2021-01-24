N = int(input())
x = []
y = []

for i in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

count = 0

for i in range(N):
    for j in range(N):
        if j >= i:
            continue

        dx = x[i] - x[j]
        dy = y[i] - y[j]

        if (-dx <= dy and dy <= dx) or (-dx >= dy and dy >= dx):
            count = count+1

print(count)

