# import streamlit
import streamlit as st
#import open ai
from openai import OpenAI

from dotenv import load_dotenv

import os

# load env variables
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
load_dotenv()
st.set_page_config(page_title="Bascc Chat APP", page_icon=":robot:")
client = OpenAI(api_key =os.getenv('OPENAI_API_KEY') )
if 'openai_model' not in st.session_state:
    st.session_state['openai_model'] = "gpt-4o"

if 'message' not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input('What is up??')
if prompt:
    st.session_state.message.append({'role':'user', 'content':prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    with st.chat_message('asisstant'):
        stream =client.chat.completions.create(
                model = st.session_state['openai_model'],
                message=[
                    {'role': m['role'], 'content':m['content']}
                    for m in st.session_state.message

                    ], stream = True,



        )
        response = st.write_stream(stream)
    st.session_state.message.append({'role':'asisstant','content':response})
