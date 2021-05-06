T = int(input())
X = 0
Y = 0
for _ in range(T):
	N ,A, B = map(int, input().split())
	for _ in range(N):
		S = str(input()).upper()
		if S[0] in "EQUINOX":
			X += A
		else:
			Y += B
	if X > Y:
		print("SARTHAK")
	elif X < Y:
		print("ANURADHA")
	elif X == Y:
		print("DRAW")




