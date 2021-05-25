class graphClique:

    def __init__(self,
                 graph: dict,
                 num_of_nodes: int) -> None:
        """
        :params graph: Input graph
        :params num_of_nodes: total nodes in graph
        return : None
        """
        self.graph = graph
        self.num_of_nodes = num_of_nodes
        self.node_colors = [-1] * len(graph)
        self.max_freq_color = [-1,-1]
        self.mesh_graph = dict()

    def getCompliment(self) -> dict:
        """
        Compliments a graph
        :return: complimented graph
        """
        compliment_graph = dict()

        for vertex in self.graph:
            cur_complimented_list = []
            for node in range(self.num_of_nodes):
                if node not in self.graph[vertex] and node!=vertex:
                    cur_complimented_list.append(node)
            compliment_graph[vertex] = cur_complimented_list

        return compliment_graph

    def isValidColoring(self,
                        graph: dict,
                        cur_vertex: int) -> bool:
        """
        :params graph: Input graph
        :params cur_vertex: node to process

        :return: whether current vertex has right color or not
        """

        for neighbour in graph[cur_vertex]:
            if (self.node_colors[neighbour] == self.node_colors[cur_vertex]):
                return False
        return True

    def colorGraph(self,
                   cur_vertex: int,
                   graph: dict) -> bool:
        """
        :params graph: Input graph
        :params cur_vertex: int

        :return: whether graph is colored or not
        """
        for neighbour in graph[cur_vertex]:
            if (self.node_colors[neighbour] != -1):
                continue
            for color in range(self.num_of_nodes):
                self.node_colors[neighbour] = color
                if (self.isValidColoring(graph, neighbour)):
                    if (self.colorGraph(neighbour, graph)):
                        break
                    else:
                        self.node_colors[neighbour] = -1
                else:
                    self.node_colors[neighbour] = -1

            if (self.node_colors[neighbour] == -1):
                return False
        return True

    def maxRepeatingColor(self):
        """
        :return: frequency of maximum used color for graph coloring from node_colors
        """
        
        frequency = [0]*len(self.graph)
        for item in self.node_colors:
            if (frequency[item]>0): 
                frequency[item] += 1
            else: #true 
                frequency[item] = 1 
        #print(frequency)
        
        max_freq = max(frequency)
        max_repeating_color = frequency.index(max_freq) 
        self.max_freq_color = [max_freq, max_repeating_color]

    def getSizeOfMaximumIndependentSet(self, graph: dict) -> bool:
        """

         :params graph: Input graph
         :return: maximum size of independant set in graph
        """
        first_vertex = list(graph.keys())[0]

        self.node_colors[first_vertex] = 0
        if (self.colorGraph(first_vertex, graph)):
            self.maxRepeatingColor()
            return True

        return False

    def getSizeOfMaxClique(self) -> bool:
        """

        :return: maximum size of clique in graph
        """

        compliment_graph = self.getCompliment()
        if (self.getSizeOfMaximumIndependentSet(compliment_graph)):
          #max_color_freq updated
          return True
        else:
          return False

    def maxMeshGraph(self) -> bool:
      """
      :return: the final graph which is a Mesh network
      """
      if (self.getSizeOfMaxClique()):
        for node in self.graph:
          if self.node_colors[node] == self.max_freq_color[1]:
            temp_list = []
            for adj_nodes in self.graph[node]:
                if self.node_colors[adj_nodes] == self.max_freq_color[1]:
                    temp_list.append(adj_nodes)
            self.mesh_graph[node] = temp_list 
        
      else:
        return False

      return True
