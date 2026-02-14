# model.py

import pandas as pd
import pickle
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load Dataset
data = pd.read_csv("wine_clustering_data.csv")

# Select all numerical columns (13 features)
X = data.select_dtypes(include=['float64', 'int64'])

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans Model
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Save Scaler
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

# Save Model
with open("kmeans_model.pkl", "wb") as f:
    pickle.dump(kmeans, f)

print("✅ Model and Pickle files created successfully!")