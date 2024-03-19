import unittest
from verify_json import *

class TestVerifyJSON(unittest.TestCase):

    def testTrueInput(self):
        self.assertTrue(verifyJson("JSONTrueFile"))

    def testFalseInput(self):
        self.assertFalse(verifyJson("JSONFalseFile"))

    def testFalseInput2(self):
        self.assertFalse(verifyJson("JSONFalseFile2"))

    def testWrongFileInput(self):
        self.assertEqual(verifyJson("InexistantJSONFile"), "File not found")

    def testNoResourceInput(self):
        self.assertEqual(verifyJson("JSONNoResource"), "JSON parsing error: No Resource found")

    def testNoStatementInput(self):
        self.assertEqual(verifyJson("JSONNoStatement"), "JSON parsing error: No PolicyDocument or Statement found")

    def testDecodeErrorInput(self):
        self.assertEqual(verifyJson("JSONDecodingErrorFile"), "JSON decoding error: Expecting value: line 1 column 1 (char 0)")


if __name__ == '__main__':
    unittest.main()