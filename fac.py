import math
T = int(input())
for _ in range(T):
	N, X, Y = map(int, input().split())
	fn = math.factorial(N)
	fx = math.factorial(X)
	fy = math.factorial(Y)
	fnx = math.factorial(N-X)
	fny = math.factorial(N-Y)
	ncx = fn/(fnx*fx)
	ncy = fn/(fny*fy)
	print(ncx*ncy)
