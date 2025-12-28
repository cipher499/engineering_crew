# Multi-Agent Portfolio Management & Trading System (CrewAI PoC)

I built this project following Ed Donner's course on Agentic AI to learn and experiment with the **CrewAI framework** by implementing a simple **portfolio management and trading system** using multiple collaborating agents.

The focus is on **agent orchestration**, role separation, and iterative development — not on building a production-grade trading platform.

---

## 🎯 Project Overview

The system is built using specialized agents that collaborate to:
- design the system
- implement backend trading logic
- build a simple frontend UI
- write unit tests

Each responsibility is handled by a dedicated agent and coordinated via CrewAI.

---

## 🧠 Agents & Tasks Configuration

Agent roles and task definitions are declared in YAML:

- **Agents config**  
  [`src/code_crew/config/agents.yaml`](src/code_crew/config/agents.yaml)

- **Tasks config**  
  [`src/code_crew/config/tasks.yaml`](src/code_crew/config/tasks.yaml)

---

## ⚙️ Core Orchestration Code

- **Crew definition**  
  [`src/code_crew/crew.py`](src/code_crew/crew.py)

- **Main entry point**  
  [`src/code_crew/main.py`](src/code_crew/main.py)

---

## 📦 Agent Outputs

All generated artifacts are written to the `output/` folder:

[`output/`](output/)

- `accounts.py` — backend trading & portfolio logic (backend agent)
- `accounts.py_design.md` — code design from team lead agent
- `app.py` — Gradio UI built by frontend agent
- `test_accounts.py` — unit tests written by testing agent

---

## ▶️ Running the Project

Run the full crew end-to-end:

```bash
uv run crewai run
