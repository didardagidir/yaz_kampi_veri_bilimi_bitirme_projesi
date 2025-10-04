#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = pd.read_csv('dava_sonuclari.csv')
data.head()


# ## VERİ SETİ İNCELEME : 
# Case Type: Davanın türü (Criminal, Civil, Commercial)  
# Case Duration (Days): Davanın süresi (gün olarak)  
# Judge Experience (Years): Hakimin deneyim yılı  
# Number of Witnesses: Tanık sayısı  
# Legal Fees (USD): Hukuk masrafları (USD olarak)  
# Plaintiff's Reputation: Davacının itibarı (1: Düşük, 2: Orta, 3: Yüksek)  
# Defendant's Wealth (USD): Davalının serveti  
# Number of Evidence Items: Delil sayısı  
# Number of Legal Precedents: İlgili hukuki emsal sayısı  
# Settlement Offered (USD): Teklif edilen uzlaşma miktarı  
# Severity: Davanın ciddiyet derecesi (1: Düşük, 2: Orta, 3: Yüksek)  
# Outcome: Davanın sonucu (0: Kaybetmek, 1: Kazanmak)  

# ## Görevler
# 
# ### Veri Ön İşleme:
# * Veri setini inceleyin ve eksik veya aykırı değerler olup olmadığını kontrol edin.  
# * Gerektiğinde eksik verileri doldurun veya çıkarın.  
# * Özelliklerin ölçeklendirilmesi gibi gerekli veri dönüşümlerini uygulayın. 
# 
# ### Veri Setini Ayırma:
# * Veri setini eğitim ve test setleri olarak ayırın (örn. %80 eğitim, %20 test).  
# 
# ### Model Kurulumu:
# * Karar ağacı modelini oluşturun ve eğitim verileri üzerinde eğitin.
# 
# ### Modeli Değerlendirme:
# * Test verilerini kullanarak modelin doğruluğunu değerlendirin.
# * Doğruluk, precision, recall ve F1-score gibi performans metriklerini hesaplayın.
# 
# ### Sonuçları Görselleştirme:
# * Karar ağacının yapısını görselleştirin.
# * Karar ağacının nasıl çalıştığını ve hangi özelliklerin davanın sonucunu belirlemede en etkili olduğunu açıklayın.

# In[ ]:

numeric_columns = df.select_dtypes(include = ["int64", "float64"]).columns

df[numeric_columns].plot(kind="box", figsize=(12,6))
plt.title("Outlier for Numerical Variables")
plt.xticks(rotation=45)
plt.show()

print(df["Defendant's Wealth (USD)"].max())
print(df["Defendant's Wealth (USD)"].min())

print(df["Defendant's Wealth (USD)"].describe())

print(df["Defendant's Wealth (USD)"].sort_values(ascending=False).head(10))

lower_limit = df["Defendant's Wealth (USD)"].quantile(0.01)
upper_limit = df["Defendant's Wealth (USD)"].quantile(0.99)

print("Lower limit: ", lower_limit)
print("Upper limit: ", upper_limit)

print("Sum of columns that less than lower limit: ", df[df["Defendant's Wealth (USD)"] < lower_limit].shape[0])
print("Sum of columns that greater than upper limit: ", df[df["Defendant's Wealth (USD)"] > upper_limit].shape[0])

df = df[(df["Defendant's Wealth (USD)"] >= lower_limit) & (df["Defendant's Wealth (USD)"] <= upper_limit)]

print("New maximum value: ", df["Defendant's Wealth (USD)"].max())
print("New minimum value: ", df["Defendant's Wealth (USD)"].min())
print("Remaining row count: ", df.shape[0])


from sklearn.model_selection import train_test_split
x = df.drop(columns = ["Outcome"])
y = df["Outcome"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

print("Training set size: ", x_train.shape[0])
print("Test set size: ", x_test.shape[0])

print(df.dtypes)

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

df["Case Type"] = encoder.fit_transform(df["Case Type"])
df["Severity"] = encoder.fit_transform(df["Severity"])
df["Outcome"] = encoder.fit_transform(df["Outcome"])

x = df.drop(columns = ["Outcome"])
y = df["Outcome"]

model = DecisionTreeClassifier(random_state = 42)
model.fit(x_train, y_train)


clf = DecisionTreeClassifier(random_state = 42)

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

print("First 10 predictions: ", y_pred[:10])


from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

conf_matrix = confusion_matrix(y_test,y_pred, labels=[0,1])
print("Confusion Matrix:\n", conf_matrix)

print("Classification Report:\n", classification_report(y_test, y_pred))

print(y.value_counts())
print(y_train.value_counts())
print(y_test.value_counts())

from sklearn.tree import plot_tree
plt.figure(figsize=(20,10))
plot_tree(model, feature_names=x.columns, class_names=[0], filled=True)
plt.show()

feature_importances = pd.DataFrame({
    'Feature': x.columns,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)

print(feature_importances)



