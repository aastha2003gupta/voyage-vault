from langchain.llms import GooglePalm
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import DuckDuckGoSearchRun
from duckduckgo_search import DDGS
import json
import scrapy
import requests
from bs4 import BeautifulSoup
api_key = ""
google_llm = GooglePalm(google_api_key=api_key)

st.title('Cuisine Information & Top Restaurants')

option = st.selectbox('Select Information Type', ['Cuisine Information', 'Top 10 Restaurants'])

place_prompt = st.text_input('Enter the place you want information about')

if place_prompt:
    if option == 'Cuisine Information':
        cuisine_info_template = PromptTemplate(
            input_variables=['prompt', 'cuisine_research'],
            template='Provide detailed information about the cuisine of {prompt} along with famous dishes based on DuckDuckGo research: {cuisine_research}.'
        )

        try:
            cuisine_research = DuckDuckGoSearchRun().run(f"Cuisine of {place_prompt}")
            cuisine_info_chain = LLMChain(llm=google_llm, prompt=cuisine_info_template, verbose=True, output_key='cuisine_info')
            cuisine_info = cuisine_info_chain.run(prompt=place_prompt, cuisine_research=cuisine_research)

            st.write("### Cuisine Information:")
            st.write(cuisine_info)

        except Exception as e:
            st.error(f"An error occurred: {e}")

    elif option == 'Top 10 Restaurants':
        def remove_duplicate_empty_lines(text):
            lines = text.splitlines()
            cleaned_lines = [line.strip() for line in lines if line.strip()]
            cleaned_text = '\n'.join(cleaned_lines)
            return cleaned_text
        tourist_template = PromptTemplate(
            input_variables=['prompt', 'duckduckgo_research'],
            template ="""
                Here is some text extracted from the webpage by bs4:
                ---------
                {duckduckgo_research}
                ---------

                Web pages can have a lot of useless junk in them. 
                For example, there might be a lot of ads, or a 
                lot of navigation links, or a lot of text that 
                is not relevant to the topic of the page. We want 
                to extract only the useful information from the text.

                You can use the url and title to help you understand 
                the context of the text.
                Please extract only the useful information from the text. 
                Try not to rewrite the text, but instead extract 
                only the useful information from the text.

                I want to extract top 10 restaurant names in {prompt} along with their exact location, suggested dish and a small description from the above extracted text 
            """
        )
        tourist_chain = LLMChain(llm=google_llm, prompt=tourist_template, verbose=True, output_key='places')


        extracted_text = ''
        with DDGS() as ddgs:
            results = list(ddgs.text(f'top 10 restaurants in {place_prompt}', region='wt-wt', safesearch='off', timelimit='y', max_results=1))
        urls = [result['href'] for result in results]

        for url in urls:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                title = soup.title.string
                text = soup.get_text()
                cleaned_text = remove_duplicate_empty_lines(text)

                extracted_text += cleaned_text + '\n\n'  

                
        try:
            max_bytes = 48000
            if len(extracted_text.encode('utf-8')) > max_bytes:
                reduction_factor = max_bytes / len(extracted_text.encode('utf-8'))
                new_text_length = int(len(extracted_text) * reduction_factor)
                
                extracted_text = extracted_text[:new_text_length]
            places = tourist_chain.run(prompt=place_prompt, duckduckgo_research=extracted_text)
            if places:
                st.write(places)
            else:
                
                st.write("No information found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")


