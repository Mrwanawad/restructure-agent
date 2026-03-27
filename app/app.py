import streamlit as st
import os;     import sys;
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# streamlit run app/app.py
from llm.client import LLM


st.set_page_config( 'Restructuring Data Agent', layout= 'wide' )

llm = LLM( api_key= st.secrets['API_KEY'] )

st.markdown("""
## 🧠 Data Extraction Chatbot

Paste any messy or unstructured text (receipts, notes, or transcriptions), and get a clean Python dictionary.

- Returns only structured data  
- Automatically detects fields (date, items, total, etc.)  
- Handles missing or uncertain values  
- Normalizes numbers and formats output  

Enter your text below 👇
""")

user_text = st.text_area( label = 'Paste Your Unstructured text here:' )


@st.dialog( 'Output Dialog' )
def generate_output_dialog() :
    response = llm.call_llm( user_text )
    st.write( response )
    
    
    
    
    
if st.button( 'Apply' ) :
    generate_output_dialog()
    