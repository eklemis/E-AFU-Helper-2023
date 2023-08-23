import unittest

#from main_actions.general_actions.manual_afu import isCorrectManualAfuFile
from main_actions.general_actions.manual_afu import isCorrectManualAfuFile

class TestClass(unittest.TestCase):
    def test_correct_manual_afus_one(self):
        self.assertTrue(isCorrectManualAfuFile("D:\\OneDrive - Save the Children International\\Kantor\\2023\\AFU\\Dahsboard\\Collected_Data.xlsx",
                                               "D:\\OneDrive - Save the Children International\\Kantor\\2023\\AFU\\Dahsboard\\tes1.xlsx"))


    def test_correct_manual_afus_two(self):
        self.assertTrue(isCorrectManualAfuFile(
            "D:\\OneDrive - Save the Children International\\Kantor\\2023\\AFU\\Dahsboard\\Collected_Data.xlsx",
            "D:\\OneDrive - Save the Children International\\Kantor\\2023\\AFU\\Dahsboard\\tes2.xlsx"))

    def test_incorrect_manual_afus(self):
        self.assertFalse(isCorrectManualAfuFile(
            "D:\\OneDrive - Save the Children International\\Kantor\\2023\\AFU\\Dahsboard\\Collected_Data.xlsx",
            "D:\\OneDrive - Save the Children International\\Kantor\\2023\\AFU\\Dahsboard\\SS_Dash_Data.xlsx"))

if __name__ == '__main__':
    unittest.main()