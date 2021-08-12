def solve(graph,src,dest,visited,psf):
    if src == dest:
        print("path",psf)
        psf = ''
        return 
     
    visited.append(src)
   
    for nbr in graph[src]:
        if nbr not in visited:
            solve(graph,nbr,dest,visited,psf+str(nbr))
    print(src)
    visited.remove(src)

graph=[[1,2],[3],[3],[]]
visited = []
psf = ''
solve(graph,0,3,visited,psf+str(0))
