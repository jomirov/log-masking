import unittest, json, pathlib, sys
from main import redact


with pathlib.Path("test/input.json").open("r") as file:
    input_file = json.load(file)
class test_mask_log(unittest.TestCase):
    def test_NestedObjectsShouldNotGetChange(self):
        res = redact("test/input.json")

        redact_file = res[0]
        update_count = res[1]

        self.assertEqual(update_count, 4)

        self.assertEqual(input_file["event"], redact_file["event"])
        self.assertEqual(input_file["meta"]["attempt"], redact_file["meta"]["attempt"])
        self.assertEqual(input_file["message"], redact_file["message"])

    def test_CheckKeysRegistryAndValues(self):
        res = redact("test/input.json")

        redact_file = res[0]

        mask_value = "[HIDDEN]"

        self.assertEqual(redact_file["email"], mask_value)
        self.assertEqual(redact_file["token"], mask_value)
        self.assertEqual(redact_file["meta"]["EMAIL"], mask_value)
        self.assertEqual(redact_file["items"][0]["token"], mask_value)

    def test_CheckByteSize(self):
        res = redact("test/input.json")

        redact_file = res[0]

        self.assertEqual(sys.getsizeof(redact_file), sys.getsizeof(input_file))

    def test_PreviewShouldNotCreateFile(self):
        res = redact("test/input.json")
        
        try: 
            with pathlib.Path("test/output.json").open("r") as file: pass
        except:
            factual_res = False
        expected_res = False

        self.assertEqual(factual_res, expected_res)

    def test_IncorrectJSONShouldNotBeProcessed(self):
        with self.assertRaises(KeyError) as cm:
            redact("test/incorrect_input.json")
        the_exception = cm.exception
        self.assertEqual(the_exception.args, ("Incorrect JSON",))

if __name__ == "__main__":
    unittest.main()