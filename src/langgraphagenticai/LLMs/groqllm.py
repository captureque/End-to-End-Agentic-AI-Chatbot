import os 
import streamlit as st
from langchain_groq import ChatGroq


class Groqllm:
    def __init__(self,user_control_input): # Initializing user control
        self.user_control_input = user_control_input

    def get_llm_model(self):
        try:
            groq_api_key= self.user_control_input["GROQ_API_KEY"]
            selected_groq_model = self.user_control_input["selected_groq_model"]
            if groq_api_key == '' and os.environ["GROQ_API_KEY"] == '' :
                st.error("Please enter the Groq API key")

            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error Occured with Exception : {e}")
        return llm
    




        



        