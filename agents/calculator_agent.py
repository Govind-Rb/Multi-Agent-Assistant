from agents.base_agent import BaseAgent
from tools.calculator_tool import multiply, add


class CalculatorAgent(BaseAgent):

    def __init__(self, name, model, tools=None):
        self.name = name
        self.model = model
        self.tools = tools or []

        self.model_with_tools = self.model.bind_tools([multiply, add])


    def run(self, query):
        response = self.model_with_tools.invoke(query)
        
        tool_call = response.tool_calls[0]
        
        if tool_call["name"] == "multiply":
            result = multiply.invoke(tool_call["args"])
            
        elif tool_call["name"] == "add":
            result = add.invoke(tool_call["args"])
            
        return result


#    def run(self, a, b):
#        calculator = self.tools[0] # Agent contains a list of tool objects, but here only one tool will be there hence [0].
#
#        result = calculator.multiply(a, b)
#
#        return result

# There is no connection yet between CalculatorAgent and CalculatorTool till now.   
