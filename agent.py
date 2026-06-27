from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from tools import search, scrape_url
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

HUGGINGFACE_API_KEY= (
    st.secrets.get("HUGGINGFACE_API_KEY")
    or os.getenv("HUGGINGFACE_API_KEY")
)

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=HUGGINGFACE_API_KEY
)

model = ChatHuggingFace(llm=llm)

#1st agent 
def build_search_agent():
    return create_agent(
        model=model,
        tools=[search]
    )
    
# 2nd agent 
def build_reader_agent():
    return create_agent(
        model=model,
        tools=[scrape_url]
    )


writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional.""")
])


writer_chain = writer_prompt | model | StrOutputParser()

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | model | StrOutputParser()