
# coding: utf-8

# For creating a file which have the random row data

import random as rand
import numpy as np


# In[8]:

f = open('data_insert.txt', 'w')


# In[9]:

for k in range(3):
    cname = '[C' + str(k) + ']'
    f.write(cname + ' ')
    for i in range(100):
        c = rand.randint(1, 4) * 10
        f.write(str(c) + str(' '))
    for j in range(14):
        c = 10
        f.write(str(c) + str(' '))
    for i in range(100):
        c = rand.randint(1, 4) * 10
        f.write(str(c) + str(' '))
    f.write('\n')


# In[10]:

f.close()


# In[ ]:



