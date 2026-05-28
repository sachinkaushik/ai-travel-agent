# AI Travel Planning System using LangGraph

A Real-World Multi-Agent AI System built using LangGraph with 4 AI agents that work together to plan a complete trip automatically.

## Features

- ✈️ Flight Search Agent
- 🏨 Hotel Search Agent
- 🗓️ Itinerary Planning Agent
- 🤖 Final Response Agent
- 🧠 Memory using PostgreSQL
- 🔀 Parallel Agent Execution (flight + hotel)
- 🌐 Real-time API Integration
- 💻 Streamlit Web Interface
- 🐳 Docker Containerized

---

## Tech Stack

- LangGraph
- LangChain
- Groq (Llama 3.3 70B)
- PostgreSQL
- Streamlit
- Tavily API
- AviationStack API
- Docker / Docker Compose

---

## Quick Start (Docker)

**1. Clone and configure:**

```bash
git clone https://github.com/sachinkaushik/ai-travel-agent.git
cd ai-travel-agent
cp .env.example .env
# Edit .env with your API keys
```

**2. Run with Docker Compose:**

```bash
docker compose up --build
```

The Streamlit UI will be available at **http://localhost:8501**

---

## Manual Setup

### Step 1: Create Python Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Install PostgreSQL

Download and install PostgreSQL: https://www.postgresql.org/download/

### Step 4: Create Database

```sql
CREATE DATABASE langgraph_memory;
```

### Step 5: Setup `.env` File

Create a `.env` file (see `.env.example`):

```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/langgraph_memory
```

### Step 6: Get API Keys

- **Groq:** https://console.groq.com
- **Tavily:** https://tavily.com
- **AviationStack:** https://aviationstack.com

### Step 7: Run the Application

**Terminal mode:**
```bash
python main.py
```

**Web UI:**
```bash
streamlit run frontend.py
```

---

## Example Prompt

> Plan a complete 7 days Japan trip including flights, hotels and sightseeing under 2 lakhs.

---

## Project Workflow

```
         ┌──────────────┐
         │    START      │
         └──┬────────┬───┘
            │        │
    ┌───────▼──┐  ┌──▼────────┐
    │ Flight   │  │  Hotel    │   ← parallel
    │ Agent    │  │  Agent    │
    └───────┬──┘  └──┬────────┘
            │        │
         ┌──▼────────▼───┐
         │  Itinerary     │
         │  Agent         │
         └───────┬────────┘
                 │
         ┌───────▼────────┐
         │  Final Agent   │
         └───────┬────────┘
                 │
         ┌───────▼────────┐
         │      END       │
         └────────────────┘
```

1. **Flight Agent** — searches flights (AviationStack API)
2. **Hotel Agent** — searches hotels (Tavily Search)
3. **Itinerary Agent** — creates travel plan using LLM
4. **Final Agent** — combines everything into a polished response
5. **PostgreSQL** — stores conversation memory across sessions

