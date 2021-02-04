# undirected graph
class Graph:
	def __init__(self,Nodes, is_directed=False):
		self.nodes = Nodes
		self.adj_list = {}
		self.is_directed = is_directed
		for node in self.nodes:
			self.adj_list[node] = []

	def add_edge(self,u,v):
		self.adj_list[u].append(v)
		if not self.is_directed:
			self.adj_list[v].append(u)

	def print_adj_list(self):
		for node in self.nodes:
			print(node, "->", self.adj_list[node])

	def degree(self,node):
		# num of edges connected to that node
		return len(self.adj_list[node])



if __name__ == '__main__':
	nodes = ["A","B","C","D","E"]
	graph = Graph(nodes,is_directed=True)
	all_edges = [("A","B")
				 ,("A","C")
				 ,("B","D")
				 ,("C","D")
				 ,("C","E")
				 ,("D","E")]
	for u,v in all_edges:
		graph.add_edge(u,v)
	graph.print_adj_list()
	print("degree: ", graph.degree("C"))