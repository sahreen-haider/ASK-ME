import os
# from langchain_back import *
from credenti import *
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.memory import ConversationBufferMemory
import streamlit as st


os.environ['OPENAI_API_KEY'] = OPENAI_KEY
os.environ['SERPAPI_API_KEY'] = SERPAPI_KEY


st.title(':rainbow[ASK ME]')

llm = OpenAI(temperature=0.9)

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


