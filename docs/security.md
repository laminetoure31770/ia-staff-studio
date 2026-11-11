# Security policy for starters

1. Keep API credentials and database URLs out of client-side code and Git.
2. Review and restrict any future MCP tools and external effects by identity and role.
3. Do not interpret reference workflows as executable programs.
4. Require human review for consequential actions.
5. Enforce quotas and RBAC/ABAC on servers, not just hidden menus.
6. Avoid performing database migrations or demo seeds during Next.js compilation.
7. Use separate staging databases and verify migrations independently.
8. Protect personal information; minimize retained data.
9. Budget values in manifests are descriptive targets, not cost guarantees.
