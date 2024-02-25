import openpyxl

class Excel:
    @staticmethod
    def get_data(xl_path,sheet_name,row,col):
        try:
            wb=openpyxl.open(xl_path)
            sheet=wb[sheet_name]
            data=sheet.cell(row,col).value
            print("Xl data",data)
        except:
            print("error in reading Xl data")
            data =None
        return data