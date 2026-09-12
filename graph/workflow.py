from langgraph.graph import StateGraph, END
from state.agent_state import AgentState


class Workflow:

    def __init__(
        self,
        supervisor_agent,
        research_agent,
        calculator_agent,
        reviewer_agent
    ):
        self.supervisor_agent = supervisor_agent
        self.research_agent = research_agent
        self.calculator_agent = calculator_agent
        self.reviewer_agent = reviewer_agent

        self.graph = StateGraph(AgentState)
        self.graph.add_node("supervisor", self.supervisor_node)
        self.graph.add_node("calculator", self.calculator_node)
        self.graph.add_node("research", self.research_node)
        self.graph.add_node("reviewer", self.reviewer_node)

        self.graph.set_entry_point("supervisor")

        self.graph.add_conditional_edges(
            "supervisor",
            lambda state: state["next_agent"],
            {
                "calculator": "calculator",
                "research": "research"
                }
        )

        self.graph.add_edge("calculator", "reviewer")
        self.graph.add_edge("research", "reviewer")
        self.graph.add_edge("reviewer", END)

        self.app = self.graph.compile()

    def run(self, user_query):
        
        initial_state = {
            "user_query": user_query,
            "next_agent": "",
            "agent_response": "",
            "final_answer": ""
        }
        result = self.app.invoke(initial_state)
        return result

    def supervisor_node(self, state):
        query = state["user_query"]
        next_agent = self.supervisor_agent.route(query)
        state["next_agent"] = next_agent
        
        return state


#    def calculator_node(self, state):
#        query = state["user_query"]
#        result = self.calculator_agent.run(25, 40)
#        state["agent_response"] = str(result)
#        return state

    def calculator_node(self, state):
        query = state["user_query"]
        result = self.calculator_agent.run(query)
        state["agent_response"] = str(result)
        return state


    def research_node(self, state):
        query = state["user_query"]
        result = self.research_agent.run(query)
        state["agent_response"] = result
        return state


    def reviewer_node(self, state):
        response = state["agent_response"]
        final_answer = self.reviewer_agent.review(response)
        state["final_answer"] = final_answer
        return state




# self.graph = StateGraph(AgentState) means
# Create a LangGraph workflow and tell it:

# "All information travelling
# through this workflow must
# follow the AgentState structure."

# AgentState will be the shared state used by the graph.

# BEFORE
# user_query = "multiply 25 and 40"
# next_agent = ""

# AFTER
# user_query = "multiply 25 and 40"
# next_agent = "calculator"