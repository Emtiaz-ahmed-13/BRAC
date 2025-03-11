def postOrder(inOrder,preOrder):
    if not inOrder:
        return []
    
    root =preOrder.pop(0)

    rootIndex=inOrder.index(root)
    left=inOrder[:rootIndex]
    right=inOrder[rootIndex+1:]

    leftPostOrder=postOrder(left,preOrder)
    rightPostOrder=postOrder(right,preOrder)

    return leftPostOrder+rightPostOrder+[root]

n=int(input())
inOrder=list(map(int,input().split()))
preOrder=list(map(int,input().split()))
result=postOrder(inOrder,preOrder)
for val in result:
    print(val,end=" ")
print()