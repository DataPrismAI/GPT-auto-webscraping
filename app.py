from AssistantService import GPTAssistant
from openai.error import AuthenticationError
import streamlit as st
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
if 'DEFAULT' in config:
    assistant_api_key = config['DEFAULT'].get('API-KEY', '')

st.title("Web Scraping Assistant")
st.write("This app helps you to extract data from HTML code using web scraping. It uses GPT-3.5-turbo to generate the code for you.")
st.write("Contribute to this project on [GitHub](https://github.com/CognitiveLabs/GPT-auto-webscraping)")
if assistant_api_key == '':
    assistant_api_key = st.text_input("Paste your API key here:")
    if assistant_api_key:
        gpt_assistant = GPTAssistant(assistant_api_key)
else:
    gpt_assistant = GPTAssistant(assistant_api_key)

html_content = st.text_input("Paste your piece of HTML here:")

if html_content:
    if st.button("Extract data format"):
        try:
            output = gpt_assistant.chain_response_format(html_content)
            st.session_state['output_format'] = output
        except NameError:
            st.write("Complete the API key field")
        except AuthenticationError:
            st.write("Invalid API key")

if 'output_format' in st.session_state:
    output_format = st.code(st.session_state['output_format'], language="json")
    
    if st.button("Generate the code"):
        try:
            python_code = gpt_assistant.chain_code_generator(st.session_state['output_format'], html_content)
            st.session_state['code_generated'] = python_code
            st.session_state['code_generated_exec'] = python_code + "\nresult = extract_info(html_data)"

        except NameError:
            st.write("Complete the API key field")
        except AuthenticationError:
            st.write("Invalid API key")


if 'code_generated' in st.session_state:
    python_function_label = st.write("Here is your python function:")
    code_generated = st.code(st.session_state['code_generated'],language="python")
    full_content = st.text_input("Paste your complete HTML here:")
    if full_content and st.button("Test the code"):
        html_data = full_content
        result = None
        exec(st.session_state['code_generated_exec'], globals())
        if result:
            st.write("data extracted successfully")
            # show data in table
            st.table(result)
        else:
            st.write("error extracting data")

with st.expander(label="How to use this app"):

    st.write("1. Paste the html code of your target element in the first text box and press \"Enter\"")
    example = st.button("Show example")
    if example:
        example = False
        text_area = st.text_area("Example", value='<li><div class="product"> <h3 class="title">Product 1</h3> <p class="description">This is the description of the product 1</p> <span class="price">10.00</span> </div></li>')
        close_example = st.button("Close example")
        if close_example:
            example = False
            close_example.disabled = True
            text_area = None

    st.write("2. Click on the button 'Extract data format'")

    st.write("3. Click on the button 'Generate the code'")

    st.write("4. Paste the complete html code in the last text box to test the auto generated code")

    st.write("5. Copy the code and include it in your own projects")
