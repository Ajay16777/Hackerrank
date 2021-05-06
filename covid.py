T = int(input())
for _ in range(T):
	A,N,d = map(int, input().split())
	x,y,z = map(int, input().split())
	total_days = 0
	total_pacent = x+y+z
	if A <=18:
		if total_pacent == N:
			total_days += 20
		elif total_pacent < N:
			total_days += 10
		if total_days <= d:
			print("YES")
		else:
			print("NO")
	elif A>= 19 and A <=50:
		if total_pacent == N:
			total_days += 28
		elif total_pacent < N:
			total_days += 14
		if total_days <= d:
			print("YES")
		else:
			print("NO")
	elif A> 51:
		if total_pacent == N:
			total_days += 42
		elif total_pacent < N:
			total_days += 21
		if total_days <= d:
			print("YES")
		else:
			print("NO")

