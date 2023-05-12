import networkx as nx

# Step 1: Data Collection
# Assuming you have collected the necessary data and stored it in a suitable format

# Step 2: Building the Graph
# Create an empty graph
graph = nx.Graph()

# Add nodes to the graph
# Assuming you have a list of web pages stored in the variable 'web_pages'
graph.add_nodes_from(routes.txt)

# Add edges to the graph based on the links between web pages
# Assuming you have a list of tuples representing links between web pages stored in the variable 'links'
graph.add_edges_from(links)

# Step 3: Node Importance
# Calculate the degree centrality of each node
degree_centrality = nx.degree_centrality(graph)

# Calculate the betweenness centrality of each node
betweenness_centrality = nx.betweenness_centrality(graph)

# Calculate the PageRank of each node
pagerank = nx.pagerank(graph)

# Step 4: Analyzing Node Importance
# Sort the nodes based on their centrality metrics
sorted_nodes_by_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)
sorted_nodes_by_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)
sorted_nodes_by_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)

# Print the top three important nodes based on each centrality metric
print("Top three important nodes based on degree centrality:")
for node, centrality in sorted_nodes_by_degree[:3]:
    print(node, centrality)

print("Top three important nodes based on betweenness centrality:")
for node, centrality in sorted_nodes_by_betweenness[:3]:
    print(node, centrality)

print("Top three important nodes based on PageRank:")
for node, centrality in sorted_nodes_by_pagerank[:3]:
    print(node, centrality)