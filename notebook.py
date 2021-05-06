T = int(input())
for _ in range(T):
	x,y,k,n=(input().split())
	X=int(x)
	Y=int(y)
	K=int(k)
	N=int(n)
	diff = X-Y
	v = 0

	for _ in range(N):
		P,C = map(int,input().split())
		if C <= K and P >= diff:
			v +=1

	if diff == 0:
		v += 1                                                             
	if v != 1:
		print("UnluckyChef")
	else:
		print("LuckyChef")
