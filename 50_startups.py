#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


data = pd.read_csv('50_Startups.csv')


# In[10]:


data.head()


# ## Bu veri seti, 50 farklı startup şirketinin çeşitli harcamalarını ve kârlılıklarını içermektedir.  
# 
# R&D Spend (Ar-Ge Harcaması): Şirketin araştırma ve geliştirme (Ar-Ge) için harcadığı tutar.  
# Administration (Yönetim Harcaması): Şirketin yönetim giderleri için harcadığı tutar.  
# Marketing Spend (Pazarlama Harcaması): Şirketin pazarlama ve reklam faaliyetleri için harcadığı tutar. 
# State (Eyalet): Şirketin faaliyet gösterdiği eyalet (örneğin, New York, California, Florida).  
# Profit (Kâr): Şirketin elde ettiği toplam kâr.  
# Bu veri seti, startup'ların çeşitli harcama kalemleri ile kârlılıkları arasındaki ilişkileri analiz   etmek için kullanılabilir. Örneğin, Ar-Ge veya pazarlama harcamalarının kârlılık üzerindeki etkisini   incelemek için uygun bir veri setidir.  

# ## 1.GÖREV : R&D Harcaması ve Kâr Arasındaki İlişki (Scatter Plot): Ar-Ge harcamaları ile kâr arasındaki ilişkiyi gösteren bir dağılım grafiği.

# In[11]:


# Kodu buraya yazınız 

x = df["R&D Spend"]
y = df["Profit"]

plt.scatter(x, y)
plt.xlabel("R&D Spend")
plt.ylabel("Profit")
plt.title("R&D Spend and Profit Comparison")
plt.show()






# ## 2.GÖREV: Yönetim Harcamaları ve Kâr Arasındaki İlişki (Scatter Plot): Yönetim harcamaları ile kâr arasındaki ilişkiyi gösteren bir dağılım grafiği.

# In[12]:


# Kodu buraya yazınız 

x = df["Administration"]
y = df["Profit"]

plt.scatter(x, y)
plt.xlabel("Administration")
plt.ylabel("Profit")
plt.show()






# ## 3. GÖREV: Eyaletlere Göre Ortalama Kâr (Bar Chart): Farklı eyaletlerdeki startup'ların ortalama kârlarını karşılaştıran bir çubuk grafik.

# In[13]:


# Kodu buraya yazınız 

mean_profit = df.groupby("State")["Profit"].mean()

mean_profit.plot(kind="bar")
plt.title("Profit Comparision by State")
plt.xlabel("State")
plt.ylabel("Profit")





# ## 4. GÖREV: Harcama Türlerinin Karşılaştırması (Boxplot): R&D, yönetim ve pazarlama harcamalarının dağılımını karşılaştıran bir kutu grafiği.

# In[14]:


# Kodu buraya yazınız 

columns = ["R&D Spend", "Administration", "Marketing Spend"]

plt.boxplot([df[c] for c in columns], tick_labels=columns)
plt.title("Spend Comparision")
plt.show()






# In[ ]:




