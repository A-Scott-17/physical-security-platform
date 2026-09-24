# AI-Assisted Physical Security Management System

A planned, educational platform for simulating physical security operations and exploring how a security manager can review access activity, alerts, and incidents in one workflow.

**Status:** Phase 0, repository foundation. There is no runnable application, event simulator, API, database, dashboard, or AI integration yet. The source directories mark intended boundaries for later work.

## Problem and concept

Access-control systems produce badge and door events that can be difficult to review in context. This project will explore a manager-facing workflow that turns fictional simulated events into explainable alerts, supports investigation and case notes, and eventually drafts summaries for human review.

Planned event scenarios include granted and denied badge use, repeated denials, after-hours or restricted-area access, held or forced doors, and unusual badge-use patterns. The first development milestone is a deterministic access-event model and simulator; later milestones add persistence, detection, a dashboard, and incident handling.

## Decision boundaries

Deterministic event validation and detection rules will remain separate from any future AI analysis. AI may explain patterns, summarize related events, suggest questions, and draft reports. A security professional remains responsible for dismissing, monitoring, escalating, converting, resolving, or closing an alert or incident. AI output is advisory and must be reviewable.

## Planned technology

- Python backend, with FastAPI considered when an API is needed.
- SQLite for an initial local database, with PostgreSQL considered if scale or deployment needs justify it.
- HTML, CSS, and JavaScript for an initial frontend; React remains optional.
- Optional RFID or embedded hardware integration in a later phase.

These are plans, not installed dependencies or implemented services.

## Roadmap

The sequence runs from repository foundation through simulation, persistence, detection, dashboard, incident management, AI assistance, analytics, optional hardware, and advanced correlation. See [ROADMAP.md](ROADMAP.md) for deliverables and exit criteria. The proposed first milestone is a core simulated access-event model and generator (`v0.1.0` when complete). No releases are published yet.

## Repository layout

| Path | Intended purpose |
| --- | --- |
| `backend/api/` | Future API boundary |
| `backend/detection/` | Deterministic detection rules |
| `backend/simulator/` | Fictional access-event generation |
| `backend/database/` | Future persistence code |
| `backend/ai/` | Future advisory analysis |
| `frontend/assets/`, `frontend/components/` | Future user interface assets and components |
| `data/simulated_events/` | Fictional sample data when needed |
| `docs/architecture/`, `docs/design/`, `docs/screenshots/` | Architecture, decisions, and future captures |
| `tests/` | Future automated tests |
| `.github/` | Issue and pull request templates |

The empty source directories are intentional at this stage. [Architecture notes](docs/architecture/overview.md) describe the planned boundaries, and [the backlog](docs/backlog.md) links the first milestone issues.

## Development workflow

`main` is the stable, presentable branch. Work starts from `develop` on a short-lived `feature/`, `fix/`, or `docs/` branch, then enters `develop` through a pull request. A milestone is reviewed and merged from `develop` to `main`. See [CONTRIBUTING.md](CONTRIBUTING.md) for branch, commit, review, test, and release conventions.

## Skills demonstrated

As the project develops, it is intended to demonstrate security-event modeling, deterministic detection design, human-centered alert triage, incident workflows, testable backend design, documentation, and responsible use of advisory AI. The current repository demonstrates planning and version-control discipline only.

## Safety and scope

This is an educational security simulation, not a replacement for production access-control or life-safety systems. All eventual examples must use fictional people, facilities, badge identifiers, and events. The project focuses on defensive monitoring and analysis.

Licensed under the [MIT License](LICENSE).
