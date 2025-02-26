import json
import networkx as nx
from networkx.algorithms import isomorphism


# ##################################################
# 1) Load workpiece graph and feature graph data from  json file
# ##################################################

# Note: Available files are: workpiece_graph.json, feature_graph.json
workpiece_file_path = "workpiece_graph.json"
feature_file_path = "feature_graph.json"

with open(workpiece_file_path, 'r') as f:
        workpiece_json = json.load(f)

with open(feature_file_path, 'r') as f:
        feature_json = json.load(f)

# ##################################################
# 2) Create graphs from loaded data
# ##################################################

# Hint: The library networkx helps you to create a graph. You can use the nx.Graph() class to create a graph.
# Note: Other appraoches are also possible.

def create_graph(json_data):
    graph = nx.Graph()
    for node in json_data["nodes"]:
        graph.add_node(node[0], **node[1])
    for edge in json_data["edges"]:
        graph.add_edge(edge[0], edge[1], **edge[2])
    return graph

workpiece_graph = create_graph(workpiece_json)
feature_graph = create_graph(feature_json)



# Note: Optional task - Visualize the graph
# Example code:
# from pyvis.network import Network
# nt = Network()
# nt.from_nx(workpiece_graph)
# nt.show("graph.html", notebook=False)

# ##################################################
# 3) Check if the feature graph is a subgraph of the workpiece workpiece and find any other matching subgraphs
# ##################################################


# TODO

# ##################################################
# 4) Results
# ##################################################

# Print results if matches are found. Return the number of matches and the node ids.

# TODO
