import networkx as nx
import matplotlib.pyplot as plt

class graphVisualization:
    def __init__(self)->None:
      """
      constructor
      """
      self.graph_to_visualise = []
          
    def addEdge(self, node1, node2)->None:
      """
      node1 -> Source node where the edge begins from
      node2 -> Source node where the edge ends at
      :return: None
      """
      temp_edge = [node1, node2]
      self.graph_to_visualise.append(temp_edge)
          
    def visualize(self, 
                  final_mesh : dict) -> None:
      """
      final_mesh -> contains only the mesh nodes
      :return: None
      """
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

    def displayMesh(self, 
                    graph_to_visualise : dict,
                    final_mesh : dict)->None:
      """
      graph_to_visualise -> main graph
      final_mesh -> contains only the mesh nodes
      :return: None
      """
      for parent_node in graph_to_visualise:
        for adj_node in graph_to_visualise[parent_node]:
          self.addEdge(parent_node, adj_node)
      self.visualize(final_mesh)