# 3
print("Bài 3:")
def anagram_number(number):
    check = False
    convertInttoStr = str(number)
    reverseNumber = convertInttoStr[::-1]
    if convertInttoStr == reverseNumber:
        check = True
    return ("Số có đảo ngược giống hay không : ",check)
print(anagram_number(121121))

# 4
print("==============================================")
print("Bài 4:")
mydict = {"I" : 1, "V" : 5, "X":10,"L":50,"C":100,"D":500,"M":1000}
num1 = 0
value = 0
def roman_to_int(s):
    len_S = len(s)
    if len_S == 1:
        for i in s:
            if i == "I":
                value = 1
            if i == "V":
                value = 5
            if i == "X":
                value = 10
            if i == "L":
                value = 50
            if i == "C":
                value = 100
            if i == "D":
                value = 500
            if i == "M":
                value = 1000
    elif 2<= len_S < 5:
        value = 0
        for i in range(len_S):
            char1 = str(s[i])
            if char1 in mydict.keys():
                num1 = mydict[char1]   
            value = value + num1
    else:
        print("Vui lòng nhập 1 hoặc 4 ký tự la mã")
    return value
print(roman_to_int("L"))
print(roman_to_int("VI"))
print(roman_to_int("XX"))
print(roman_to_int("LXX"))
print(roman_to_int("XCVI"))
print(roman_to_int("CIII"))
# Hàm trừ
# Điều kiện
print("Em chưa làm kịp hàm trừ")
print(roman_to_int("CXLV"))