
# coding: utf-8

# In[1]:


#  This is a very simple die roll simulator.  It is constrained to single digit numbers of dice and does not constrin the user to a number of sides.


# In[2]:


print ('Welcome to my dice script!')


# In[3]:


name = input ('What is your name?')


# In[4]:


print ('Hello, ' + name + ', what type of die do you want to roll? \nFor example "n"d4, 6, 10, 12, 20, 100')

die_type = input()


# In[5]:


number = die_type[:1]

n = int(number)


# In[6]:


sides = die_type[2:]

s = int(sides)


# In[7]:


# The lines below detect a d20 roll and change the output of a 1 or 20 to a text message.


# In[8]:


import random

for rolls in range (n):
    
    rr = (random.randint (1,s))
    
    if s == 20:
        if rr == 1:
            print ('Crit FAIL!')
            
        elif rr == 20:
            print ('Crit HIT!')
            
        else:
            print (rr)

