<div align="center">

# 🌌 ResearchGuru
### AI Powered Multi-Agent Research Assistant

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/LangChain-Agent%20Framework-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit"/>
<img src="https://img.shields.io/badge/HuggingFace-LLM-yellow?style=for-the-badge&logo=huggingface"/>

A professional **Multi-Agent AI Research System** that autonomously searches the web, extracts information, writes structured research reports, and evaluates its own output using specialized AI agents.

---

</div>

## 📖 Overview

ResearchGuru is an AI-powered research assistant built using **LangChain's Agent Framework**.

Instead of relying on a single LLM, ResearchGuru divides the research workflow into multiple specialized AI agents, each responsible for one task.

The result is a structured and reliable research pipeline capable of generating detailed reports with self-evaluation.

---

# ✨ Features

✅ Multi-Agent Architecture

✅ Autonomous Web Search

✅ Website Scraping

✅ AI Generated Research Reports

✅ Self Critique & Quality Evaluation

✅ Modern Streamlit Dashboard

✅ Markdown Report Export

✅ Modular & Scalable Design

---

# 🏗️ Architecture

```
                User Query
                     │
                     ▼
            🔍 Search Agent
                     │
                     ▼
            📄 Reader Agent
                     │
                     ▼
            ✍️ Writer Agent
                     │
                     ▼
            🧐 Critic Agent
                     │
                     ▼
            Final Research Report
```

---

# 🤖 Agent Workflow

## 1️⃣ Search Agent

Uses DuckDuckGo Search to collect relevant and recent information from the internet.

**Responsibilities**

- Search latest information
- Find reliable sources
- Return search summaries

---

## 2️⃣ Reader Agent

Chooses the best source and scrapes detailed information using BeautifulSoup.

**Responsibilities**

- Extract webpage content
- Remove unnecessary HTML
- Clean textual information

---

## 3️⃣ Writer Agent

Uses the gathered research to generate a professional report.

The generated report includes:

- Introduction
- Key Findings
- Detailed Explanation
- Conclusion
- Sources

---

## 4️⃣ Critic Agent

Acts as an AI reviewer.

It evaluates:

- Report quality
- Completeness
- Missing information
- Final Score
- Suggestions for improvement

---

# 🖥️ User Interface

The project includes a modern Streamlit interface featuring

- Beautiful Dark Theme
- Animated Agent Pipeline
- Real-time Progress
- Download Report Button
- Research History View
- Raw Search Logs
- Critic Feedback Panel

---

# 📂 Project Structure

```bash
ResearchGuru/
│
├── agent.py             # Agent creation
├── tools.py             # Search & Scraping tools
├── pipeline.py          # CLI Pipeline
├── app.py               # Streamlit UI
│
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| LangChain | Agent Framework |
| HuggingFace | Large Language Model |
| Streamlit | Frontend |
| BeautifulSoup | Web Scraping |
| DuckDuckGo Search | Search Engine |
| dotenv | Environment Variables |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ResearchGuru.git

cd ResearchGuru
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
HUGGINGFACE_API_KEY=your_api_key
```

---

# ▶️ Run the Application

### Streamlit UI

```bash
streamlit run app.py
```

### Command Line Version

```bash
python pipeline.py
```

---

# 📸 Screenshots

Add screenshots here.

```
assets/home.png

assets/pipeline.png

assets/report.png
```

---

# 📥 Example Output

```
Topic:
Future of Quantum Computing

↓

Search Agent
↓

Reader Agent

↓

Writer Agent

↓

Generated Report

↓

Critic Feedback

↓

Score: 9.2 / 10
```

---

# 🔥 Future Improvements

- PDF Report Export

- Citation Generation

- Multi-source Verification

- Memory Enabled Agents

- Local LLM Support

- RAG Integration

- Parallel Agent Execution

- Vector Database

- Source Ranking

- Multi-language Reports

- Research History Database

---

# 🧠 Concepts Demonstrated

- Multi-Agent Systems

- Agent Orchestration

- Prompt Engineering

- Web Search

- Web Scraping

- LLM Chains

- AI Evaluation

- Report Generation

- Streamlit Development

- Modular Software Design

---

# 📈 Why this Project?

Unlike traditional chatbots, ResearchGuru follows a collaborative AI architecture where multiple specialized agents solve different parts of the research process.

This makes the system more modular, scalable, and closer to real-world AI agent workflows used in modern enterprise applications.

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

3. Commit your changes

4. Push to your branch

5. Open a Pull Request

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork it

📢 Share it with others

---

<div align="center">

Made with ❤️ using Python, LangChain and Streamlit

</div>