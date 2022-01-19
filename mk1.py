import streamlit as st
import indicnlp 
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


