Multi-Agent Research Assistant

This project implements a Multi-Agent Research Assistant that answers user queries using a coordinated workflow of AI agents and external tools.

The system combines LLMs, agent orchestration, backend APIs, and a user interface** to process research questions and return structured answers.

---

# Technologies Used

The project is built using the following technologies:

**LLM:Ollama (phi3)
**Agent Framework: LangGraph (stateful multi-agent workflow)
**MCP:FastMCP client + server
Backend:Django REST API
Frontend:Streamlit
Database:PostgreSQL
Cache:Redis

---

# Project Structure

```
MultiAgent
│
├── agents            # LangGraph agents (Planner + Research)
├── backend           # Django backend API
├── mcp_client        # MCP client implementation
├── mcp_server        # MCP server providing tools
├── streamlit_app     # Streamlit frontend UI
│
├── requirements.txt
└── All_Run.bat       # Script to start all services
```

---

# System Workflow

The system processes a user question using multiple agents.

```
User
  ↓
Streamlit UI
  ↓
Django REST API
  ↓
Planner Agent (LangGraph)
  ↓
Research Agent
  ↓
MCP Tool Server
  ↓
LLM (Ollama - phi3)
  ↓
Final Answer
```

Simplified flow:

```
User → Planner → Research → Answer
```

---

# How to Install Dependencies

Clone the repository:

```
git clone https://github.com/yourusername/multi-agent-research-assistant.git
```

Navigate to the project directory:

```
cd multi-agent-research-assistant
```

Install the required dependencies:

```
pip install -r requirements.txt
```

Make sure the following services are installed on your system:

* Redis
* Ollama
* PostgreSQL

---

# How to Run the Application

The project includes a batch script that automatically starts all required services.

Run the following file:

```
All_Run.bat
```

This script automatically starts:

1. Redis – used for caching
2. Ollama (phi3) – local LLM used for generating responses
3. MCP Server – tool server used by the agents
4. Django Backend – REST API handling requests
5. Streamlit UI – frontend interface

Multiple terminal windows will open and start each service.

Once all services are running, open the Streamlit interface:

```
http://localhost:8501
```

---

# Example Usage

Example user question:

```
population of India
```

System processing:

```
Planner Decision: SEARCH_DB
```

Example response:

```
India has a population of approximately 1.4 billion people.
```

The result is returned to the Streamlit interface and displayed to the user.

---

# Error Handling

The system includes basic error handling for tool failures.

If a tool cannot retrieve information, the system returns a safe message instead of crashing.

Example:

```
Tool error: Could not retrieve information
```

---

# Logging

Basic logging is used to track:

* user queries
* planner agent decisions
* research agent results
* tool execution errors

This helps debugging and monitoring the application.

---

# Database and Caching

PostgreSQL stores conversation data and system records.
Redis is used for caching to improve performance and reduce repeated computations.

---

# Summary

This project demonstrates a simple multi-agent architecture combining:

* LLM reasoning with Ollama
* agent orchestration with LangGraph
* tool communication using MCP
* backend APIs with Django
* interactive UI with Streamlit

to build an intelligent research assistant capable of answering user questions.
