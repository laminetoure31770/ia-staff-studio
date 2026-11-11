# IA STAFF Studio Architecture

The repository is a catalogue of independent open-source starters, not a production SaaS or an agent engine.

- `templates/distributions`: immutable starting presets, editable after scaffolding.
- `schemas`: machine-readable manifest contract.
- `cli`: copy-only CLI generators; no provisioning or deployment.
- `templates/web-nextjs`: independent minimal Next.js web starter.
- `workflows`: non-executable human-reviewed design examples.
- `tests`: scaffolding tests.
- `docs`: security and operational guidance.

Future commercial components should remain in a separate repository. Avoid storing secrets, credentials or nonredistributable source code. Agents must be authenticated, authorized, monitored and supervised before any production integration.
