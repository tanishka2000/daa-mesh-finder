import networkx as nx
import matplotlib.pyplot as plt
import json

class graphClique:

    def __init__(self, graph, num_of_nodes):
        self.graph = graph
        self.num_of_nodes = num_of_nodes
        self.node_colors = [-1] * len(graph)
        self.max_freq_color = [-1,-1]
        self.mesh_graph = dict()
        self.graph_to_visualise = []

    def getCompliment(self):
        compliment_graph = dict()

        for vertex in self.graph:
            cur_complimented_list = []
            for node in range(self.num_of_nodes):
                if node not in self.graph[vertex] and node!=vertex:
                    cur_complimented_list.append(node)
            compliment_graph[vertex] = cur_complimented_list

        return compliment_graph

    def isValidColoring(self, graph, cur_vertex):
        for neighbour in graph[cur_vertex]:
            if (self.node_colors[neighbour] == self.node_colors[cur_vertex]):
                return False
        return True

    def colorGraph(self, cur_vertex, graph):
        print("Graph colors: ", self.node_colors)
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
        frequency = [0]*len(self.graph)
        for item in self.node_colors:
            if (frequency[item]>0): 
                frequency[item] += 1
            else: #true 
                frequency[item] = 1 
        #print(frequency)
        
        #storing the max frequency and corresponding number in a list
        max_freq = max(frequency)
        max_repeating_color = frequency.index(max_freq) 
        self.max_freq_color = [max_freq, max_repeating_color]

    def checkColor(self):
        node_colors_list = []
        for color in range(self.num_of_nodes):
            node_colors_list.append(color)
        
        if sorted(node_colors_list) == sorted(self.node_colors):
            return True 
        return False

    def getSizeOfMaximumIndependentSet(self, graph):
        first_vertex = list(graph.keys())[0]

        self.node_colors[first_vertex] = 0
        if (self.colorGraph(first_vertex, graph)):
            if(self.checkColor()):
                return False
            self.maxRepeatingColor()
            return True

        return False

    def getSizeOfMaxClique(self):
        compliment_graph = self.getCompliment()
        print(compliment_graph)
        if (self.getSizeOfMaximumIndependentSet(compliment_graph)):
          #max_color_freq updated
          return True
        else:
          return False

    def maxMeshGraph(self):
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

    def addEdge(self, node1, node2):
      temp_edge = [node1, node2]
      self.graph_to_visualise.append(temp_edge)
          
    def visualize(self, 
                  final_mesh):
      cur_graph = nx.Graph()
      cur_graph.add_edges_from(self.graph_to_visualise)
      node_map = []
      for node in cur_graph:
        if node in final_mesh:
          node_map.append('green')
        else: 
          node_map.append('purple') 
      nx.draw_networkx(cur_graph, node_color=node_map, edge_color="black", font_size = 16, font_color="white", node_size=800, width=2.0)
      plt.figure(figsize=(3, 3))
      plt.show()

    def displayMesh(self, graph_to_visualise, final_mesh):
      for parent_node in graph_to_visualise:
        for adj_node in graph_to_visualise[parent_node]:
          self.addEdge(parent_node, adj_node)
      self.visualize(final_mesh)

'''
class visualizeAllCliques:
    def __init__(self,graph,node_colors):
        self.graph = graph
        self.node_colors = node_colors
        self.graph_to_visualise = []

    def addEdge(self, node1, node2):
      temp_edge = [node1, node2]
      self.graph_to_visualise.append(temp_edge)
          
    def visualize(self):
      cur_graph = nx.Graph()
      cur_graph.add_edges_from(self.graph_to_visualise)
      node_map = self.node_colors
      nx.draw_networkx(cur_graph, node_color=node_map, edge_color="black", font_size = 16, font_color="white", node_size=800, width=2.0)
      plt.figure(figsize=(3, 3))
      plt.show()

    def displayMesh(self):
        for parent_node in self.graph:
            for adj_node in self.graph[parent_node]:
                self.addEdge(parent_node, adj_node)
        print(self.graph)
        self.visualize()
'''

#main program
input_graph = dict()
# Opening JSON file
with open('input3.json') as json_file:
    data = json.load(json_file)
    for i in data:
        j = int(i)
        input_graph[j] = data[i]

num_of_nodes= len(input_graph)

graph_clique_obj = graphClique(input_graph,num_of_nodes)

stor = graph_clique_obj.maxMeshGraph()
if(stor):
    print()
    print("Mesh Found")
    print()
    print("Original graph: ",input_graph)
    print("\nPrinting Mesh")
    print()
    final_mesh = graph_clique_obj.mesh_graph
    print("Your Mesh: ", final_mesh)
    print()
    graph_clique_obj.displayMesh(input_graph, final_mesh)
else:
    print()
    print("No mesh network found")
    print()

"""
print("Visualising all the cliques")

visualize_all_cliques_obj = visualizeAllCliques(input_graph, graph_clique_obj.node_colors)
visualize_all_cliques_obj.displayMesh()"""

