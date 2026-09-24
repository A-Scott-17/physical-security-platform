# Planned architecture

This document records intended boundaries, not an implemented design.

1. A **simulator** will produce fictional badge and door events from explicit scenarios.
2. A **data layer** will validate, store, and query those events.
3. A **deterministic detection layer** will evaluate documented rules and attach supporting evidence to alerts.
4. An **API and user interface** will present events, alerts, and incidents for human review.
5. An optional **AI advisory layer** may summarize evidence or draft text, but will not make or apply security decisions.

Alert disposition and incident status changes belong to the manager-facing workflow. A future implementation should record the actor, time, decision, and rationale where appropriate. Event and alert schemas must be settled before persistence or interface code is added.

The initial system should run locally on fictional data. Integrations with physical devices or other security systems remain optional, separately scoped work.
