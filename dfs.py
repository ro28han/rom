def main():
    graph={"A":['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':['F'],'F':[]}
    print(graph)
    visited=[]
    queue=[]
    def BFS(visited,graph,node):
        visited.append(node)
        print("Initial visited List =",visited)
        queue.append(node)
        print("Initial queue List =",queue)
       
        while queue:
            m=queue.pop(0)
            print("Poped Element ",m)
            for neighbour in graph[m]:
                if neighbour in visited:
                    return
                else:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    print("IN visited List =",visited)
                    print("IN queue List =",queue)


   
    BFS(visited,graph,"A")
main()
