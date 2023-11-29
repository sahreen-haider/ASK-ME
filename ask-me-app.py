import os
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.memory import ConversationBufferMemory
import streamlit as st
import serpapi
# from decouple import config


os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_KEY"]
os.environ['SERPAPI_API_KEY'] = st.secrets["SERPAPI_KEY"]


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
prompt = st.text_input('**Please enter your Prompt here:** ')
resultant = agent.run(prompt)
st.write(resultant)