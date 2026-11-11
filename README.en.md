# IA STAFF Studio

**Human-led. AI-powered. Accountable by design.**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Templates](https://img.shields.io/badge/distributions-7-43a978.svg)](templates/distributions/)
[![Framework](https://img.shields.io/badge/starter-Next.js-black.svg)](templates/web-nextjs/)

**IA STAFF Studio** is the public, open-source foundation for building configurable AI applications and supervised agentic workflows. It brings together application starters, reusable workflow specifications, CLI scaffolding tools, documentation, and quality checks in one repository.

The project is guided by a straightforward principle: **humans direct; intelligences collaborate**. AI is treated as part of an information system, with explicit identity, authentication, authorization, observability, resource limits, and human accountability.

This repository is intended for individual practitioners, educators, nonprofits, small teams, developers, and organizations evaluating responsible AI. It favors reusable building blocks and transparent boundaries over opaque "one prompt solves everything" claims.

> **Maturity disclosure:** This repository currently contains a working *scaffolding foundation*, a minimal Next.js starter and declarative model/workflow examples. It is **not** a ready-to-run multi-agent platform, general artificial intelligence (AGI), or a production-grade enterprise suite. Advanced capabilities are configuration targets unless explicitly implemented and tested.

## Table of contents

1. [Why IA STAFF](#why-ia-staff)
2. [Distribution catalog](#distribution-catalog)
3. [Architecture](#architecture)
4. [Getting started](#getting-started)
5. [Using the command-line interfaces](#using-the-command-line-interfaces)
6. [Deploying to Vercel](#deploying-to-vercel)
7. [Workflow examples](#workflow-examples)
8. [Security and governance](#security-and-governance)
9. [Efficiency and sustainability](#efficiency-and-sustainability)
10. [Development status and roadmap](#development-status-and-roadmap)
11. [Contributing](#contributing)
12. [License](#license)

## Why IA STAFF

IA STAFF helps teams design applications that combine people, language models, data, and tools while keeping control of what agents may do.

Our goals are to:

- **Improve accessibility:** start with a small, low-resource Persona before adding infrastructure.
- **Keep humans in charge:** require human validation before externally consequential actions.
- **Make systems inspectable:** expose workflow structure, policies and limits.
- **Control cost and consumption:** define token budgets and context limits, then measure real use when providers are connected.
- **Favor portability:** separate provider-specific implementations from reusable specifications.
- **Protect organizations and users:** keep secrets server-side and enforce authorization before actions.
- **Enable progressive adoption:** evolve from a minimal assistant to multi-agent, RAG and organizational configurations only when justified.

## Distribution catalog

Seven starter distributions share a common manifest format.

| Model | Intended audience | Configuration focus | Current availability |
|---|---|---|---|
| **Persona** | Individuals, educators, small projects | Single assistant, limited context, small token target | Manifest + starter |
| **Agent** | Developers prototyping automation | One supervised domain-specific agent and audited tools | Manifest + workflow specification |
| **Blog + Assistant** | Publishers and associations | Assisted drafting, moderation and human editorial approval | Manifest + workflow specification |
| **AI STAFF Light** | Small teams | Assistant, basic roles and audit requirements | Manifest |
| **AI STAFF Medium** | Teams integrating knowledge and tools | Two agents, retrieval and controlled MCP integrations | Manifest |
| **AI STAFF Pro** | Complex orchestrations | Multi-agent design, GraphRAG, ABAC and FinOps | Architecture manifest |
| **AI STAFF Enterprise** | Multi-team organizations | Multi-tenancy, IAM/SSO, advanced audit and continuity planning | Architecture manifest |

**Important:** The words “Pro” and “Enterprise” here identify *design profiles*, not commercial subscriptions or certified enterprise implementations. Professional proprietary components, if developed, will belong in a separate repository rather than be silently mixed into MIT-licensed code.

### What a manifest contains

Each distribution JSON file defines the profile name and description, expected storage architecture, number of agents and assistants, a *target* monthly token budget, maximum context target, selected modules and feature flags, and mandatory human approval.

Feature flags are descriptive. Setting `rag: true`, `mcp: true`, `graph: true` or `multitenant: true` **does not create a database, connect a provider, or turn on those capabilities**. Real implementation and server-side enforcement are separate engineering tasks.

## Architecture

```text
ia-staff-studio/
├── catalog/                         Machine-readable model index
├── templates/
│   ├── distributions/               7 versioned JSON model manifests
│   └── web-nextjs/                  Minimal independent Next.js starter
├── cli/
│   ├── python/                      Zero-runtime-dependency Python CLI
│   └── typescript/                  Node.js / TypeScript CLI
├── workflows/                       Declarative human-reviewed examples
├── schemas/                         JSON distribution contract
├── tests/                           Automated scaffold checks
├── docs/                            Architecture, safety and deployment
└── .github/workflows/               GitHub Actions CI
```

The starter uses Next.js with React and does not require an LLM provider, Neon, or a token to render its initial page. Its health endpoint is `/api/health`.

The CLI copies the starter into a new folder and attaches `distribution.json`. It does not provision resources, push Git commits, purchase services or automatically deploy to Vercel.

## Getting started

Requirements: Python 3.10+ for the Python CLI, or a compatible Node.js/npm installation for the TypeScript CLI and Next.js starter. Follow the versions required by the package manifests and check current framework compatibility before a production deployment.

Clone the repository:

```bash
git clone https://github.com/laminetoure31770/ia-staff-studio.git
cd ia-staff-studio
```

List profiles and generate a project:

```bash
python3 cli/python/ia_staff.py list
python3 cli/python/ia_staff.py init persona ../my-ia-persona
cd ../my-ia-persona
npm install
npm run typecheck
npm run build
npm run dev
```

Open your browser at the local address printed by Next.js. To try a different profile, use another **new** directory.

## Using the command-line interfaces

### Python

```bash
python3 cli/python/ia_staff.py list
python3 cli/python/ia_staff.py init blog ../my-assisted-blog
```

The generator uses the Python standard library and refuses to overwrite an existing directory. The output is a self-contained starter with a selected distribution manifest.

### TypeScript

```bash
cd cli/typescript
npm install
npm run build
node dist/index.js list
node dist/index.js init medium ../../../my-medium
```

The TypeScript implementation performs the same scaffolding task. Neither CLI stores account credentials, executes workflows, configures an API key, or deploys by itself.

### Validation

```bash
python3 -m unittest discover -s tests -v
```

The GitHub Actions workflow validates the Python scaffolding tests and all JSON manifests on pull requests and on the main branch. Tests do not replace end-to-end authentication, database, provider, cost or production readiness checks.

## Deploying to Vercel

1. Generate the application from a selected profile.
2. Place the generated project in a dedicated Git repository.
3. Import that repository into [Vercel](https://vercel.com/).
4. Use the Next.js framework preset and run `npm run build`.
5. Verify `/api/health` and inspect build logs.
6. Add server-side environment variables **only when actual integrations are implemented**.

The Next.js starter does not perform database migrations, account seeding, credential generation or automatic LLM calls during build. A successful Vercel deployment validates the web starter deployment, **not** the advanced capabilities named by a model profile.

For a deployment directly from this monorepo, set the Vercel Root Directory to `templates/web-nextjs`; this gives a generic starter, not a previously scaffolded model.

## Workflow examples

The `workflows/` directory includes:

- **Agent human review:** input, policy check, model draft, approval, output.
- **Assisted blog review:** editorial draft, evidence checks, moderation and human approval.
- **Documentary RAG:** retrieval, evidence validation, response draft, review.
- **Read-only MCP:** authorization, allowed tool call, audit and output.

These JSON files are **reference specifications**. They are not executable n8n, LangGraph, Mastra or other vendor exports. They explicitly declare execution disabled. An implementation must provide runtime adapters, safe tool permissions, validation, retries, authorization, logging and testing.

## Security and governance

IA STAFF treats an agent as a component that can act on information systems. Tools should be used only when an authenticated user or service is authorized.

Key engineering controls:

1. **Human oversight:** keep approval before high-impact external actions.
2. **Identity and access:** enforce RBAC/ABAC server-side; a hidden menu is not authorization.
3. **Least privilege:** restrict available MCP tools, credentials and network destinations.
4. **Auditability:** record relevant events without leaking secrets or sensitive prompts.
5. **Input and output controls:** validate schema and policy for any model-generated action.
6. **Data boundaries:** isolate environments and datasets; protect personal information.
7. **Separation of concerns:** never run arbitrary seeds or migrations during a build.
8. **Supply-chain hygiene:** review and update dependencies and GitHub Actions.
9. **Fail closed:** refuse unexpected configuration or permission changes.
10. **Measurement:** observe real token use, latency and failures when providers are integrated.

A profile marked “Enterprise” does not imply regulatory certification or compliance by default. Assess obligations under applicable data protection and AI regulations for each real deployment.

## Efficiency and sustainability

IA STAFF promotes **appropriate model selection and resource-conscious operation**. Begin with the simplest design that satisfies a documented need. Bound conversation history, avoid needless retrieval and tool calls, cache safe immutable results where appropriate, and measure rather than guess consumption. The monthly token budgets included in the manifests are planning targets, not enforced provider quotas.

## Development status and roadmap

**Included in this repository:**

- Seven distribution manifests and their common schema.
- Python and TypeScript scaffold CLIs.
- Minimal Next.js application and health check.
- Four workflow design examples.
- Automated Python/JSON checks and documentation.

**Not yet implemented:**

- Production agent runtime or LLM gateway.
- Production blog engine and content moderation.
- Authenticated RBAC/ABAC, SSO and tenant isolation.
- Working RAG/GraphRAG retrieval and MCP execution infrastructure.
- Provider billing, token enforcement, dashboards and operational monitoring.
- Tested database migrations, backup/restore and disaster recovery.
- Automated deployment of every distribution.

The roadmap is incremental: validate the starter → introduce safe authentication → add model connectors and observability → implement one supervised workflow at a time → enable data retrieval → test enterprise boundaries separately.

## Creating and updating shared templates

Use **[GitHub Actions → Create or update a shared template](https://github.com/laminetoure31770/ia-staff-studio/actions/workflows/manage-templates.yml)** to create or update a distribution manifest, reference workflow, Python example or TypeScript example. Each request generates a separate branch and a pull request for review. The workflow never auto-merges, deploys, migrates a database or executes submitted code. Editing functional source requires additional manual review in the pull request.

See the [template contribution guide](docs/template-contributions.md).

## Contributing

Issues, documentation corrections, feature requests and pull requests are welcome.

Before submitting code:

- Identify the problem and intended model.
- Include a minimal reproduction or test where possible.
- Preserve compatibility with the distribution manifest schema.
- Never commit secrets, personally identifiable data or non-redistributable components.
- Distinguish actual implementation from a design-only option.
- Verify user-facing texts in French or English as relevant.
- Respect the existing MIT licensing terms.

Security reports must not expose credentials or confidential data in a public issue.

## License

The repository is distributed under the [MIT License](LICENSE), copyright © 2026 laminetoure31770.

IA STAFF and its branding identify the project. The MIT source-code license is not a representation that third-party models, APIs, datasets, fonts, trademarks or future proprietary packages are covered by the same license.

---

**IA STAFF Studio — Human-led. Responsible by design. Open to collaboration.**
