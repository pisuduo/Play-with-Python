def bfs(n, m, edges, s):
    ## n: number of nodes
    ## m: number of edges
    ## edges: 2-d array of start and end nodes for edges: mx2
    ## s: starting node

    ## create a graph
    graph=dict()
    for i in range(m):
        graph[i]=edges
    

    queue=[]
    queue.append(s)
    visit=set()
    visit.add(s)
    E=dict()
    E[s] +=1
    D=dict()

    while len(queue)>0:
        vertex=queue.pop(0)
        nodes=graph[vertex]
        for nod in nodes:
            if E[nod]==0:
                E[nod]+=1
                D[nod]=D[]

            

    


edges=[[1,2],[3,4],[1,3]]
e=[int(x) for x in edges]

n=4
