import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv('laptops_train.csv')

data['Screen Size'] = data['Screen Size'].str.replace('"', '').astype(float)
data['CPU'] = data['CPU'].str.extract(r'(\d+\.?\d*)').astype(float)
data['RAM'] = data['RAM'].str.extract(r'(\d+)').astype(int)

laptop_names = data['Model Name']

# Select relevant features for clustering
features = ['Screen Size', 'CPU', 'RAM']
X = data[features]

# Perform data preprocessing - standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the elbow method
inertia = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
import matplotlib.pyplot as plt
plt.plot(k_range, inertia)
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Within-Cluster Sum of Squares (Inertia)')
plt.title('Elbow Curve')

plt.show()

# Choose the optimal k value based on the elbow curve
k = 4

# Perform clustering with the selected k value
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X_scaled)

# Add the cluster labels to the dataset
data['Cluster'] = kmeans.labels_
data['Model Name'] = laptop_names

# Print the number of laptops in each cluster
print(data['Cluster'].value_counts())

# Explore the clusters
for cluster in range(k):
    print(f'\nCluster {cluster}:')
    cluster_data = data[data['Cluster'] == cluster]
    cluster_laptop_names = cluster_data['Model Name'].values
    print(cluster_data[features + ['Model Name']].head(10))
