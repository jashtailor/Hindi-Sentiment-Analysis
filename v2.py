# importing the necessary libraries
import streamlit as st

import pickle

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier

from zipfile import ZipFile

import json

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# design elements
st.header('''
Parampara, Pratishtha, Anushasan
''')
# Ye is gurukul ke teen stambh hai. Ye wo aadarsh hain jinse hum aapka aane waala kal banaate hain.

input = st.text_input('Enter your sentence in the Hindi Language')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# loading the hindi dictionary
file_name = "hindi_words_v3.zip"
with ZipFile(file_name, 'r') as zip1:
  zip1.extractall()

with open('hindi_words_v3.json', 'r') as fp:
  data = json.load(fp)

# loading the model using pickle
RFC = pickle.load(open('model1.pkl', 'rb'))

# predict function
def predict(text):
  # 1 -> positive
  # 0 -> negative
  # print(text)
  max_len = 48
  txt_seq = []
  lst = []
  tokenized_input = text.split(' ')
  for each in tokenized_input:
    txt_seq.append(data[each])
  if len(txt_seq)<max_len:
    difference = max_len - len(txt_seq)
    # print(difference)
    zeroes = [0]*difference
    lst = zeroes + txt_seq
  # print(lst)
  lst1 = np.asarray(lst, dtype=np.float64)
  new_lst1 = lst1.reshape(1, -1)
  a = RFC.predict(new_lst1)
  if a==1:
    st.write('Positive')
  elif a==0:
    st.write('Negative')

if st.button(label="Submit"):
  try:
    predict(input)
  except:
    st.write('Error')
else:
  pass
