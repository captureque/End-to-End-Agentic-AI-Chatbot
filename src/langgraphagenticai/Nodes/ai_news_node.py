from tavily import TavilyClient 
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:
    def __init__(self,llm):
        """
        Initialize the AINewsNode with API keys for Tavily and Groq 
        """

        self.tavily = TavilyClient() # Initialize Tavily Client
        self.llm = llm
        self.state = {} # Initialize state dictionary. This is used to capture/store various steps in this file so that they can be used later.
                         #for example, the news articles fetched from Tavily API are stored in self.state['news_articles'].

    def fetch_news(self,state:dict)->dict:  # Fetch latest AI news articles using Tavily API
        """
        Fetch AI news based on the specified frequency.

        Args : state (dict): A dictionary containing the 'frequency' key to specify news frequency.

        Returns:
            dict: Updated state with 'news_data' key containing fetched news articles.
        """                 

        frequency = state["messages"][0].content.lower()  # Extract frequency from input message
        self.state['frequency'] = frequency
        time_range_map = {
            "daily": "d",
            "weekly": "w",
            "monthly": "m",
            "yearly": "y"}
        days_map = {'daily':1,'weekly':7,'monthly':30,'yearly':365}


        response = self.tavily.search(   # Fetch news articles from Tavily API
            query = " Top Artificial Intelligence (AI) technology news India and Globally",
            topic="news",
            time_range= time_range_map[frequency],
            include_answer="advanced",
            max_results=15,
            days = days_map[frequency] 
                  )
        self.state['news_data'] = response.get('results',[])  # Store fetched news articles in state        
        return self.state 
    
    def summarize_news(self,state:dict)->dict:
        """
        Summarize the fetched AI news articles using the provided language model.

        Args:
            state(dict): The state dictionary containing 'news_data'

        Returns:
            dict : Update state with 'summary' key containing the summarized news.
            
        """

        news_items = self.state['news_data']  # Retrieve fetched news articles from state

        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system","""Summarize AI news article into markdown format. For each item include:
                 - Date in **YYYY-MM-DD** format in IST timezone
                 -Concise sentences summary from latest news
                 -Sort news by date wise(latest first)
                 -Source url as link
                 use format:
                 ### [Date]
                 - [summary](url)"""),
                 ("user","Articles: \n{articles}")

            ]
        )

        articles_str = "\n\n".join([
            f"Content: {item.get('content','')}\n URL: {item.get('url','')}\n Published At: {item.get('published_at','')}"
            for item in news_items
        ])

        response = self.llm.invoke(prompt_template.format(articles=articles_str))  # Generate summary using LLM
        self.state['summary'] = response.content  # Store summary in state
        return self.state
    
    def save_result(self,state):
        frequency = self.state['frequency']
        summary = self.state['summary']
        filename = f"./AINews/{frequency}_summary.md" # Define filename based on frequency
         # Save the summary to a markdown file
        with open(filename,"w") as file:
            file.write(f" #{frequency.capitalize()} AI News Summary\n\n")
            file.write(summary)
        self.state['filename']= filename
        return self.state 
    
