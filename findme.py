n,k = map(int,input().split())
a = list(map(int,input().split()))[:n]
if k in a:
	print(1)
else:
	print(-1)
