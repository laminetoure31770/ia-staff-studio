#!/usr/bin/env python3
"""Generate or refresh a shareable IA STAFF starter via a reviewed pull request."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAFE_NAME = re.compile(r"^[a-z][a-z0-9-]{1,47}$")
KINDS = ("distribution", "workflow", "python", "typescript")
ACTIONS = ("create", "update")


def destination(kind: str, name: str) -> Path:
    if kind == "distribution":
        return ROOT / "templates" / "distributions" / (name + ".json")
    if kind == "workflow":
        return ROOT / "workflows" / (name + ".json")
    if kind == "python":
        return ROOT / "templates" / "code" / "python" / name / "main.py"
    return ROOT / "templates" / "code" / "typescript" / name / "index.ts"


def generate(kind: str, name: str, action: str, title: str, description: str) -> Path:
    if kind not in KINDS or action not in ACTIONS:
        raise ValueError("Unsupported kind or action")
    if not SAFE_NAME.fullmatch(name):
        raise ValueError("Name must be a lowercase slug (2–48 characters)")
    if any(ord(c) < 32 for c in title + description):
        raise ValueError("Control characters are not allowed")
    if len(title.strip()) < 3 or len(title) > 100:
        raise ValueError("Title must contain 3–100 characters")
    if len(description.strip()) < 8 or len(description) > 500:
        raise ValueError("Description must contain 8–500 characters")

    path = destination(kind, name)
    exists = path.exists()
    if action == "create" and exists:
        raise FileExistsError("Template already exists; select update")
    if action == "update" and not exists:
        raise FileNotFoundError("Template not found; select create")
    path.parent.mkdir(parents=True, exist_ok=True)

    if kind == "distribution":
        if exists:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("id") != name or data.get("schemaVersion") != 1:
                raise ValueError("Invalid existing manifest")
            data["name"] = title.strip()
            data["description"] = description.strip()
        else:
            data = {
                "schemaVersion": 1, "id": name, "name": title.strip(),
                "description": description.strip(), "status": "scaffold",
                "storage": "postgres", "agents": 0, "assistants": 1,
                "monthlyTokenBudget": 100000, "contextLimit": 2048,
                "modules": ["human-review"],
                "features": {"rag": False, "mcp": False, "graph": False,
                             "multitenant": False, "blog": False},
                "humanApproval": True, "deployAutomatically": False,
            }
        if data.get("humanApproval") is not True or data.get("deployAutomatically") is not False:
            raise ValueError("Unsafe distribution settings")
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        catalog_path = ROOT / "catalog" / "models.json"
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        catalog["templates"] = list(dict.fromkeys([*catalog["templates"], name]))
        catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    elif kind == "workflow":
        if exists:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("id") != name or data.get("execution") != "disabled":
                raise ValueError("Cannot update a workflow that enables execution")
            data["title"] = title.strip()
            data["description"] = description.strip()
        else:
            data = {
                "schemaVersion": 1, "id": name, "title": title.strip(),
                "description": description.strip(), "status": "reference_only",
                "execution": "disabled", "humanApproval": True,
                "nodes": [{"id": "input", "kind": "input"},
                          {"id": "review", "kind": "human-approval"},
                          {"id": "output", "kind": "output"}],
            }
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    elif kind == "python":
        if not exists:
            path.write_text('"""' + title.strip() + ' — shareable example (no external actions)."""\n\n'
                            'def main() -> None:\n    print("Template ready: configure before use")\n\n'
                            'if __name__ == "__main__":\n    main()\n', encoding="utf-8")
        (path.parent / "README.md").write_text(
            "# " + title.strip() + "\n\n" + description.strip() +
            "\n\nThis is a scaffold only. Add tests and review before distribution.\n",
            encoding="utf-8")
    else:
        if not exists:
            path.write_text('// ' + title.strip() + ' — standalone example\n'
                            'export function run(): string {\n  return "Template ready: configure before use";\n}\n',
                            encoding="utf-8")
        (path.parent / "README.md").write_text(
            "# " + title.strip() + "\n\n" + description.strip() +
            "\n\nThis is a scaffold only. Add tests and review before distribution.\n",
            encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=KINDS, required=True)
    parser.add_argument("--action", choices=ACTIONS, required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--description", required=True)
    args = parser.parse_args()
    print(generate(args.kind, args.name, args.action, args.title, args.description).relative_to(ROOT))


if __name__ == "__main__":
    main()
