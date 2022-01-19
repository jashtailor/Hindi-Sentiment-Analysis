import streamlit as st
import indicnlp 
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator

st.write('Heeeeellooooooooooooo')
title = st.text_input('Enter in Hindi')
st.write('The current movie title is', title)

Host_Country = st.selectbox('Select HomeTeamName name:',('France', 'Spain', 'Italy', 'England', 'Belgium', 'Portugal','Sweden'))
st.write('You selected:', Host_Country)
