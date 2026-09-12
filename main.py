#from tools.calculator_tool import CalculatorTool
from tools.search_tool import SearchTool

from agents.calculator_agent import CalculatorAgent
from agents.research_agent import ResearchAgent
from agents.supervisor_agent import SupervisorAgent
from agents.reviewer_agent import ReviewerAgent

from graph.workflow import Workflow
from config.config import get_model

model = get_model()

#calculator_tool = CalculatorTool()
search_tool = SearchTool()


#calculator_agent = CalculatorAgent(
#    name="Calculator Agent",
#    model=model,
#    tools=[calculator_tool]
#)

calculator_agent = CalculatorAgent(
    name="Calculator Agent",
    model=model
)

research_agent = ResearchAgent(
    name="Research Agent",
    model=model,
    tools=[search_tool]
)

supervisor_agent = SupervisorAgent(
    name="Supervisor Agent",
    model=model
)

reviewer_agent = ReviewerAgent(
    name="Reviewer Agent",
    model=model
)

workflow = Workflow(
    supervisor_agent=supervisor_agent,
    research_agent=research_agent,
    calculator_agent=calculator_agent,
    reviewer_agent=reviewer_agent
)

result = workflow.run("Multiply 37 and 18")
print(result["final_answer"])
