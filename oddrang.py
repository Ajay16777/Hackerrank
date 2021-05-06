L,R = map(int, input().split())
odd = []
for i in range(L,R+1):
	if i % 2 != 0:
		odd.append(i)
		i+=1

print(*odd,sep=' ')