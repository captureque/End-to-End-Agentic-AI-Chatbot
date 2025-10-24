from src.langgraphagenticai.State.state import State

class ChatbotwithToolsNode:
    """
    chatbot logic enhanced with tool integratation.
    """
    def __init__(self,model): #Loding the model
        self.llm =  model

    def process(self,state:State)-> dict:    # This method is optional , if there are no tool integration 
        """
        Processes the input state and generates a response with tool integration.
        """
        user_input = state['messages'][-1] if state['messages'] else ""  # else empty
        llm_response = self.llm.invoke([{"role": "user" ,"content": user_input}])  # will make the call to the tool

        #Simulate tool specific logic
        tools_response = f"Tool Integration for :'{user_input}'"
        return {"messages": [llm_response,tools_response]}
    

    def create_chatbot(self,tools):
        """
        Returns a chatbot node function
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state:State):
            """
            Chatbot logic for processing the input state and returning a response 
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        return chatbot_node
    


