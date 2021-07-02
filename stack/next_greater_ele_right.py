lst = [1,3,4,1,1,5,4,6,2,2,7,9,5,5]

stack = []
ans = []
stack.append(lst[0])
print(stack)
for i in range(1,len(lst)-1,1):
    print(lst[i])
    while len(stack) > 0:
        #print(2)
        top = stack[-1]
        print(top)
        if lst[i]>top:
            print("inside if")
            stack.pop()
            stack.append(lst[i])
            ans.append(lst[i])

print(ans)