class BaseAgent:

    def __init__(self, name, model, tools=None):
        self.name = name
        self.model = model
        self.tools = tools or []