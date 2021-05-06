# hourglass sum code
def hourglassSum(arr):
	m = []
	for i in range(N - 2):
		for j in range(N - 2):
			temp = 0
			temp += arr[i][j] + arr[i][j+1] + arr[i][j+2]
			temp += arr[i+1][j+1]
			temp += arr[i+2][j] + arr[i+2][j+1]+ arr[i+2][j+2]
			m.append(temp)
	print(max(m))

# Main function
N = int(input())
arr = []
for _ in range(N):
	arr.append(list(map(int,input().split())))


hourglassSum(arr)


