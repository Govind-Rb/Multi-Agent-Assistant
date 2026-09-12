from agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):

    def __init__(self, name, model, tools=None):
        self.name = name
        self.model = model
        self.tools = tools or []

    def run(self, query):
        prompt = f"""
        You are a research agent.
        Answer the following question clearly and concisely.
        Question: {query}
        """
        response = self.model.invoke(prompt)
        return response.content


#    def run(self, query):
#        search_tool = self.tools[0]
#
#        result = search_tool.search(query)
#
#        return result