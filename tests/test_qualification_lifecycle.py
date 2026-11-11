"""Run lifecycle qualification in an isolated temporary tree; never alter production data."""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

SOURCE=Path(__file__).resolve().parents[1]
DATA=json.loads((SOURCE/"tests"/"fixtures"/"qual-template-cases.json").read_text(encoding="utf-8"))

spec=importlib.util.spec_from_file_location("template_manager_qualification",SOURCE/"scripts"/"template_manager.py")
manager=importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(manager)

class QualificationLifecycle(unittest.TestCase):
    def test_synthetic_create_update(self):
        self.assertTrue(DATA["synthetic"])
        self.assertEqual(DATA["environment"],"qual")
        with tempfile.TemporaryDirectory(prefix="ia-staff-qual-") as td:
            root=Path(td)
            (root/"catalog").mkdir(parents=True)
            (root/"catalog"/"models.json").write_text(json.dumps({"templates":["persona"]}),encoding="utf-8")
            original=manager.ROOT
            try:
                manager.ROOT=root
                for case in DATA["cases"]:
                    path=manager.generate(case["kind"],case["name"],case["action"],case["title"],case["description"])
                    self.assertTrue(path.exists())
                profile=json.loads((root/"templates"/"distributions"/"demo-qual.json").read_text())
                self.assertTrue(profile["humanApproval"])
                self.assertFalse(profile["deployAutomatically"])
                self.assertEqual(profile["name"],"Qualification Persona V2")
                workflow=json.loads((root/"workflows"/"review-qual.json").read_text())
                self.assertEqual(workflow["execution"],"disabled")
                self.assertEqual(workflow["title"],"Human Review QA V2")
                self.assertEqual((root/"catalog"/"models.json").read_text().count("demo-qual"),1)
                self.assertTrue((root/"templates"/"code"/"python"/"hello-qual"/"main.py").exists())
                self.assertTrue((root/"templates"/"code"/"typescript"/"hello-qual"/"index.ts").exists())
            finally:
                manager.ROOT=original
    def test_no_overwrite_existing(self):
        with tempfile.TemporaryDirectory(prefix="ia-staff-qual-") as td:
            root=Path(td)
            (root/"catalog").mkdir(parents=True)
            (root/"catalog"/"models.json").write_text('{"templates":[]}',encoding="utf-8")
            original=manager.ROOT
            try:
                manager.ROOT=root
                manager.generate("workflow","safe-test","create","Safe Workflow","Synthetic workflow for validation")
                with self.assertRaises(FileExistsError):
                    manager.generate("workflow","safe-test","create","Safe Workflow","Synthetic workflow for validation")
            finally:
                manager.ROOT=original

if __name__=="__main__":
    unittest.main()
