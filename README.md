# 🧠 Agentic AI Exercises

This repository contains three exercises that demonstrate the use of **LangChain agents and tools** to build autonomous systems. The exercises are part of a hands-on training module titled **"Creating with Agentic AI"**.

## 📦 Project Structure

.
├── _pycache/      # Python bytecode cache
├── filepath/      # Folder to store output files
├── venv/          # Python virtual environment
├── .env           # Environment variables (API keys, DB URI)
├── .gitignore     # Git ignore rules
├── exercise_1.py  # Weather tool agent example
├── exercise_2.py  # SQL database + file I/O agent example
├── exercise_3.py  # GitHub integration agent
├── model.py       # LLM setup using LangChain
├── prompt.py      # Custom prompts if any (not used currently)
├── README.md      # 📄 You are here!
└── requirements.txt # Python dependencies


## 🧪 Exercises Overview

### ✅ Exercise 1 - Weather Agent

- Uses a tool (`get_weather`) to fetch current weather for any city using [wttr.in](https://wttr.in).
- Agent Type: `ZERO_SHOT_REACT_DESCRIPTION`
- Example query:
  ```python
  "I want to know the weather in New York City"
✅ Exercise 2 - SQL + File Writing Agent
Connects to a PostgreSQL database using the environment variable POSTGRES_URL.

Tools:

SQL Query Executor: Executes SQL commands
ReadFile: Reads from a file in filepath/
WriteQueryResultToFile: Executes a query and saves the result to a file
Example query:

Python

"How many users are there in the database and write it to a file"
✅ Exercise 3 - GitHub Agent
Interacts with the GitHub API using your GitHub token.

Tools:

GitHub Repository Search
GitHub Repository Details
GitHub Create Issue
GitHub List Issues
Example query:

Python

"Get details about the repository 'langchain-ai/langchain' and list the issues it has"
⚙️ Setup Instructions
Clone this repository:

Bash

git clone [https://github.com/your-username/agentic-ai-exercises.git](https://github.com/your-username/agentic-ai-exercises.git)
cd agentic-ai-exercises
Create a virtual environment and activate it:

Bash

python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies:

Bash

pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory and add your PostgreSQL connection string and GitHub personal access token:

Code snippet

POSTGRES_URL=your_postgres_connection_string
GITHUB_TOKEN=your_github_personal_access_token
🚀 Running the Exercises
Bash

# Run Exercise 1 - Weather Agent
python exercise_1.py

# Run Exercise 2 - SQL Agent + File Writer
python exercise_2.py

# Run Exercise 3 - GitHub API Agent
python exercise_3.py
🛠 LangChain Agent Configuration
All agents are initialized using the initialize_agent function from LangChain with the following configurations:

Python

initialize_agent(
    tools=...,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
The Language Model (llm) used is defined in model.py.
Tools are custom functions annotated with @tool or created using Tool().
📌 Notes
Ensure you have internet access for API requests (wttr.in, GitHub).
The filepath/ directory will be automatically created if it doesn't exist.
Tool inputs must be a single string or a dictionary based on the tool's definition.
Do not hardcode credentials; always use the .env file for sensitive information.
✨ Credits
Built as part of LangChain x Agentic AI Engineering Training.

Inspired by the power of LLMs, APIs, and Tool-using Agents.
