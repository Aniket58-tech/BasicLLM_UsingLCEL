import requests
import streamlit as st
import json


def get_groq_response(input_text):
    json_body={
        "input": {
            "language": "hindi",
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }
    print("Sending JSON:", json.dumps(json_body, indent=2))

    response=requests.post("http://127.0.0.1:8000/chain/invoke",json=json_body)

    print(response.json())


    return response.json()

## Streamlit app
st.title("LLM Application Using LCEL")
input_text=st.text_input("Enter the text you want to convert to Hindi")

if input_text:
    st.write(get_groq_response(input_text))