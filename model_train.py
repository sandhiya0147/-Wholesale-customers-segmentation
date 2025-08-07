import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
import joblib

# Load dataset
df = pd.read_csv("Wholesale customers data.csv")

# Scale data
scaler = StandardScaler()
scaled = scaler.fit_transform(df)

# PCA transformation
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled)

# DBSCAN clustering
dbscan = DBSCAN(eps=0.8, min_samples=5)
labels = dbscan.fit_predict(pca_data)

# Save clustered data
clustered_df = pd.DataFrame(pca_data, columns=["PC1", "PC2"])
clustered_df["Cluster"] = labels
clustered_df.to_csv("clustered_data.csv", index=False)

# Save models
joblib.dump(scaler, "scaler.pkl")
joblib.dump(pca, "pca_model.pkl")
joblib.dump(dbscan, "dbscan_model.pkl")
