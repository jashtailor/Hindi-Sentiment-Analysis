import streamlit as st
import indicnlp 
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator

st.write('Heeeeellooooooooooooo')
title = st.text_input('Enter in Hindi')
st.write('The current movie title is', title)

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

