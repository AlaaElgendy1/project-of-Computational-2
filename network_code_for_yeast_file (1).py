#!/usr/bin/env python
# coding: utf-8

# In[12]:


import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("SaccharomycesCerevisiaeS288C_htb_hq.txt",sep="\t",usecols=["Uniprot_A","Uniprot_B"])


# In[13]:


G=nx.from_pandas_edgelist(df,"Uniprot_A","Uniprot_B",create_using=nx.DiGraph())


# In[14]:


degrees=dict(G.degree())
order=sorted(degrees.items(),key=lambda t:t[1])
x,y=zip(*order)
plt.plot(x,y)
plt.show()


# In[26]:


from collections import Counter
degree_sequence = [G.degree(n) for n in G.nodes]
degree_counts = Counter(degree_sequence)
min_degree, max_degree = min(degree_counts.keys()), max(degree_counts.keys())
plt.xlabel("Degree", fontsize=20)
plt.ylabel("Frequency", fontsize=20)
plot_x = list(range(min_degree, max_degree + 1))
plot_y = [degree_counts.get(x, 0) for x in plot_x]
plt.bar(plot_x, plot_y)


# In[16]:


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


# In[17]:


plot_degree_dist(G)


# In[29]:


order


# In[30]:


len(order)


# In[32]:


y=[]


# In[33]:


for x in range(len(order)-1,len(order)-252,-1):
    y.append(order[x][0])


# In[36]:


y


# In[34]:





# In[35]:





# In[ ]:





# In[ ]:




