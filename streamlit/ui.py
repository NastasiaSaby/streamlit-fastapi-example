import streamlit as st
import requests

st.title('Form example: What is your favourite film?')

# fastapi endpoint
url = 'http://fastapi:8000'
endpoint = '/postfilm'

option = st.selectbox(
     'How would you like to be contacted to speak more about your favourite film?',
    ('Email', 'Home phone', 'Mobile phone'))

title = st.text_input('Film title', 'Life of Brian')


def process(title, option, server_url: str):

    r = requests.post(server_url, json={"title": title, "option": option})

    return r


if st.button('Submit'):

    if title == None or title == "":
        st.write("Insert a title!")  # handle case with no image
    else:
        result = process(title, option, url + endpoint)
        if (result.status_code == 200):
            st.write(result)
            jsonDecoded = result.json()
            st.write("Your favourite film is " + jsonDecoded["YourTitle"])
            st.write("You would like to be contacted by " + jsonDecoded["YourOption"])

