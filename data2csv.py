import pandas as pd
import numpy as np
from xpinyin import Pinyin


f=open('12306@邮箱-密码-姓名-身份证-手机.txt', encoding='gbk')
data = []
p = Pinyin()
for line in f:
    tem = line.split("----")
    tem.insert(4,tem[3][6:14])
    tem.insert(3,p.get_pinyin(tem[2]))
    data.append(tem)
data = np.array(data)
df = pd.DataFrame(data[:,:-1],columns=["Email","Password","Name","Name_Pinyin","Id","BirthDay","NickName","PhoneNumber"])
df.to_csv("PdData.csv",index=False)