# Deploy the IA STAFF Next.js starter to Vercel

1. Generate a project: `python3 cli/python/ia_staff.py init persona ../my-persona`.
2. Push the generated project to its own GitHub repository.
3. Import that repository in Vercel; choose the Next.js preset and root directory `/`.
4. Build with `npm run build`; inspect `/api/health` after deployment.
5. Provide secrets and database configuration only for later, actually implemented modules.

To deploy the generic starter directly from this monorepo, configure Vercel Root Directory as `templates/web-nextjs`.

**No database and no LLM key are required** for the current scaffold. It does not create agents, users, workflows or billing resources merely because a manifest lists them.

Official platform documentation: https://vercel.com/docs/deployments
