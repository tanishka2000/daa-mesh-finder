from modules import graphClique
from modules import graphVisualization

def testGraphClique()->None:
    """
    A function to test graph clique component
    """
    import json
    input_graph = dict()
    # Opening JSON file
    with open('input2.json') as json_file:
        data = json.load(json_file)
        for i in data:
          j = int(i)
          input_graph[j] = data[i]

    num_of_nodes= len(input_graph)

    graph_clique_obj=graphClique.graphClique(input_graph,num_of_nodes)
    stor = graph_clique_obj.maxMeshGraph()
    if(stor):
      print("Mesh Found")
      print("Printing Mesh")
      final_mesh = graph_clique_obj.mesh_graph
      print(final_mesh)
      graph_visualisation_obj=graphVisualization()
      graph_visualisation_obj.displayMesh(input_graph, final_mesh)
    else:
      print("No mesh network found")

if __name__ == "__main__":
    testGraphClique()