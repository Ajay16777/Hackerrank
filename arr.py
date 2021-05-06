N = int(input())
arr = list(map(int, input().split()))[:N]
arr.reverse()
print(*arr,sep=' ')
