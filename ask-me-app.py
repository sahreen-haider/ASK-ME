import os
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.memory import ConversationBufferMemory
import streamlit as st
from rec import *
from credentials import *


os.environ['OPENAI_API_KEY'] = key_1
os.environ['SERPAPI_API_KEY'] = key_2

path_to_audio = '/Users/sahreenhaider/Documents/ASK-ME/data/prompt.mp3'

col_L, col_T = st.columns([2, 8])

with col_L:
    st.image('/Users/sahreenhaider/Documents/ASK-ME/data/_1320224e-7ac8-4d17-b833-d527334b6acf.jpeg', width=100)

with col_T:
    st.title(':rainbow[ASK ME]')

temp = st.slider(label='How creative should be the ASK ME CHAT be: ', min_value=0.0, max_value=1.0, value=0.9)

llm = OpenAI(temperature=temp)

memory = ConversationBufferMemory()

tools = load_tools(['serpapi', 'llm-math'], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory = memory,
    verbose = False
)
col1, col2 = st.columns(2)

prompt = col1.text_input('Enter your Prompt here: ')
voice = col2.button('voice')
if prompt:
    result = agent.run(prompt)
    st.write(result)

else:
    if col2:
        st.write('recording.......')
        record_audio(7, path_to_audio)
        st.write('recording ended.......')
        resultant = agent.run(transcribe_to_text(path_to_audio))
        st.write(resultant)