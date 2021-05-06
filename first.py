T = int(input())
x,y,xr,yr,D = map(int,input().split())[:T]

eat = x/xr
water = y/yr
total = [eat,water]

if min(total)>=D:
	print(YES)
else:
	print(NO)