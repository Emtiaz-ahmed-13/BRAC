def MaxPairSum(A,left,right):
    if left == right:
        return A[left]
    
    mid = (left+right)//2

    maxLeft=MaxPairSum(A,left,mid)
    maxRight=MaxPairSum(A,mid+1,right)

    leftMax=max(A[left:mid+1])
    rightMax=max(A[mid+1:right+1])

    combine=(leftMax+rightMax) **2

    return max(maxLeft,maxRight,combine)


T = int(input()) 
A = list(map(int,input().split()))
result=MaxPairSum(A,0,len(A)-1)
print(result)

