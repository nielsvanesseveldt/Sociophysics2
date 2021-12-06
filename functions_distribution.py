#!/usr/bin/env python
# coding: utf-8

# In[3]:


def get_coords_from_prob_landscape(t,t0,prob_landscape):
    import numpy as np
    if t < t0:
        prob_landscape = prob_landscape/(np.sum(prob_landscape))
        index = np.arange(0,3150)
        chosenindex = np.random.choice(index,p=prob_landscape.ravel())
        x_goal, y_goal = chosenindex//150, chosenindex%150
    elif t>= t0:
        x_goal, y_goal = 1,1
    return x_goal, y_goal


# In[ ]:




