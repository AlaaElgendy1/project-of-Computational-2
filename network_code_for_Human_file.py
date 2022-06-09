#!/usr/bin/env python
# coding: utf-8

# In[38]:


import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("HomoSapiens_htb_hq.txt",sep="\t",usecols=["Uniprot_A","Uniprot_B"])


# In[39]:


G=nx.from_pandas_edgelist(df,"Uniprot_A","Uniprot_B",create_using=nx.DiGraph())


# In[40]:


degrees=dict(G.degree())
order=sorted(degrees.items(),key=lambda t:t[1])
x,y=zip(*order)
plt.plot(x,y)
plt.show()


# In[41]:


from collections import Counter
degree_sequence = [G.degree(n) for n in G.nodes]
degree_counts = Counter(degree_sequence)
min_degree, max_degree = min(degree_counts.keys()), max(degree_counts.keys())
plt.xlabel("Degree", fontsize=20)
plt.ylabel("Frequency", fontsize=20)
plot_x = list(range(min_degree, max_degree + 1))
plot_y = [degree_counts.get(x, 0) for x in plot_x]
plt.bar(plot_x, plot_y)


# In[42]:


import math
def plot_degree_dist(G):
    
    degrees = G.degree()
    degrees = dict(degrees)
    values = sorted(set(degrees.values()))
   
    histo = [list(degrees.values()).count(x) for x in values]
    P_k = [x / G.order() for x in histo]
   
    
    plt.figure()
    plt.bar(values, P_k)
    plt.xlabel("k",fontsize=20)
    plt.ylabel("p(k)", fontsize=20)
    plt.title("Degree Distribution", fontsize=20)
    
    plt.show()
    plt.figure()
    plt.grid(False)
    plt.loglog(values, P_k, "bo")
    plt.xlabel("k", fontsize=20)
    plt.ylabel("log p(k)", fontsize=20)
    plt.title("log Degree Distribution")
    plt.show()
    plt.show()  


# In[43]:


plot_degree_dist(G)


# In[44]:


order


# In[45]:


len(order)


# In[46]:


y=[]


# In[47]:


for x in range(len(order)-1,len(order)-696,-1):
    y.append(order[x][0])


# In[48]:


y


# In[34]:





# In[35]:





# In[ ]:





# In[ ]:




