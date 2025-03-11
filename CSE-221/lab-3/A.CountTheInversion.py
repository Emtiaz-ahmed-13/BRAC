# n=int(input())
# arr=list(map(int,input().split()))

# inversions=0
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i]>arr[j]:
#             inversions+=1

# for i in  range(n):
#     for j in range(n-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]

# print(inversions)

# for num in arr:
#     print(num,end=' ')
# print()

def merge(arr,temp_arr,left,right,mid):
    i=left
    j=mid+1
    k=left
    inv_count=0

    while i<=mid and j<=right:
        if arr[i] <=arr[j]:
            temp_arr[k]=arr[i]
            i+=1
        else:
            temp_arr[k]=arr[j]
            inv_count+=(mid-i+1)
            j+=1
        k+=1
    while i<=mid:
        temp_arr[k]=arr[i]
        k+=1
        i+=1
    while j<=right:
        temp_arr[k]=arr[j]
        k+=1
        j+=1
    for i in range(left,right+1):
        arr[i]=temp_arr[i]
    return inv_count


def mergeCount(arr,temp_arr,left,right):
    int_count=0
    if left<right:
        mid=(left+right)//2
        int_count+=mergeCount(arr,temp_arr,left,mid)
        int_count+=mergeCount(arr,temp_arr,mid+1,right)
        int_count+=merge(arr,temp_arr,left,right,mid)
    return int_count

n=int(input())
arr=list(map(int,input().split()))

temp_arr=[0]*n 
int_count=mergeCount(arr,temp_arr,0,n-1)
print(int_count)

print(" ".join(map(str,arr)))