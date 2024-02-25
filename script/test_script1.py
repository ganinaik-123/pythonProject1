from generic.base_file import BaseTest
from generic.utility import Excel
class Test_script(BaseTest):

    def test_script1(self):
        print(self.driver.title)
        d=Excel.get_data('../data/Book1.xlsx','Sheet2',1,1)
        print("Xl data in test",d)
