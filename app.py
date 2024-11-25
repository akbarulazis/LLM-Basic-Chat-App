# import streamlit
import streamlit as st
#import open ai
from openai import OpenAI

from dotenv import load_dotenv

import os

# load env variables
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
load_dotenv()
st.set_page_config(page_title="Basic Chat APP", page_icon=":robot:")
st.title("Basic Chat App clone")
client = OpenAI(api_key =os.getenv('OPENAI_API_KEY') )
if 'openai_model' not in st.session_state:
    st.session_state['openai_model'] = "gpt-4o"

if 'message' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input('What is up??')
if prompt:
    st.session_state.messages.append({'role':'user', 'content':prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({'role':'asisstant','content':response})
