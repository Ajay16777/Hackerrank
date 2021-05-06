n = int(input())
name =[]
score = []
for _ in range(n):
	a = list(map(str, input().split()))[:4]
	v = float(a[1])
	g = float(a[2])
	h = float(a[3])
	name.append(a[0])
	s = [v,g,h]
	score.append(s)

n = str(input())
if n == name[0]:
	u = sum(score[0])/3 
	print("{0:.2f}".format(u))	
elif n == name[1]:
	u = sum(score[1])/3
	print("{0:.2f}".format(u))
elif n == name[2]:
	u = sum(score[2])/3
	print("{0:.2f}".format(u))