def swap(a,b):
    temp = a
    a = b
    b = temp

def reversarr(arr,n):
    i = 0
    j = n-1
    while j>i:
        swap(arr[i],arr[j])
        i+=1
        j-=1
    return arr
n = int(input())
arr = list(map(int, input().strip().split()))[:n]
print(reversarr(arr,n))

input()

