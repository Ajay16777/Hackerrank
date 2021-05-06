N = int(input())

d = dict(input().split()for _ in range(N))
print(d)
while True:
    try:
        name = input()
        if name in d:
            print("{}={}".format(name,d[name]))
        else:
            print('Not found')
    except:
        break
