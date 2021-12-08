#!/usr/bin/env python
# coding: utf-8

# In[3]:


def get_coords_from_prob_landscape(n,t,t0,prob_landscape):
    import numpy as np
    if t < t0:
        prob_landscape = prob_landscape/(np.sum(prob_landscape))
        index = np.arange(0,3150)
        chosenindex = np.random.choice(index,n,p=prob_landscape.ravel())
        x_goal, y_goal = chosenindex//150, chosenindex%150
    elif t>= t0:
        x_goal, y_goal = 1,1
    return x_goal, y_goal
# n is the amount of random coordinates you want
# t is the moment you're interested in
# t0 is the moment when the train arrives
# prob_landscape is the csv file you need to import

# In[ ]:




