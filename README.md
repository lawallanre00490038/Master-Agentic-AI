# 🧠 Agentic AI Exercises

This repository contains three exercises that demonstrate the use of **LangChain agents and tools** to build autonomous systems. These exercises are part of a hands-on training module titled **"Creating with Agentic AI."**

---

## 📦 Project Structure

```
.
├── __pycache__/           # Python bytecode cache
├── filepath/              # Folder to store output files
├── venv/                  # Python virtual environment
├── .env                   # Environment variables (API keys, DB URI)
├── .gitignore             # Git ignore rules
├── exercise_1.py          # Weather tool agent example
├── exercise_2.py          # SQL database + file I/O agent example
├── exercise_3.py          # GitHub integration agent
├── model.py               # LLM setup using LangChain
├── prompt.py              # Custom prompts if any (not used currently)
├── README.md              # 📄 You are here!
└── requirements.txt       # Python dependencies
```

---

## 🧪 Exercises Overview

### ✅ Exercise 1 – Weather Agent

- Uses a tool (`get_weather`) to fetch current weather data using [wttr.in](https://wttr.in)
- **Agent Type**: `ZERO_SHOT_REACT_DESCRIPTION`
- **Example Query**:
  ```python
  "I want to know the weather in New York City"
  ```

---

### ✅ Exercise 2 – SQL + File Writing Agent

- Connects to a PostgreSQL database using the environment variable `POSTGRES_URL`.

**Tools Used**:
- `SQL Query Executor`: Executes SQL commands  
- `ReadFile`: Reads from a file in `filepath/`  
- `WriteQueryResultToFile`: Executes a query and saves the result to a file

**Example Query**:
```python
"How many users are there in the database and write it to a file"
```

---

### ✅ Exercise 3 – GitHub Agent

- Interacts with the GitHub API using your personal access token.

**Tools Used**:
- `GitHub Repository Search`
- `GitHub Repository Details`
- `GitHub Create Issue`
- `GitHub List Issues`

**Example Query**:
```python
"Get details about the repository 'langchain-ai/langchain' and list the issues it has"
```

---

## ⚙️ Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/your-username/agentic-ai-exercises.git
cd agentic-ai-exercises
```

### 2. Create a virtual environment and activate it

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory and add:

```env
POSTGRES_URL=your_postgres_connection_string
GITHUB_TOKEN=your_github_personal_access_token
```

---

## 🚀 Running the Exercises

```bash
# Run Exercise 1 – Weather Agent
python exercise_1.py

# Run Exercise 2 – SQL Agent + File Writer
python exercise_2.py

# Run Exercise 3 – GitHub API Agent
python exercise_3.py
```

---

## 🛠 LangChain Agent Configuration

All agents are initialized using the `initialize_agent` function from LangChain:

```python
initialize_agent(
    tools=...,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
```

- The **Language Model (`llm`)** is defined in `model.py`
- Tools are defined using `@tool` decorators or created with `Tool()`

---

## 📌 Notes

- Ensure you have internet access for external API calls (e.g., wttr.in, GitHub).
- The `filepath/` directory will be automatically created if it doesn't exist.
- Tool inputs must be either a single string or a dictionary depending on the tool.
- **Do not hardcode credentials** — use the `.env` file for all sensitive data.

---

## ✨ Credits

Built as part of the **LangChain x Agentic AI Engineering Training**.

Inspired by the power of **LLMs, APIs, and Tool-Using Agents**.
