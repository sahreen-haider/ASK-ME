import os
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.memory import ConversationBufferMemory
import streamlit as st
import whisper
import serpapi
from rec import *

OPENAI_KEY = "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"
SERPAPI_KEY = "654b8bee0c754d8a87403bc292cffb8c2296190e6bf88f86f96a7f4d67d118cf"

os.environ['OPENAI_API_KEY'] = OPENAI_KEY
os.environ['SERPAPI_API_KEY'] = SERPAPI_KEY

path_to_audio = '/Users/sahreenhaider/Documents/ASK-ME/data/prompt.mp3'

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

if col2.button('speak'):
    model = whisper.load_model('base')
    result = model.transcribe()

if col2.button('voice'):
    st.write('recording.......')
    record_audio(path_to_audio)
    st.write('recording ended.......')
    resultant = agent.run(transcribe_to_text(path_to_audio))
    st.write(resultant)
else:
    agent.run(prompt)
    st.write(result)