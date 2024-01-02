from langchain.llms import GooglePalm
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
#from langchain.utilities import WikipediaAPIWrapper
from langchain.tools import DuckDuckGoSearchRun
import requests


api_key = ""
llm = GooglePalm(google_api_key=api_key, temperature=0.7)

st.title('Top Tourist Spots')
prompt = st.text_input('The place you are visiting')
tourist_template = PromptTemplate(
    input_variables=['prompt', 'wikipedia_research'],
    template='Provide top 10 tourist attractions in {prompt}  based on duckduckgo research: {wikipedia_research} along with links to the location and a 2 line description on them .Dont make anything up '
)

tourist_chain = LLMChain(llm=llm, prompt=tourist_template, verbose=True, output_key='places')

duckduckgo = DuckDuckGoSearchRun()
prompt_research='Give a list of top tourists attractions  in {prompt}'


if prompt:
        wiki_research = duckduckgo.run(prompt_research)
        places = tourist_chain.run(prompt=prompt, wikipedia_research=wiki_research)
        st.write("### Top 10 toursits spots:")
        st.write(places)


    
    

    
