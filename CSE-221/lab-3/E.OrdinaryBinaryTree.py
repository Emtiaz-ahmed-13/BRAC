def buildBST(arr,left,right,result):
    if left>right:
        return 
    
    mid=(left+right)//2
    result.append(arr[mid])

    buildBST(arr,left,mid-1,result)
    buildBST(arr,mid+1,right,result)
n=int(input())
arr=list(map(int,input().split()))

result=[]
buildBST(arr,0,n-1,result)
for val in result:
    print(val,end=" ")
print()