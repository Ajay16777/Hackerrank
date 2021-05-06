N = int(input())
fac = []
for i in range(1,N+1):
    if N%i == 0:
    	fac.append(i)

print(len(fac))

print(*fac,sep=' ')
