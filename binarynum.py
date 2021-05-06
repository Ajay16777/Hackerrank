N = int(input())
b = bin(N)
c = 0
m = 0
for i in b:
	if i == '1':
		c = c+1
	else:
		m = max(m,c)
		c = 0

print(max(m,c))
