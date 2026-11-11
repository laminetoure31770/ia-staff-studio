"""Static validation of the template contribution workflow."""
import importlib.util
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("template_manager",ROOT/"scripts"/"template_manager.py")
module=importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(module)

class TemplateManagerTests(unittest.TestCase):
    def test_slug_validation(self):
        for slug in ("../secret","HELLO","bad/name","a","spaces here"):
            with self.subTest(slug=slug):
                with self.assertRaises(ValueError):
                    module.generate("python",slug,"create","Valid title","Valid description")
    def test_unknown_kind_rejected(self):
        with self.assertRaises(ValueError):
            module.generate("shell","sample","create","Valid title","Valid description")
    def test_title_control_characters_rejected(self):
        with self.assertRaises(ValueError):
            module.generate("typescript","sample","create","Hello\nattack","Valid description")
    def test_missing_update_rejected(self):
        with self.assertRaises(FileNotFoundError):
            module.generate("workflow","never-created-zzzz","update","Valid title","Valid description")

if __name__=="__main__":
    unittest.main()
