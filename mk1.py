import streamlit as st
import indicnlp 
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator
from indicnlp.tokenize import indic_tokenize  

st.write('Parampara Pratishtha, Anushasan')
lang = st.selectbox('Select Language:',('None','Gujarati', 'Punjabi', 'Kannada', 'Malayalam', 'Odia', 'Bengali'))
input_text = st.text_input('Enter in a sentence in Hindi')

input__text = indic_tokenize.trivial_tokenize(input_text) 
if lang=='Gujarati':
  st.write(UnicodeIndicTransliterator.transliterate(input_text,"hi",'gu'))
elif lang=='Punjabi':
  st.write(UnicodeIndicTransliterator.transliterate(input_text,"hi",'pa'))
elif lang=='Kannada':
  st.write(UnicodeIndicTransliterator.transliterate(input_text,"hi",'kn'))
elif lang=='Malayalam':
  st.write(UnicodeIndicTransliterator.transliterate(input_text,"hi",'ml'))
if lang=='Odia':
  st.write(UnicodeIndicTransliterator.transliterate(input_text,"hi",'or'))
if lang=='Bengali':
  st.write(UnicodeIndicTransliterator.transliterate(input_text,"hi",'bn'))

