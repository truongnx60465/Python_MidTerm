# 1
from datetime import datetime
from datetime import date
import time

def day_diff(release_date, code_complete_day):
    convert_Releasedate = datetime.strptime(release_date, "%d/%m/%Y")
    # print("1",convert_Releasedate)
    convert_Completeday = datetime.strptime(code_complete_day, "%Y-%d-%m")
    # print("2",convert_Completeday)
    countDay = convert_Releasedate - convert_Completeday
    return ("số ngày mà team test có để test sản phẩm: %d ngày"%(countDay.days))
print("Bài 1:")
print(day_diff("19/12/2021","2021-17-05"))


# 2
print("==============================================")
def alpha_num(sentence):
    cutStr = sentence.split()
    final_list = list()
    for i in cutStr:
        isLetter = False
        isNum = False
        for f in i:
            if f.isalpha():
               isLetter = True
            if f.isdigit():
                isNum = True
        if isLetter and isNum:
            newList = i
            final_list.append(newList)
        
    return ("Các ký tự là: %s"%(final_list))
print("Bài 2:")
print(alpha_num("Emma25 is Data scientist50 and AI Expert"))  