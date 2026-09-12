# State is so important in LangGraph: different nodes/agents can read 
# information from it and return updates to it.

from typing import TypedDict


class AgentState(TypedDict):
    user_query: str
    next_agent: str
    agent_response: str
    final_answer: str












# "Whenever we use an AgentState dictionary, I expect it to have 
# a key called user_query, and its value should be a string."


# If the user asks:"What is 25 × 40?"
# The agent state should be:

# {
#   "user_query": "What is 25 × 40?"
# }

# If the user asks:"What is the capital of France?"
# The agent state should be:

# {
#   "user_query": "What is the capital of France?"
# }
