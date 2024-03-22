import streamlit as st
import tiktoken
from io import StringIO

st.set_page_config(page_title='Tokenizer')
st.title('Tokenizer')
st.subheader("Count tokens from file")


st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)

option=st.radio(
        "Select the model",
        options=["gpt-3.5-turbo",'gpt-4'],
    )
st.write(option) 

option="gpt-3.5-turbo"
upload_file=st.file_uploader('Upload txt file',type='txt')

   

def ifSubmitted():
            stringio = StringIO(upload_file.getvalue().decode("utf-8"))
            txt = stringio.read()
            
            encoding = tiktoken.encoding_for_model(option)
            num_tokens = len(encoding.encode(txt))
            
            st.write('tokens: ',num_tokens, 'in', option)
            st.write(txt)
            
if upload_file is not None:
        ifSubmitted()
        #encoding = tiktoken.encoding_for_model(option)
        #num_tokens_box = len(encoding.encode(txtBox))
        #st.write(num_tokens_box)

st.write("#")
st.subheader("Enter text to count tokens")
txtBox = st.text_area("")
encoding = tiktoken.encoding_for_model(option)
num_tokens_box = len(encoding.encode(txtBox))
st.write("Tokens: ", num_tokens_box)
#st.write("Tokens: ", (encoding.encode(txtBox)))
#[encoding.decode_single_token_bytes(token) for token in (encoding.encode(txtBox)) ]