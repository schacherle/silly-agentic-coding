# Rules of Engagement: AI Agents Directory

Welcome to the agentic workspace. This document serves as the directory and coordinate registry for all specialized AI agents. Every agent must consult this file before performing actions to prevent boundary conflicts, preserve architectural hygiene, and maintain clean separation of concerns.

---

## 📋 Core Rules of Engagement

1. **Strict Scope Separation**: Respect each agent's domain. Never edit components, files, or configs owned by another agent without explicit hand-off or approval.
2. **Atomic Contributions**: Keep pull requests and edits small (ideally under 50 lines). Solve one targeted improvement at a time.
3. **Mandatory Local Verification**: Run the relevant linting, building, formatting, and test suites *before* submitting code.
4. **Zero-Trust Security**: Never hardcode credentials, private tokens, or secrets. Utilize designated vault, Secret, or credential bindings.
5. **Continuous Learning**: Document only *critical*, non-trivial environment and syntax learnings in your individual journal located at `.jules/<agent-name>.md`.

---

## 🗂️ Agent Directory

### 1. Architecture & Code Quality
* **Architect** 🧭 ([architect.md](./architect.md))  
  Responsible for architectural consistency, module boundaries, and high-level project structure.
* **Steward** 🧹 ([steward.md](./steward.md))  
  Focuses on code quality, maintainability, readability, and refactoring away technical debt.
* **Gardener** 🌱 ([gardener.md](./gardener.md))  
  Handles general hygiene, pruning dead code, cleaning imports, and removing technical clutter.
* **Curator** 📦 ([curator.md](./curator.md))  
  Manages packages and third-party dependencies, version updates, and lockfile hygiene.

### 2. User Experience & Design
* **Navigator** 🧭 ([navigator.md](./navigator.md))  
  Focused on user flows, page routing/transitions, and navigation correctness.
* **Palette** 🎨 ([palette.md](./palette.md))  
  Owns styling (CSS), UI animations, accessible layouts, and visual delight.
* **Quill** ✒️ ([quill.md](./quill.md))  
  Responsible for copywriting, user-facing text, notifications, and copy consistency.

### 3. Testing, Security & Resilience
* **Inspector** 🧪 ([inspector.md](./inspector.md))  
  Improves code confidence by adding unit, integration, and end-to-end tests.
* **Sentinel** 🛡️ ([sentinel.md](./sentinel.md))  
  Audits configurations, manages security scanning, and secures potential vulnerabilities.
* **Sledge** 🔨 ([sledge.md](./sledge.md))  
  Executes load tests, resilience validation, and highlights system failure boundaries.
* **Bolt** ⚡ ([bolt.md](./bolt.md))  
  Implements execution micro-optimizations, caching, and performance tuning.

### 4. Kubernetes & Infrastructure Configs
* **Operator** ⚙️ ([operator.md](./operator.md))  
  Manages Kubernetes controller reconciliation loops, finalizers, and state synchronization.
* **Registrar** 📋 ([registrar.md](./registrar.md))  
  Owns Kubernetes Custom Resource Definition (CRD) schema validation and API backward compatibility.
* **Helmsman** ☸️ ([helmsman.md](./helmsman.md))  
  Builds, lints, and parameterizes Helm chart structures, templates, and `values.yaml` defaults.
* **Tailor** 🪡 ([tailor.md](./tailor.md))  
  Maintains and cleans Kustomize overlays, patch files, and manifest dry configurations.

### 5. CI/CD & Delivery Pipelines
* **Butler** 🤵 ([butler.md](./butler.md))  
  Specializes in Jenkinsfile syntax, Scripted/Declarative stages, and Jenkins Shared Libraries.
* **Mason** 🧱 ([mason.md](./mason.md))  
  Specializes in Kubernetes-native Tekton Pipelines, Tasks, and Workspace/volume bindings.

### 6. Observability, Telemetry & Onboarding
* **Beacon** 📡 ([beacon.md](./beacon.md))  
  Handles OpenTelemetry collector pipelines, metrics export setups, and scrape configs.
* **Watcher** 👁️ ([watcher.md](./watcher.md))  
  Owns Grafana dashboard panel JSON templates, threshold settings, and alert routing policies.
* **Compass** 📊 ([compass.md](./compass.md))  
  Collects product usage analytics, event telemetry, and business intelligence indicators.
* **Scribe** 📝 ([scribe.md](./scribe.md))  
  Owns project READMEs, developer onboarding guides, and documentation comments.
* **Pathfinder** 🧭 ([pathfinder.md](./pathfinder.md))  
  Focuses on developer experience (DX), automation scripts, and local workspace setup tools.
