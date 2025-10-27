from langgraph.graph import StateGraph
from langgraph.graph import START,END
from src.langgraphagenticai.State.state import State
from src.langgraphagenticai.Nodes.BasicChatbotNode import BasicChatbotNode1
from src.langgraphagenticai.Tools.Search_tool import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition
from src.langgraphagenticai.Nodes.chatbotwithtools_Node import ChatbotwithToolsNode
from src.langgraphagenticai.Nodes.ai_news_node import AINewsNode
class GraphBuilder:
    def __init__(self,model):
        self.llm = model 
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using Langgraph. 
        This method initializes a chatbot node using the 'BasicChatbotNode' class and integrates it into the graph . 
        The chatbot node is set as both as both the entry and exit point of the graph. 
        """
        self.basic_chatbot_node = BasicChatbotNode1(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)


    def chatbot_with_tools_graph(self):
        """
        Builds an advanced chatbot graph with tool interaction.
        This method creates a chatbot graph that includes both a chatbot node and a tool node. 
        It defines tools, initializes the chatbot with tool capabilities, and sets up conditional and direct edges between nodes.
        The chatbot node is set as the entry point.
        """

        # Defining the Tool and ToolNode 

        tools = get_tools()
        tool_node = create_tool_node(tools)

        #Defining LLM

        llm = self.llm

        #Defining the chatbot node 
        chatbotwithtool = ChatbotwithToolsNode(llm)
        chatbot_node = chatbotwithtool.create_chatbot(tools)



        ##Add nodes
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
       # self.graph_builder.add_edge("chatbot",END)

    def AI_NewsSummarizer_graph(self):

        ai_news_node = AINewsNode(self.llm)

        # Add Nodes 
        self.graph_builder.add_node("FetchNews", ai_news_node.fetch_news)
        self.graph_builder.add_node("Summarizer", ai_news_node.summarize_news)
        self.graph_builder.add_node("SaveResults", ai_news_node.save_result)

        #Add Edges 
        self.graph_builder.set_entry_point("FetchNews")
        self.graph_builder.add_edge("FetchNews","Summarizer")
        self.graph_builder.add_edge("Summarizer","SaveResults")
        self.graph_builder.add_edge("SaveResults",END)

    def setup_graph(self, usecase: str):
        """
        sets up the graph for the selected use case.
        """

        if usecase == "BasicChatbot":
            self.basic_chatbot_build_graph()

        if usecase == "Chatbot with Tools":
            self.chatbot_with_tools_graph()

        if usecase == "AI News Generator":
            self.AI_NewsSummarizer_graph()
        
        return self.graph_builder.compile()

        
            



          
        