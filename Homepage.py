import streamlit as st
from langchain.llms import GooglePalm
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import DuckDuckGoSearchRun
from duckduckgo_search import DDGS

st.set_page_config(
    page_title="VoyageVault"
)

st.sidebar.success("Select a page above")

st.title('VoyageVault')

import requests
api_key = ""
google_llm = GooglePalm(google_api_key=api_key)

prompt = st.text_input('The place you are visiting')
def weather(prompt):
        api_key = ''
        while True:
            result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={prompt}&units=metric&appid={api_key}')
            if result.json()['cod'] == '404':
                print("Invalid location!")
                continue
            break
        description = result.json()['weather'][0]['description']
        temperature = round(result.json()['main']['temp'])
        feels_like = round(result.json()['main']['feels_like'])
        high = round(result.json()['main']['temp_max'])
        low = round(result.json()['main']['temp_min'])
        st.write(f"The weather in {prompt[0].upper()}{prompt[1:]} is {temperature}° C with {description}.")
        st.write(f"It feels like {feels_like}° C.")
        st.write(f"Today's high is {high}° C and today's low is {low}° C.")

place_template = PromptTemplate(
    input_variables=['prompt', 'wikipedia_research'],
    template='Provide informationn for a tourism perspection on  {prompt}  based on duckduckgo research: {wikipedia_research} ,tell about the history , local culture and some famous and unknown facts about the place '
)

tourist_chain = LLMChain(llm=google_llm, prompt=place_template, verbose=True, output_key='info')

duckduckgo = DuckDuckGoSearchRun()
prompt_research='Give information about in {prompt}'


if prompt:
        weather(prompt)
        wiki_research = duckduckgo.run(prompt_research)
        info= tourist_chain.run(prompt=prompt, wikipedia_research=wiki_research)
        st.write(info)





