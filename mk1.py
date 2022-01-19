import streamlit as st
import indicnlp 
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator

st.write('Heeeeellooooooooooooo')
input_text = st.text_input('Enter in a sentence in Hindi')

lang = st.selectbox('Select Language:',('None','Gujarati', 'Punjabi', 'Kannada', 'Malayalam', 'Odia', 'Bengali'))

st.write(UnicodeIndicTransliterator.transliterate(input_text,"hi",lang))

