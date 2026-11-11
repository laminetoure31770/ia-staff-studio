import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "cli" / "python"))
from ia_staff import available, init

class ScaffoldTests(unittest.TestCase):
    def test_seven_models(self):
        self.assertEqual(set(available()), {"persona","agent","blog","light","medium","pro","enterprise"})
    def test_security_defaults(self):
        for model in available():
            data=json.loads((ROOT / "templates" / "distributions" / (model + ".json")).read_text())
            self.assertEqual(data["id"], model)
            self.assertTrue(data["humanApproval"])
            self.assertFalse(data["deployAutomatically"])
    def test_scaffolding(self):
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)/"my-persona"
            init("persona",target)
            self.assertTrue((target/"package.json").exists())
            self.assertEqual(json.loads((target/"distribution.json").read_text())["id"],"persona")
            with self.assertRaises(FileExistsError):
                init("persona",target)
    def test_workflows_disabled(self):
        for path in (ROOT / "workflows").glob("*.json"):
            data=json.loads(path.read_text())
            self.assertEqual(data["execution"],"disabled")
            self.assertTrue(data["humanApproval"])

if __name__ == "__main__":
    unittest.main()
