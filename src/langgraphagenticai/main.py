import streamlit as st

from src.langgraphagenticai.UI.streamlitUI.loadui import LoadStreamlitUI # used to connect main to StreamlitUI
from src.langgraphagenticai.LLMs.groqllm import Groqllm
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.UI.streamlitUI.display_results import DisplayResultsStreamlit
# making that connection

def load_langgraph_agenticai_app():
    """
   Loads and runs the LangGraph Agentic AI application with streamlit UI. This function initializes the UI, handles user input , configures the LLM Model,
    sets up the graph based on the selected use case , and display the output while implementing exception handling for robustness.  
    """

    ##LoadUI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return
    user_message = st.chat_input("Enter your message:")
# Next make connection to app.py


    if user_message:
        try:
            ## configure the LLMs
            obj_llm_config = Groqllm(user_control_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized" )
                return 
            
            
            # Initialize graph based on use case 
            usecase = user_input.get('selected_usecase')

            if not usecase:
                 st.error("Error: No use case selected ")
                 return
            
            ## Graph Builder 

            graph_builder = GraphBuilder(model)
            try:
                 graph = graph_builder.setup_graph(usecase) 
                 DisplayResultsStreamlit(usecase,graph,user_message).display_results_on_ui()       
                # when i call this function it will go to graphbuilder.py and call self.basic_chatbot_build_graph() functtion and load the specific graph 
            except Exception as e:
                 st.error(f"Error : Graph set up failed1 - {e} ")
                 return 
        
        except Exception as e:
            st.error(f"Error : Graph set up failed 2 - {e} ")
            return 










