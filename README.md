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

1. **Architecture & Code Quality**: [Architect](./architect.md), [Steward](./steward.md), [Gardener](./gardener.md), [Curator](./curator.md)
2. **User Experience & Design**: [Navigator](./navigator.md), [Palette](./palette.md), [Quill](./quill.md)
3. **Testing, Security & Resilience**: [Inspector](./inspector.md), [Sentinel](./sentinel.md), [Sledge](./sledge.md), [Bolt](./bolt.md)
4. **Kubernetes & Infrastructure Configs**: [Operator](./operator.md), [Registrar](./registrar.md), [Helmsman](./helmsman.md), [Tailor](./tailor.md)
5. **CI/CD & Delivery Pipelines**: [Butler](./butler.md), [Mason](./mason.md)
6. **Observability, Telemetry & Onboarding**: [Beacon](./beacon.md), [Watcher](./watcher.md), [Compass](./compass.md), [Scribe](./scribe.md), [Pathfinder](./pathfinder.md)

---

## 📋 Rules of Engagement

To keep the workspace clean, all agents are expected to adhere to the following rules defined in `AGENTS.md`:
1. **Strict Scope Separation**: Respect each agent's domain. Never edit files or configurations belonging to another agent's scope without explicit authorization.
2. **Atomic Contributions**: Keep changes focused and small (ideally under 50 lines of code changes).
3. **Mandatory Local Verification**: Run formatting, linting, building, and tests locally before proposing changes.
4. **Zero-Trust Security**: Never commit raw secrets or credentials. Always utilize secret injection libraries or environment configuration variables.
5. **Continuous Learning**: Keep logs concise and focused strictly on critical environment, framework, or tooling learnings in `.jules/<agent-name>.md`.

---

## 🛠️ Usage

When invoking an agent, mount its prompt markdown file (e.g., [steward.md](./steward.md)) as a system prompt instruction. This instructs the LLM on its exact bounds and the verification steps it must perform before completing its tasks.
