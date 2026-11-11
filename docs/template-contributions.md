# Template contribution workflow

## From GitHub Actions (no local Git required)

Open **[Actions → Create or update a shared template](https://github.com/laminetoure31770/ia-staff-studio/actions/workflows/manage-templates.yml)** and choose **Run workflow**.

Specify:

- **action**: `create` (new) or `update` (existing)
- **kind**: `distribution`, `workflow`, `python` or `typescript`
- **name**: lowercase slug (letters, digits, hyphens), 2–48 characters
- **title** and **description**: plain text to document the model

The workflow validates the changes, creates a separate `template/<run-id>` branch and opens a **pull request for human review**. It does **not** merge into `main`, deploy to Vercel or execute an agent.

**Update behavior:** distribution and workflow updates edit their titles/descriptions and preserve the existing settings and graph; Python/TypeScript updates refresh their README only, leaving existing source untouched. To add business logic, edit the PR branch yourself, supply tests, and request review. Existing files cannot be overwritten through the create action.

## CI and review

The regular `validate.yml` runs on pull requests and checks the seven baseline profiles, JSON syntax, Python CLI and template-manager validation. Review source licensing, package dependencies, reproducibility, security implications and tests before merging.

## Required GitHub setting

Repository Settings → Actions → General → Workflow permissions: select read/write permissions where available and allow GitHub Actions to create pull requests. The workflow also declares `contents: write` and `pull-requests: write`. If the organization policy forbids PR creation, its branch push may succeed but PR opening will fail; use the pushed branch to open a PR manually.

## CLI or local contributions

Run from the repository root:

```bash
python3 scripts/template_manager.py --action create --kind workflow --name my-workflow \
  --title "My workflow" --description "Description of what the workflow will do"
python3 -m unittest discover -s tests -v
```

Then submit the result through a normal pull request. **Never include API secrets or personal data**. Created workflow JSON is a design reference, not an executable agent runtime.
