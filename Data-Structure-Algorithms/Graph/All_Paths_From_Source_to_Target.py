def allPathsSourceTarget(graph):
    dest = max(graph)[0]
    path = []
    for i in range(len(graph)):
        dfs(i,dest,graph,path)    
        
        
def dfs(src,dest,graph,path):
    visited = []
    stack = []
    stack.append(src)
    visited.append(src)
    path.append(src)
    #print(visited,stack)
    #print("initial done")
    while stack:
        el=stack.pop(0)
        #print("el",el,src)
        for item in graph[el]:
            #print(item)
            if item not in visited:
                if item == dest:
                    path.append(item)
                    #print(path)
                else:
                    stack.append(item)
                    print(stack)
                    path.append(item)
                    visited.append(item)


                
            

g=[[1,2],[3],[3],[]]
allPathsSourceTarget(g)