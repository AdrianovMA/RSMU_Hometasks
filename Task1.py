#!/usr/bin/env python
# coding: utf-8

# Задача 1
# Дано имя файла: folder1/folder2/file.ext
# Необходимо вывести на экран его расширение с помощью стандартного модуля re.

# In[15]:


import re


# In[16]:


help(re)


# In[28]:


filename = input()


# In[29]:


pattern = '\..*'
a = re.search(pattern, filename)
print(a.group())


# In[ ]:




