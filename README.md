# Silly Agentic Coding 🤖

A repository dedicated to defining, organizing, and coordinating specialized AI agents. This workspace serves as a template directory and coordinate registry for agentic coding workflows, establishing standard personas, boundaries, and rules of engagement to preserve code quality and prevent operational conflicts.

## 🚀 Concept

In modern AI-assisted software engineering, having a single model manage all concerns can lead to context pollution, scope creep, and conflicting edits. This repository implements a **multi-agent orchestration framework** by dividing development concerns into narrow, highly specialized roles (e.g., performance tuning, testing, security, Kubernetes configuration, and pipeline management).

Each agent is governed by:
- A specific persona and target mission.
- Core boundaries (things they must **always do**, **ask first**, or **never do**).
- A daily execution process.
- An individual journal (`.jules/<agent-name>.md`) for recording critical environment or syntax discoveries.

---

## 🗂️ Agent Categories

All agents are documented in the [AI Agents Directory (AGENTS.md)](./AGENTS.md). Here is the category breakdown:

1. **Architecture & Code Quality**: [Architect](./agents/architect.md), [Steward](./agents/steward.md), [Gardener](./agents/gardener.md), [Curator](./agents/curator.md)
2. **User Experience & Design**: [Navigator](./agents/navigator.md), [Palette](./agents/palette.md), [Quill](./agents/quill.md)
3. **Testing, Security & Resilience**: [Inspector](./agents/inspector.md), [Sentinel](./agents/sentinel.md), [Sledge](./agents/sledge.md), [Bolt](./agents/bolt.md)
4. **Kubernetes & Infrastructure Configs**: [Operator](./agents/operator.md), [Registrar](./agents/registrar.md), [Helmsman](./agents/helmsman.md), [Tailor](./agents/tailor.md)
5. **CI/CD & Delivery Pipelines**: [Butler](./agents/butler.md), [Mason](./agents/mason.md), [Stagehand](./agents/stagehand.md)
6. **Observability, Telemetry & Onboarding**: [Beacon](./agents/beacon.md), [Watcher](./agents/watcher.md), [Compass](./agents/compass.md), [Scribe](./agents/scribe.md), [Pathfinder](./agents/pathfinder.md)

---

## 📋 Rules of Engagement

To keep the workspace clean, all agents are expected to adhere to the following rules defined in `AGENTS.md`:
1. **Strict Scope Separation**: Respect each agent's domain. Never edit files or configurations belonging to another agent's scope without explicit authorization.
2. **Atomic Contributions**: Keep changes focused and small (ideally under 50 lines of code changes).
3. **Mandatory Local Verification**: Run formatting, linting, building, and tests locally before proposing changes.
4. **Zero-Trust Security**: Never commit raw secrets or credentials. Always utilize secret injection libraries or environment configuration variables.
5. **Continuous Learning**: Keep logs concise and focused strictly on critical environment, framework, or tooling learnings in `.jules/<agent-name>.md`.

---

## 🛠️ Development & Building Prompts

This project uses a modular prompt architecture. Agent prompts are constructed from reusable components under `agent_sources/common/` and agent-specific templates under `agent_sources/templates/`. 

To compile the monolithic output agent files inside [agents/](file:///home/eschacherl/development/silly-agentic-coding/agents):
```bash
python3 build.py
```

To verify that the compiled agent files are up-to-date with their sources (e.g., in CI/CD or pre-commit hooks):
```bash
python3 build.py --check
```

> [!WARNING]
> Never edit the files inside the [agents/](file:///home/eschacherl/development/silly-agentic-coding/agents) directory directly. They are auto-generated and will be overwritten by `build.py`. Make all modifications under `agent_sources/` instead.

## 🚀 Usage

When invoking an agent, mount its compiled monolithic prompt markdown file (e.g., [steward.md](file:///home/eschacherl/development/silly-agentic-coding/agents/steward.md)) as a system prompt instruction. This instructs the LLM on its exact bounds and the verification steps it must perform before completing its tasks.

