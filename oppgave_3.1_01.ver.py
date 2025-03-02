#!/usr/bin/env python
# coding: utf-8

# #%% oppgave 3.1 Formatert utskrift av beløp med rente

# In[21]:


# importere nødvending funksjonalitet fra pandas
import numpy as np


# In[61]:


#definere varibel for innskudd
beløp = 10000 # innskudd start
rente = 1.85 # årlig rente
t = 5 # antall år


# In[41]:


# hva blir blir beløpet på kontoen etter 5 år på konto?


# In[63]:


beløp_etter_5år = int(beløp*(1 + rente/100)**5)


# In[65]:


print(f"Beløpet har vokst til kr : {beløp_etter_5år:.2f} etter 5 år")


# In[ ]:




