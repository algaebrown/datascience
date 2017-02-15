# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 09:47:32 2017

@author: Charl
To deal with data gathered from "102寒假國考調查"
"""
# import from excel
import pandas as pd
df = pd.read_excel('102寒假國考調查- code.xlsx', header = 0)

# delete usless column
del df['Score']
del df['Timestamp']

#list all column names
columnNames = list(df.columns.values)
#
"""
['我的醫學一原始分數', numeric
 '我的醫學二原始分數', numeric
 '我從哪時開始準備國考', numeric**
 '準備國考「解剖」我做了', complex binary
 '準備國考微生物我做了：', complex binary
 '我準備免疫學的「主要」教材為？',complex binary
 '我如何準備公衛',complex binary
 '我準備生理的教材為？',complex binary
 '我準備生化的教材為？',complex binary
 '我準備藥理的教材為？',complex binary
 '我準備病理的教材為？',complex binary
 '考前一個月，我如何調適自己(休閒娛樂之類的、運動習慣、飲食等都可以寫)',binary
 '我有修過這些選修課或研究所的課',complex binary
 '我曾經重修/暑修以下科目',complex binary
 '我「基礎」block考試成績最常有的十位數為？',numeric
 '我的103學年排名',numeric
 '我的104學年排名',numeric
 '我準備基礎block的方式',complex binary
 '我的基礎block到課情形',numeric**
 '我自認我在課堂有專心在聽',binary
 '在修習「臨床」block的時候，我會複習對應的「基礎學科」或「病理學」',binary
 '想跟即將進入臨床block的103學弟妹說：',no
 '準備國考後，我想給即將進入block的104學弟妹的建議：',no
 '準備國考後，我想跟即將開始上生化的105學弟妹說：']no
 """
 # numeric[0:2, 14:17]; dict[2,18]
 #binary[19,20]
 #no [21:]
newDf = pd.DataFrame()
newDf = newDf.fillna(0) # with 0s rather than NaNs

#index
rows = df.shape[0] #tuple

#醫學一、醫學二原始分數 check isnumeric, 
numericNames= columnNames[0:2]+ columnNames[14:17]
for i in numericNames:
    newDf[i]=df[i]

#numeric2
def attendence(x):
    if "百分百" in x:
        y = 1
    elif "七成五" in x:
        y = 0.75
    elif "五成" in x:
        y = 0.5
    elif "二成五" in x:
        y = 0.25
    else:
        y = 0
    return y
newDf['出席率'] = df['我的基礎block到課情形'].map(attendence)
def prepareTime(x):
    if "暑假尾巴" in x:
        y = 162
    elif "暑假中間" in x:
        y = 192
    elif "暑假頭" in x:
        y = 222
    elif "期中考" in x:
        y = 100
    else:
        y = 35
    return y
newDf['準備天數'] = df['我從哪時開始準備國考'].map(prepareTime)   

#binary ones
yesToOne = lambda x: True if x == "是" else False
binaryNames = columnNames[19:21]+ columnNames[11:12]
for i in columnNames[19:21]:
    newDf[i]= df[i].map(yesToOne)
sportToOne = lambda x: True if "規律運動" in x else False
newDf['規律運動']=df['考前一個月，我如何調適自己(休閒娛樂之類的、運動習慣、飲食等都可以寫)'].map(sportToOne)
  

# parse other column
# original [a,b,c,e,other]-->[1,1,1,0,1]+[other] given dataframe names = [a,b,c,d,e]
complexBinary = columnNames[3:11] + columnNames[12:14] + columnNames[17:18]
for i in complexBinary:
    lisAll=[] 
    for j in range(rows):
        if type(df.ix[j,i]) == str:
            lisSingle = str.split(df.ix[j,i],', ')
            lisAll = list(set(lisAll)|set(lisSingle))
    for j in range(rows):
        #binaryConvert=[0]*len(lisAll)
        if type(df.ix[j,i]) == str:
            for k in range(len(lisAll)):
                if lisAll[k] in df.ix[j,i]:
                    #input()
                    newDf.ix[j,lisAll[k]] = True               
                    #binaryConvert[k] = 1
                else: newDf.ix[j,lisAll[k]] = False
        else: 
            for k in range(len(lisAll)):
               newDf.ix[j,lisAll[k]] = False 
                #binaryConvert[k] = 0
        #newDf.ix[j,lisAll]=binaryConvert

# save dataframe
newDf.to_pickle("parsedData") 

         

   

