#!/usr/bin/env python3
"""IA STAFF Studio — minimal Python scaffold CLI."""
import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRESETS = ROOT / "templates" / "distributions"
STARTER = ROOT / "templates" / "web-nextjs"

def available():
    return sorted(path.stem for path in PRESETS.glob("*.json"))

def init(model, destination):
    if model not in available():
        raise ValueError("Unknown distribution: " + model)
    output = Path(destination).resolve()
    if output.exists():
        raise FileExistsError("Destination already exists: " + str(output))
    if output == ROOT or ROOT in output.parents:
        raise ValueError("Create your project outside this repository")
    manifest = json.loads((PRESETS / (model + ".json")).read_text(encoding="utf-8"))
    if manifest["humanApproval"] is not True or manifest["deployAutomatically"] is not False:
        raise ValueError("Unsafe manifest")
    shutil.copytree(STARTER, output)
    (output / "distribution.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return output

def main():
    parser = argparse.ArgumentParser(description="IA STAFF template CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    create = sub.add_parser("init")
    create.add_argument("model", choices=available())
    create.add_argument("directory")
    args = parser.parse_args()
    try:
        if args.command == "list":
            for model in available():
                print(model)
        else:
            result = init(args.model, args.directory)
            print("Created: " + str(result))
    except (OSError, ValueError) as error:
        parser.exit(2, str(error) + "\n")

if __name__ == "__main__":
    main()
