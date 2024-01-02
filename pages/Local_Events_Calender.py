from langchain.llms import GooglePalm
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import DuckDuckGoSearchRun
from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

api_key = ""
google_llm = GooglePalm(google_api_key=api_key)

st.title('Local Events')

prompt = st.text_input('Enter the place ')

def remove_duplicate_empty_lines(text):
    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    cleaned_text = '\n'.join(cleaned_lines)
    return cleaned_text

events_template = PromptTemplate(
    input_variables=['prompt', 'duckduckgo_research'],
    template="""
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

        I want to extract information about local events in {prompt} along with important contacts and locations and time and date
    """
)
events_chain = LLMChain(llm=google_llm, prompt=events_template, verbose=True, output_key='events')

extracted_text = ''
with DDGS() as ddgs:
    results = list(ddgs.text(f'Local Events in {prompt}', region='wt-wt', safesearch='off', timelimit='y', max_results=2))

if len(results) > 0:  
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

        events_info = events_chain.run(prompt=prompt, duckduckgo_research=extracted_text)
        if events_info:
            st.write(events_info)
        else:
            st.write("No information found.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("No results found for the given query.")
