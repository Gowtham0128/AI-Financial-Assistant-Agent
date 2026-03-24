# 🚀 AI Financial Assistant Agent

## 📌 Project Overview

This project is a **multi-functional AI Financial Assistant Agent** developed using **Google ADK** and **Gemini (gemini-2.0-flash)**.

It is designed to simulate a **real-world financial advisor system** by combining multiple intelligent roles like wealth strategist, portfolio manager, tax optimizer, and behavioral coach into a single AI agent.

---

## 🎯 Objective

To build an AI-powered system that can:

* Understand financial queries
* Automatically select the correct financial tool
* Provide intelligent, data-driven financial insights

---

## 🧠 Core Architecture

The system is built around a **central LLM Agent (`agent.py`)** which:

* Uses **Gemini AI model**
* Connects to **MCP Tool Server**
* Executes tool-based financial operations
* Supports real-time intelligent decision making

---

## ⚙️ Key Modules

### 🔹 1. Agent Module (`agent.py`)

* Initializes the AI agent
* Connects to MCP tool server (`http://localhost:8080/mcp/stream`)
* Integrates financial tools and Google Search
* Handles user queries and tool execution

---

### 🔹 2. Prompt Module (`prompt.py`)

* Contains predefined prompts
* Helps simulate real user queries
* Maps queries to specific tool functions

---

### 🔹 3. Multi-Agent Functional Roles

#### 💼 Wealth Strategist

* Net worth calculation
* Financial goal tracking
* Future projections

#### 📊 Portfolio Manager

* Investment holdings
* Transaction history
* Performance metrics (XIRR, CAGR)

#### 💰 Tax Optimizer

* Income source analysis
* Tax document processing
* Deduction identification

#### 🧾 Behavioral Coach

* Expense tracking
* Savings analysis
* Spending trends

#### 🎯 Smart Marketplace

* Credit profile analysis
* Product recommendations
* SIP suggestions

#### 🛡️ Anomaly Watchdog

* Fraud detection
* Duplicate transaction alerts

---

## 🔄 Workflow

1. User inputs a financial query
2. AI agent analyzes intent
3. Selects appropriate tool via MCP
4. Executes tool function
5. Returns structured response

---

## 🛠️ Technologies Used

* Python
* Google ADK (Agent Development Kit)
* Gemini AI (gemini-2.0-flash)
* MCP Toolset (Tool Integration Layer)
* dotenv (Environment Management)

---

## ▶️ Setup Instructions

```bash id="d0h5xp"
# Clone the repository
git clone https://github.com/your-username/AI-Financial-Assistant-Agent.git

# Navigate into project folder
cd AI-Financial-Assistant-Agent

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the agent
python agent.py
```

---

## 🔐 Environment Configuration

Create a `.env` file:

```id="m6k04q"
GOOGLE_API_KEY=your_api_key_here
```

---

## 🚫 Important Notes

* Do not upload `venv/` folder
* Keep API keys secure
* Ensure MCP server is running before execution

---

## 🔮 Future Enhancements

* Web-based UI dashboard
* Voice-enabled assistant
* Real-time financial API integration
* Automated investment execution
* Personalized AI financial planning

---

## 🎯 Real-World Applications

* Personal finance assistant
* Investment advisor bot
* Tax planning assistant
* Expense monitoring system
* AI fintech solutions

---

## 🧑‍💻 Author

Developed as an AI-based financial automation project using modern agent architecture.

---

## ⭐ Final Note

This project showcases how **AI agents + tool integration (MCP)** can be used to build scalable, intelligent financial systems similar to real fintech platforms.
