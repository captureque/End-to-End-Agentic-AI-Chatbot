import streamlit as st 
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json

class DisplayResultsStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_results_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase =="BasicChatbot":
            for event in graph.stream({'messages':("user",user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)

        elif usecase =="Chatbot with Tools":
            # prepare state and invoke the graph
            initial_state = {"messages":[user_message]}
            result = graph.invoke(initial_state)
            for message in result["messages"]:
                if type(message)== HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message)== ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool call start")
                        st.write(message.content)
                        st.write("Tool call end")
                elif type(message)== AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)

         