#!/usr/bin/env python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 20:40
# @Author  : 蒲天恩
# @File    : data_tongbu_doctor.py
import random
from datetime import date, timedelta
import time
# 随机手机号
def phoneNORandomGenerator():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
               "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
# 随机姓名
def nameRandomGenerator():
    prelist = ["张", "王", "小", "天", "恩", "蒲", "武", "钟", "秀", "大", "毛", "二", "文", "鸡", "起", "舞", "王", "者", "荣", "耀",
               "爷", "哗", "宋", "百", "嘛", "哈", "哥", "书"]
    return random.choice(prelist) + "".join(random.choice(prelist))
# 随机身份证号
def CreateIDCard():
    """
    随机生成符合规则的身份证号码
    """
    # 随机身份证前六位 townNum
    ProvinceID = ['110000', '120100', '120102', '120103']
    townNum = random.choice(ProvinceID)
    # 随机身份证年份,大于18岁  yearNum
    timeDate = time.time()
    yearDate = time.strftime("%Y", time.localtime(timeDate))
    yearNum = random.randint(1980, int(yearDate) - 18)
    # 随机身份证月 日 dateNum
    someDate = date.today() + timedelta(days=random.randint(1, 366))
    dateNum = someDate.strftime("%m%d")
    # 随机身份证后四位的前三位 lastThree
    lastThree = random.randint(100, 999)
    # 随机身份证的前17位 id17(注：都加str仅仅是为了排版。)
    id17 = str(townNum) + str(yearNum) + str(dateNum) + str(lastThree)
    count = 0
    # 权重项
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # 校验项
    CheckCode = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
    for i in range(0, len(id17)):
        count = count + weight[i] * int(id17[i])
    # 获取校验码
    CheckNum = count % 11
    # 得到符合规则的身份证号码
    IDCard = id17 + CheckCode[CheckNum]
    return IDCard

# 部门
def department():
    partment = ["儿科", "眼科", "胸科", "骨科", "耳鼻喉科"]
    return random.choice(partment)
# 医师资格证类型 "
def doctor_id_type():
    doctortype = ["YS", "YZ","YJ","YY","ZC","XL","HS","QT"]
    return  random.choice(doctortype)
# 职称
def doc_title():
    doctitle = ["助理医师","实习医师","住院医师","主治医师", "副主任医师", "主任医师", "护士", "护师", "主管护师", "副主任护师", "主任护师", "其他"]
    return  random.choice(doctitle)
# 职称代码
def doc_title_code():
    doccode = ["ZLYS", "SXYS", "ZYYS", "ZZYS", "FZRYS", "ZRYS", "XHS", "HS", "ZGHS", "FZRHS", "ZRHS", "QT"]
    return  random.choice(doccode)