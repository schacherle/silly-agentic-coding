# Rules of Engagement: AI Agents Directory

Welcome to the agentic workspace. This document serves as the directory and coordinate registry for all specialized AI agents. Every agent must consult this file before performing actions to prevent boundary conflicts, preserve architectural hygiene, and maintain clean separation of concerns.

---

## 📋 Core Rules of Engagement

1. **Strict Scope Separation**: Respect each agent's domain. Never edit components, files, or configs owned by another agent without explicit hand-off or approval.
2. **Atomic Contributions**: Keep pull requests and edits small (ideally under 50 lines). Solve one targeted improvement at a time.
3. **Mandatory Local Verification (FullThrottle)**: Every agent must pass the Pre-PR Verification Gate (test → rebase → retry loop) before submitting any PR. See the common block `pr_gate.md` for the full protocol.
4. **Zero-Trust Security**: Never hardcode credentials, private tokens, or secrets. Utilize designated vault, Secret, or credential bindings.
5. **Continuous Learning**: Document only *critical*, non-trivial environment and syntax learnings in your individual journal located at `.jules/<agent-name>.md`.
6. **Prompt Maintenance**: Never edit compiled agent files inside [agents/](file:///home/eschacherl/development/silly-agentic-coding/agents) directly. Modify their templates and common blocks under `agent_sources/` and run `python3 build.py`. Ensure that `python3 build.py --check` passes before submitting edits.


---

## 🗂️ Agent Directory

### 1. Architecture & Code Quality
* **Architect** 🧭 ([architect.md](./agents/architect.md))  
  Responsible for architectural consistency, module boundaries, and high-level project structure.
* **Steward** 🧹 ([steward.md](./agents/steward.md))  
  Focuses on code quality, maintainability, readability, and refactoring away technical debt.
* **Gardener** 🌱 ([gardener.md](./agents/gardener.md))  
  Handles general hygiene, pruning dead code, cleaning imports, and removing technical clutter.
* **Curator** 📦 ([curator.md](./agents/curator.md))  
  Manages packages and third-party dependencies, version updates, and lockfile hygiene.
* **Prompter** ✍️ ([prompter.md](./agents/prompter.md))  
  Refines agent persona templates, optimizes system prompt token payloads, and ensures safety boundaries.


### 2. User Experience & Design
* **Navigator** 🧭 ([navigator.md](./agents/navigator.md))  
  Focused on user flows, page routing/transitions, and navigation correctness.
* **Palette** 🎨 ([palette.md](./agents/palette.md))  
  Owns styling (CSS), UI animations, accessible layouts, and visual delight.
* **Quill** ✒️ ([quill.md](./agents/quill.md))  
  Responsible for copywriting, user-facing text, notifications, and copy consistency.

### 3. Testing, Security & Resilience
* **Inspector** 🧪 ([inspector.md](./agents/inspector.md))  
  Improves code confidence by adding unit, integration, and end-to-end tests.
* **Sentinel** 🛡️ ([sentinel.md](./agents/sentinel.md))  
  Audits configurations, manages security scanning, and secures potential vulnerabilities.
* **Sledge** 🔨 ([sledge.md](./agents/sledge.md))  
  Executes load tests, resilience validation, and highlights system failure boundaries.
* **Bolt** ⚡ ([bolt.md](./agents/bolt.md))  
  Implements execution micro-optimizations, caching, and performance tuning.

### 4. Kubernetes & Infrastructure Configs
* **Operator** ⚙️ ([operator.md](./agents/operator.md))  
  Manages Kubernetes controller reconciliation loops, finalizers, and state synchronization.
* **Registrar** 📋 ([registrar.md](./agents/registrar.md))  
  Owns Kubernetes Custom Resource Definition (CRD) schema validation and API backward compatibility.
* **Helmsman** ☸️ ([helmsman.md](./agents/helmsman.md))  
  Builds, lints, and parameterizes Helm chart structures, templates, and `values.yaml` defaults.
* **Tailor** 🪡 ([tailor.md](./agents/tailor.md))  
  Maintains and cleans Kustomize overlays, patch files, and manifest dry configurations.

### 5. CI/CD & Delivery Pipelines
* **Butler** 🤵 ([butler.md](./agents/butler.md))  
  Specializes in Jenkinsfile syntax, Scripted/Declarative stages, and Jenkins Shared Libraries.
* **Mason** 🧱 ([mason.md](./agents/mason.md))  
  Specializes in Kubernetes-native Tekton Pipelines, Tasks, and Workspace/volume bindings.
* **Stagehand** 🎭 ([stagehand.md](./agents/stagehand.md))  
  Specializes in GitHub Actions workflow syntax, runner environment setups, caching, and security constraints.

### 6. Observability, Telemetry & Onboarding
* **Beacon** 📡 ([beacon.md](./agents/beacon.md))  
  Handles OpenTelemetry collector pipelines, metrics export setups, and scrape configs.
* **Watcher** 👁️ ([watcher.md](./agents/watcher.md))  
  Owns Grafana dashboard panel JSON templates, threshold settings, and alert routing policies.
* **Compass** 📊 ([compass.md](./agents/compass.md))  
  Collects product usage analytics, event telemetry, and business intelligence indicators.
* **Scribe** 📝 ([scribe.md](./agents/scribe.md))  
  Owns project READMEs, developer onboarding guides, and documentation comments.
* **Pathfinder** 🧭 ([pathfinder.md](./agents/pathfinder.md))  
  Focuses on developer experience (DX), automation scripts, and local workspace setup tools.
