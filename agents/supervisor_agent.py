class SupervisorAgent:

    def __init__(self, name, model):
        self.name = name
        self.model = model



    def route(self, query):
        prompt = f"""

        You are a supervisor agent.
        Decide which agent should handle the user's request.
        Available agents:
            - calculator: for mathematical calculations
            - research: for questions requiring information or research
        User query: {query}
        Return only one word:
        calculator or research
        
    """
        response = self.model.invoke(prompt)
        return response.content.strip().lower()

    #def route(self, query):
    #    query = query.lower()
    #
    #    if "calculate" in query or "multiply" in query or "add" in query:
    #        return "calculator"

    #    return "research"


# Later, we can replace these simple if rules with the LLM deciding the route. 
# For now, just create this file.