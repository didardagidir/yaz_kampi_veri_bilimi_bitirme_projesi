#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd


# In[5]:


data = pd.read_csv('dava.csv')
data


# ## Veri Seti inceleme
# Veri Seti Özellikleri:  
# Case Duration (Gün): Davanın tamamlanması için geçen süre (gün cinsinden).  
# Number of Witnesses (Tanık Sayısı): Dava boyunca dinlenen tanık sayısı.  
# Legal Fees (Hukuk Maliyetleri): Dava süresince oluşan toplam hukuk maliyetleri (USD cinsinden).  
# Number of Evidence Items (Delil Sayısı): Davada kullanılan delil sayısı.  
# Severity (Ciddiyet Düzeyi): Davanın ciddiyet düzeyi (1: Düşük, 2: Orta, 3: Yüksek).  
# Outcome (Sonuç): Davanın sonucu (0: Aleyhte, 1: Lehinde).  

# ## GÖREV: 
# Özellik Seçimi: Hangi özelliklerin kümeleme için kullanılacağına karar verin.  
# Küme Sayısını Belirleme: Elbow yöntemi gibi tekniklerle optimal küme sayısını belirleyin.  
# Kümeleme İşlemi: K-Means algoritmasını kullanarak verileri kümeleyin.  
# Sonuçları Görselleştirme: Kümeleme sonuçlarını uygun grafiklerle görselleştirin ve yorumlayın.  

# In[ ]:


# Kodu buraya yazınız.

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


df = df.drop(columns = ["Unnamed: 0"])
print(df.columns)
features = df.drop(columns=["Outcome"])

scaler = StandardScaler()
scaler_features = scaler.fit_transform(features)

import os
os.environ["OMP_NUM_THREADS"] = "1"

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

inertia = []
K = range(1,6)
for k in K:
    kmeans = KMeans(n_clusters = k, random_state = 42, n_init=10, max_iter=300,algorithm="lloyd")
    kmeans.fit(scaler_features)
    inertia.append(kmeans.inertia_)

plt.plot(K, inertia, 'bo-'),
plt.xlabel("Number of Clusters(k)")
plt.ylabel("Inertia (SSE)")
plt.title("Elbow Method for Optimal K")
plt.show()

import warnings
warnings.filterwarnings("ignore")


kmeans = KMeans(n_clusters = k, random_state = 42, n_init=10, max_iter=300,algorithm="lloyd")
clusters = kmeans.fit_predict(scaler_features)

df["Cluster"] = clusters

print(df.head())



from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

pca = PCA(n_components=2)
pca_features = pca.fit_transform(scaler_features)

plt.figure(figsize=(8,6))
plt.scatter(pca_features[:,0], pca_features[:,1], c=df["Cluster"], cmap="viridis", s=50)

plt.title("K-Means Clustering Visualization (PCA reduced)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.colorbar(label="Cluster")
plt.show()


import matplotlib.pyplot as plt

plt.scatter(scaler_features[:, 0], scaler_features[:, 1], c=df['Cluster'], cmap='viridis')
plt.xlabel("Case Duration (scaled)")
plt.ylabel("Number of Witnesses (scaled)")
plt.title("K-Means Clustering Result")
plt.show()




