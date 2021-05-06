# Complete the reverseArray function below.
def reverseArray(a):
    start = 0
    end = len(a)-1
    while start<end:
        arr[start], arr[end] = arr[end],arr[start]
        start +=1
        end -=1
    return a
        


N = int(input())
arr = list(map(int, input().rstrip().split()))[:N]

res = reverseArray(arr)

print(*res,sep=' ')

    
