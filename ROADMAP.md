# Roadmap

Phases describe planned work, not features that currently exist. Each phase exits only when its deliverables are documented and verified. Scope can change through reviewed issues and pull requests.

## Phase 0 — Repository foundation (current)

**Objective:** Establish a maintainable project and review workflow.

**Major deliverables:** Git branches and conventions, starter layout, documentation, issue backlog, and GitHub templates.

**Exit criteria:** The repository has a clean `main`, a `develop` branch, a documented workflow, and no application functionality presented as complete.

## Phase 1 — Access-control simulator

**Objective:** Generate realistic but fictional access-control events.

**Major deliverables:** Event, employee/badge, door, and access-level models; deterministic scenario generator; unit tests and sample output.

**Exit criteria:** Documented schemas and repeatable tests demonstrate valid events and expected simulated scenarios without real employee or badge data. Candidate milestone: `v0.1.0` after review.

## Phase 2 — Security database

**Objective:** Persist and query simulated events locally.

**Major deliverables:** SQLite schema and migrations or equivalent versioned schema management, repository layer, and persistence tests.

**Exit criteria:** Simulated events can be saved and retrieved with documented constraints, and test data is isolated from local development data.

## Phase 3 — Detection engine

**Objective:** Turn event patterns into explainable alerts using deterministic rules.

**Major deliverables:** Rule specifications, evaluation logic, alert model, and tests for repeated denials, after-hours access, and selected door scenarios.

**Exit criteria:** Each alert records the triggering rule and supporting events; normal and edge cases pass tests. Candidate milestone: `v0.2.0`.

## Phase 4 — Security dashboard

**Objective:** Give a security manager a clear view of events and alerts.

**Major deliverables:** Basic dashboard, filterable event and alert views, and a documented local run path.

**Exit criteria:** A user can inspect simulated events and understand why alerts were raised. Candidate milestone: `v0.3.0`.

## Phase 5 — Incident management

**Objective:** Support human-led alert disposition and case work.

**Major deliverables:** Dismiss, monitor, escalate, and incident-conversion actions; incident notes, status history, and resolution workflow.

**Exit criteria:** Decisions are attributable to a human action and case history remains understandable. Candidate milestone: `v0.4.0`.

## Phase 6 — AI-assisted analysis

**Objective:** Add optional analyst assistance without transferring decision authority.

**Major deliverables:** Event summaries, draft incident reports, investigation prompts, and clear review controls.

**Exit criteria:** AI output is labeled as advisory, traceable to source events, and never changes alert or incident status without a human decision. Candidate milestone: `v0.5.0`.

## Phase 7 — Security analytics

**Objective:** Explore trends in fictional security activity.

**Major deliverables:** Useful counts, trend views, filters, and documented metric definitions.

**Exit criteria:** Metrics can be reproduced from the same simulated dataset and interpreted without overstating risk.

## Phase 8 — Optional hardware integration

**Objective:** Evaluate a safe lab interface to RFID or embedded devices if it adds portfolio value.

**Major deliverables:** Isolated lab adapter, fictional device data, and a documented boundary from real facilities.

**Exit criteria:** The simulation remains usable without hardware and no real access-control equipment is controlled.

## Phase 9 — Advanced event correlation

**Objective:** Relate events across doors, time windows, and other future simulated sources.

**Major deliverables:** Correlation specifications, test scenarios, and explainable linked-event views.

**Exit criteria:** Correlations show supporting evidence, known limits, and false-positive behavior in tests.

## Versioning

Use [Semantic Versioning](https://semver.org/) for meaningful tagged milestones. Before `v1.0.0`, minor versions mark substantial reviewed capability milestones and patch versions mark corrections to a released milestone. `v1.0.0` is reserved for a stable, documented portfolio release with a coherent end-to-end workflow. The candidate versions above are targets, not promises or published releases. Update [CHANGELOG.md](CHANGELOG.md) when a release is prepared.
