
graph=[[1,2],[3],[3],[]]

def solve(graph,src,dest):
    stack = []
    visited = []
    stack.append(src)
    visited.append(src)
    while stack:
        top = stack.pop(0)
        for element in graph[top]:
            if element == dest:
                print("path is exites")
                return

            if element not in visited:
                stack.append(element)
    print("path not exites")



solve(graph,3,1)


