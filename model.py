import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import streamlit as st


nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')


st.title('Mood Detection App')
user_input = st.text_input("How was your Day?")
doc = nlp(user_input)
Polarity =  round(doc._.polarity, 2)


st.write('Your Mood Looks:','SAD..😔' if Polarity < 0 else 'HAPPY!!..😀')

# Subjectivity = round(doc._.subjectivity, 2)
# st.write('Subjectivity:',Subjectivity) 
# print(doc._.polarity)
# print(doc._.subjectivity)  
# print(doc._.assessments) 