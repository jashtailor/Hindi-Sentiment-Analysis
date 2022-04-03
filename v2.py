# IMPORTING THE NECESSARY LIBRARIES
import streamlit as st

import pickle

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier

from zipfile import ZipFile

import json

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.header('''
Parampara, Pratishtha, Anushasan
''')

input = st.text_input('Enter your sentence in the Hindi Language')

st.form_submit_button(label="Submit")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

RFC = pickle.load(open('model.pkl', 'rb'))

file_name = "hindi_words2.zip"
with ZipFile(file_name, 'r') as zip1:
  zip1.extractall()

with open('hindi_words2.json', 'r') as fp:
  data = json.load(fp)
  
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
 
if submit_button:
  predict(input)
