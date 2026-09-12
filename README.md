# Multi-Agent Assistant

A learning-focused **Agentic AI project built with LangGraph and LangChain** to demonstrate how multiple specialized AI agents can collaborate within a state-based workflow.

The project implements **LLM-driven agent routing, specialized agents, tool calling, shared state, and workflow orchestration** using GPT-5.4-mini.

## Overview

The system receives a user query and passes it to a **Supervisor Agent**, which uses an LLM to determine which specialized agent should handle the request.

Currently, the system contains:

- **Supervisor Agent** – analyzes the user query and routes it to the appropriate agent.
- **Research Agent** – handles general knowledge and research-oriented questions using an LLM.
- **Calculator Agent** – handles mathematical queries and uses LLM tool calling to select and execute calculator tools.
- **Reviewer Agent** – processes the agent response and produces the final answer.

## Architecture

```text
                         USER
                          │
                          ▼
                  SUPERVISOR AGENT
                    GPT-5.4-mini
                          │
                    LLM Routing
                  ┌───────┴───────┐
                  ▼               ▼
           RESEARCH AGENT    CALCULATOR AGENT
            GPT-5.4-mini       GPT-5.4-mini
                                  │
                           LLM Tool Calling
                            ┌─────┴─────┐
                            ▼           ▼
                           add       multiply
                            │           │
                            └─────┬─────┘
                                  │
                  └───────┬───────┘
                          ▼
                    REVIEWER AGENT
                          │
                          ▼
                     FINAL ANSWER
```

## How It Works

For a mathematical query:

```text
User: "Multiply 37 and 18"
        ↓
Supervisor Agent
        ↓
LLM selects "calculator"
        ↓
Calculator Agent
        ↓
LLM selects multiply tool
        ↓
Arguments generated:
a = 37
b = 18
        ↓
Python tool executes
        ↓
666
        ↓
Reviewer Agent
        ↓
Final Answer: 666
```

For a general question:

```text
User: "What is Agentic AI?"
        ↓
Supervisor Agent
        ↓
LLM selects "research"
        ↓
Research Agent
        ↓
LLM generates response
        ↓
Reviewer Agent
        ↓
Final Answer
```

## Key Concepts Demonstrated

This project was built to understand the core building blocks of Agentic AI systems:

- Multi-agent architecture
- LangGraph workflow orchestration
- StateGraph and shared agent state
- Nodes and edges
- Conditional routing
- LLM-based decision making
- Specialized AI agents
- LangChain tool calling
- Tool schemas using `@tool`
- `bind_tools()`
- LLM-generated tool arguments
- Python tool execution
- Object-oriented design for agents

## Tech Stack

- Python
- LangGraph
- LangChain
- OpenAI GPT-5.4-mini
- LangChain OpenAI
- uv
- Jupyter Notebook

## Project Structure

```text
Multi_agent_assistant/
│
├── agents/
│   ├── base_agent.py
│   ├── supervisor_agent.py
│   ├── research_agent.py
│   ├── calculator_agent.py
│   └── reviewer_agent.py
│
├── tools/
│   ├── calculator_tool.py
│   └── search_tool.py
│
├── graph/
│   └── workflow.py
│
├── state/
│   └── agent_state.py
│
├── config/
│   └── config.py
│
├── testing/
│   └── notebook.ipynb
│
├── main.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Example

```python
result = workflow.run("Multiply 37 and 18")

print(result["final_answer"])
```

Output:

```text
Final Answer: 666.0
```

## Environment Variables

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_openai_api_key
```

The `.env` file is excluded from Git using `.gitignore` and should never be committed to the repository.

## Purpose

This project was developed as a hands-on exercise to understand how **LLMs, agents, tools, state, and orchestration work together in an Agentic AI system**.

Rather than building a single LLM application, the project focuses on understanding how specialized agents can be coordinated through a graph-based workflow and how LLMs can dynamically make routing and tool-selection decisions.
