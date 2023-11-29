import os
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.memory import ConversationBufferMemory
import streamlit as st
import whisper

import serpapi
from audio_recorder_streamlit import audio_recorder
# from decouple import config
OPENAI_KEY = "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"
SERPAPI_KEY = "654b8bee0c754d8a87403bc292cffb8c2296190e6bf88f86f96a7f4d67d118cf"

os.environ['OPENAI_API_KEY'] = OPENAI_KEY
os.environ['SERPAPI_API_KEY'] = SERPAPI_KEY


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
prompt = col1.text_input('**Please enter your Prompt here:** ')
audio_bytes = audio_recorder(
    text="record",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="user",
    icon_size="2x",

)
if audio_bytes:
    model = whisper.load_model('base')
    result = model.transcribe(col2.audio(audio_bytes, format="audio/wav"))
if prompt:
    resultant = agent.run(prompt)
    st.write(resultant)
else:
    agent.run(result["text"])
    st.write(result)