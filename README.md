# Webscrapper generator with ChatGPT
This project is a tool to generate code for web scrapping using ChatGPT. The idea is to use the power of the GPT models to generate code for web scrapping projects.
The tech stack used includes langchain, streamlit, and openai.

Try it: [Space 🤗](https://huggingface.co/spaces/CognitiveLabs/GPT-auto-webscraping)

## Development
(Recomended to use a **virtual environment**, see [Venv](https://docs.python.org/3/tutorial/venv.html) for more information about)

```bash
pip install -m requirements.txt
```

Create a config.ini with the following information on your root directory

Visit [OpenAI](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) to get your API Key
```bash
[DEFAULT]
API-KEY = {fill the value with your OPENAI API Key}
```

Run the app

```bash
streamlit run app.py 
```

# How it works

The idea of the project is to use GPT to automatize code generation for web scrapping.
* The tool will return a method to be used in web scrapping projects.

* The first bot (GPT chain) will return a JSON with the information of the fields to be extracted.

* The second bot will return a function called **extract_info**.

* The function will receive the HTML of the page and will return the information extracted from the page.

### Video Demo
[![Demo video](https://j.gifs.com/gpqvPl.gif | width=300)](https://www.youtube.com/watch?v=_zeCun4OlCc)



# Steps to generate the code:
For now, the workflow has 2 manual steps, but the idea is to automatize the process in the future.

## Step 1: Get an HTML element from the page you want to extract information from
* Inspect the element from which you want to get the information
* Copy the HTML element and paste it into the input of the app
* Click on generate code

Here the **first chain** will generate a JSON with the information of the fields to be extracted
That JSON will be used in the **second chain** as expected output format to generate the code

## Step 2: Get the whole HTML of the page
* Copy the HTML of the entire page
* Paste it in the second input of the app to test it
* Click on test code

If it was successful you will see a table with the information extracted from the page.
