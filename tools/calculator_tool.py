from langchain_core.tools import tool


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

# A class can have methods without needing __init__.
# previous calculator tool replaced
# class CalculatorTool:
#
#    def add(self, a, b):
#        return a + b
#
#   def multiply(self, a, b):
#        return a * b