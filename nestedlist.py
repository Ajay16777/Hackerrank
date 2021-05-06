n = int(input())
mask = []
maeksheet = []
for _ in range(n):
    name = input()
    score = float(input())
    maeksheet += [[name, score]]
    mask += [score]

sh = sorted(list(set(mask)))[1]

for i,j in sorted(maeksheet):
    if j == sh:
        print(i)


