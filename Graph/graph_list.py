class Graph:
    def __init__(self):
        self.graph={}
    def add_edge(self,u,v,directed=False):
        if u not in self.graph:
            self.graph[u]=[]
        self.graph[u].append(v)
        if not directed:
            if v not in self.graph:
                self.graph[v]=[]
        self.graph[v].append(u)
    def print(self):
        for node in self.graph:
            print(f"{node}->{self.graph[node]}")
    
graph=Graph()
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(2,5)
graph.add_edge(3,4)
graph.add_edge(4,6)
graph.print()

