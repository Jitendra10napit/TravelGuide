import os

from langchain_classic.chains.summarize.map_reduce_prompt import prompt_template
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import PromptTemplate

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
llm=ChatOpenAI(model="gpt-5.4-mini", api_key=OPENAI_API_KEY)

prompt_template = PromptTemplate(
    input_variables=["city", "month", "language","budget"],
    template="""Welcome to the {city} travel guide!
    If you're visiting in {month}, here's what you can do:
    1. Must-visit attractions.
    2. Local cuisine you must try.
    3. Useful phrases in {language}.
    4. Tips for traveling on a {budget} budget.
    Enjoy your trip!
    """
)

st.title("Ask Anything")

city = st.text_input("Enter your city?")
month = st.text_input("Enter the number month of travel?")
language = st.text_input("Enter your language?")
budget = st.selectbox("Travel Budget",["Low", "Medium", "High"])

if city and month and language and budget:
    response = llm.invoke(prompt_template.format(city=city, month=month, language=language, budget=budget))
    st.write(response.content)
