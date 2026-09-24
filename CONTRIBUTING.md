# Contributing

This is currently a solo portfolio project, but changes follow a reviewable pull request workflow.

## Branches

- `main`: stable, presentable milestones. Direct commits are limited to repository initialization or exceptional maintenance.
- `develop`: integration branch for reviewed changes.
- `feature/<short-description>`: new capability, for example `feature/access-event-model`.
- `fix/<short-description>`: defect correction.
- `docs/<short-description>`: documentation-only work.

Create short-lived work branches from `develop`. Keep names lowercase and use hyphens between words. Remove a work branch after merge. Do not create idle branches for planned features.

## Commits and pull requests

Use focused conventional commits such as `feat: define access event model`, `test: cover denied badge scenarios`, or `docs: clarify event schema`. Keep the subject imperative and explain non-obvious decisions in the body.

Open a pull request from the work branch to `develop`. Link the issue, explain the reason and scope, record testing, and update documentation when behavior or design changes. Review the diff and checklist even for solo work. Squash merge a short feature branch after review to keep integration history readable; retain a merge commit when distinct commits carry useful context. Resolve conflicts and rerun relevant checks before merging.

For a completed milestone, open a pull request from `develop` to `main`. Check the milestone exit criteria, update the changelog, review the full diff, and merge with a merge commit so the release boundary is visible. Tag a version only after that merge. Do not publish a release for documentation-only setup or an incomplete feature.

## Testing and documentation

For code changes, add or update tests that cover behavior and important edge cases; include the exact commands and results in the pull request. For documentation-only changes, check links, spelling, and consistency with the current project status. There is no test runner or CI configured during Phase 0, so do not claim automated checks ran.

Use only fictional people, facilities, badge identifiers, and events. Do not commit secrets, local databases, logs, or real security-system details. Keep detection decisions deterministic and future AI analysis advisory, with human control over dispositions.
