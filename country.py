#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


data = pd.read_csv('country.csv')
data


# ##  Country.csv dosyasının özelliği
# Bu tablo, çeşitli ülkelerle ilgili bir dizi demografik, ekonomik ve coğrafi veriyi içermektedir. Tabloda her bir satır bir ülkeyi temsil ederken, sütunlar bu ülkelerle ilgili farklı özellikleri gösterir. İşte sütunların anlamları:
# 
# Country: Ülkenin adı.  
# Region: Ülkenin bulunduğu bölge (örneğin, Asya, Doğu Avrupa).  
# Population: Ülkenin toplam nüfusu.  
# Area (sq. mi.): Ülkenin yüzölçümü (mil kare olarak).  
# Pop. Density (per sq. mi.): Nüfus yoğunluğu (mil kare başına düşen kişi sayısı).  
# Coastline (coast/area ratio): Sahil uzunluğunun, ülkenin toplam alanına oranı.  
# Net migration: Net göç oranı (göçmenlerin ülkeye giren veya ülkeden çıkan kişi sayısına göre oranı).  
# Infant mortality (per 1000 births): Bebek ölüm oranı (1000 doğum başına).  
# GDP ($ per capita): Kişi başına düşen Gayri Safi Yurtiçi Hasıla (GSYİH).  
# Literacy (%): Okur-yazarlık oranı.  
# Phones (per 1000): Her 1000 kişi başına düşen telefon sayısı.  
# Arable (%): Tarıma elverişli arazi yüzdesi.  
# Crops (%): Ekilebilir ürünlerin yüzdesi.  
# Other (%): Diğer arazi kullanımı yüzdesi.  
# Climate: Ülkenin iklim kategorisi (numerik bir değer olarak gösterilmiş).  
# Birthrate: Doğum oranı.  
# Deathrate: Ölüm oranı.  
# Agriculture: Tarım sektörünün ekonomideki payı.  
# Industry: Sanayi sektörünün ekonomideki payı.  
# Service: Hizmet sektörünün ekonomideki payı.  
# 

# ## Bu Dosyada Yapacağınız görevleri alt taraftan bakabilirsiniz.

# ## 1. Görev : Nüfusa Göre Azalan Sırada Sıralama:

# In[4]:


# Nüfusa Göre Azalan Sırada Sıralama kodunu buraya yazınız

population_desc = df.sort_values(by="Population", ascending=False)
print(population_desc[["Country", "Population"]])






# ## 2. Görev: GDP per capita sütununa göre ülkeleri artan sırada sıralamak(Kişi başına düşen Gayri Safi Yurtiçi Hasıla).

# In[5]:


# GDP per capita sütununa göre ülkeleri artan sırada sıralamak(Kişi başına düşen Gayri Safi Yurtiçi Hasıla). kodunu buradan yazınız.

gdp_asc = df.sort_values(by="GDP ($ per capita)", ascending=True)
print(gdp_asc[["Country", "GDP ($ per capita)"]])







# ## 3. Görev: Population sütunu 10 milyonun üzerinde olan ülkeleri seçmek.

# In[6]:


# Kodunu buraya yazınız.

population_over_10m = df[df["Population"] > 10000000]
print(population_over_10m[["Country", "Population"]])






# ## 4. Görev: Literacy (%) sütununa göre ülkeleri sıralayıp, en yüksek okur-yazarlık oranına sahip ilk 5 ülkeyi seçmek.

# In[7]:


# Kodunu buraya yazınız.

top5_literacy = df.sort_values(by="Literacy (%)", ascending=False).head(5)
print(top5_literacy[["Country", "Literacy (%)"]])






# ## 5. Görev:  Kişi Başı GSYİH 10.000'in Üzerinde Olan Ülkeleri Filtreleme: GDP ( per capita) sütunu 10.000'in üzerinde olan ülkeleri seçmek.

# In[8]:


# Kodunu buraya yazınız.

gdp_over_10000 = df[df["GDP ($ per capita)"] > 10000]
print(gdp_over_10000[["Country", "GDP ($ per capita)"]])







# ## Görev 6 : En Yüksek Nüfus Yoğunluğuna Sahip İlk 10 Ülkeyi Seçme:
# Pop. Density (per sq. mi.) sütununa göre ülkeleri sıralayıp, en yüksek nüfus yoğunluğuna sahip ilk 10 ülkeyi seçmek.

# In[ ]:

top10_density = df.sort_values(by="Pop. Density (per sq. mi.)", ascending=False).head(10)
print(top10_density[["Country", "Pop. Density (per sq. mi.)"]])


