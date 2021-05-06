T = int(input())
for _ in range(T):
	N,C = map(int,input().split())
	An = list(map(int, input().split()))[:N]
	h = sum(An)
	if h>C:
		print("NO")
	else:
		print("YES")


