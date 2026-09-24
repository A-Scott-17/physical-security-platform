# Phase 1 issue backlog

These GitHub issues track planned work; none of the features are implemented yet. All examples and fixtures must be fictional.

## 1. [Define access-event data model](https://github.com/A-Scott-17/physical-security-platform/issues/1)

**Goal:** Specify event identifiers, timestamps, event types, badge and door references, outcome, and validation rules.

**Acceptance criteria:** A documented schema distinguishes granted, denied, held-open, and forced-door events; timestamps and identifiers have clear formats; tests cover valid and invalid examples.

**Dependency:** None. This is the next recommended issue.

## 2. [Define employee and badge model](https://github.com/A-Scott-17/physical-security-platform/issues/2)

**Goal:** Represent fictional employees, badges, and badge status without real personal data.

**Acceptance criteria:** Fields and relationships are documented; inactive and unknown badges have explicit behavior; tests use fictional fixtures.

**Dependency:** Align identifiers with issue 1.

## 3. [Define door and access-level model](https://github.com/A-Scott-17/physical-security-platform/issues/3)

**Goal:** Represent fictional doors, areas, and access permissions.

**Acceptance criteria:** Door and area identifiers are defined; restricted access has an explicit rule; tests cover allowed and denied access.

**Dependency:** Align identifiers with issue 1.

## 4. [Add unit-test foundation](https://github.com/A-Scott-17/physical-security-platform/issues/4)

**Goal:** Choose a minimal Python test runner and fixture conventions once the first model is added.

**Acceptance criteria:** A documented local test command runs model tests; fictional fixtures are reusable; no external service is required.

**Dependency:** Coordinate with issue 1.

## 5. [Build repeatable event generator](https://github.com/A-Scott-17/physical-security-platform/issues/5)

**Goal:** Generate fictional event sequences for the documented scenarios.

**Acceptance criteria:** The same seed produces the same sequence; generated events validate against the schema; sample scenarios include granted, denied, and door events.

**Dependency:** Issues 1–4.

## 6. [Specify initial detection rules](https://github.com/A-Scott-17/physical-security-platform/issues/6)

**Goal:** Document future thresholds and evidence requirements for repeated denials, after-hours access, and door anomalies.

**Acceptance criteria:** Each rule names inputs, trigger conditions, alert evidence, and likely false positives; no alerting engine is implemented in this issue.

**Dependency:** Issue 1; implementation belongs to Phase 3.
