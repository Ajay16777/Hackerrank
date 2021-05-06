N = int(input())
arr = list(map(int,input().split()))[:N]
Q = int(input())
x = list(map(int, input().split()))[:Q]
for i in x:
	arr1 = (arr[i:] + arr[:i])
	res_list = [arr[j] + arr1[j] for j in range(len(arr))]
	arr = res_list
	print(sum(arr))






