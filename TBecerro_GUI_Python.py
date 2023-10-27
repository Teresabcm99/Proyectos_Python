#!/usr/bin/env python
# coding: utf-8

# # GUI

# In[9]:


import pandas as pd
datafile='put your file.csv'
df_copy = pd.read_csv(datafile)
df_copy


# In[10]:


import PySimpleGUI as sg
import pandas as pd

df_copy
sg.theme('LightPurple')
font = ('Calibri', 25)

layout = [  [sg.Text("Enter word")],
            [sg.InputText()],
            [sg.Submit()] ]

window = sg.Window('Find data in the database', layout, font=font)

event, values = window.read()                   

output = df_copy.loc[df_copy["target"]== values[0]]

#sg.print('Results of the words in  database', output)

window.close()
output


# In[ ]:




