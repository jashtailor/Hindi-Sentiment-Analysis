import streamlit as st

import pickle

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier

st.header('''
Parampara, Pratishtha, Anushasan
''')

input = st.text_input('Enter your sentence in the Hindi Language')
