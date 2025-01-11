import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the CSV data
df = pd.read_csv(r'C:\Users\HARI\Desktop\Saru\Opinion\backend\clustered_combined_data.csv')


# Reduce data size for visualization
df = df.sample(n=500)  # Sample 500 rows for better performance

# Initialize graph
G = nx.Graph()

# Add nodes for each unique entity in the Cluster column
for cluster in df['Cluster'].unique():
    cluster_nodes = df[df['Cluster'] == cluster]
    for node in cluster_nodes.index:
        G.add_node(node, group=cluster)

# Create edges based on shared themes or sentiment
for i, row1 in df.iterrows():
    neighbors = df[(df['Assigned_Theme'] == row1['Assigned_Theme']) | (df['VADER_sentiment'] == row1['VADER_sentiment'])]
    for j, row2 in neighbors.iterrows():
        if i != j:
            G.add_edge(i, j, weight=0.5)

# Position nodes using spring layout
pos = nx.spring_layout(G, seed=42)

# Plot the graph with Matplotlib
plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(G, pos, node_size=50, node_color='skyblue')
nx.draw_networkx_edges(G, pos, alpha=0.3, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10)

# Save the plot as an image
plt.title("Opinion Clusters (Using GNN Visualization)")
plt.savefig("cluster.png")
plt.close()

print("Matplotlib visualization saved as opinion_clusters_matplotlib.png")
