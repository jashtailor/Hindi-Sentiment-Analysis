# IMPORTING THE NECESSARY LIBRARIES
import streamlit as st

import pickle

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier

from zipfile import ZipFile

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.header('''
Parampara, Pratishtha, Anushasan
''')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

input = st.text_input('Enter your sentence in the Hindi Language')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

RFC = pickle.load(open('model.pkl', 'rb'))

file_name = "hindi_words2.zip"
with ZipFile(file_name, 'r') as zip1:
  zip1.extractall()
