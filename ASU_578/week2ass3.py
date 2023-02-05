'''
week2 Q3
Make a line chart of attendance at Atmosfear every five minutes.

Note: For this question, display the line chart in the notebook and print the data used to create the chart as a list of lists (ex: [['Stall 1', 10], ['Stall 2', 50], ...]) or tuple lists (ex: [('Stall 1, 10),('Stall 2', 50), ...]

The first item in tuples is irrelevant, but you can put in some meaningful information. The second item is the count of visits at that moment. For example, your output should look like this (in Python syntax; not relevant to the correct answer): [ (0, 0), (1, 7), (2, 3), …, (190, 4), (191, 5) ].

'''

import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt

dbName = 'D:\python_test\dinofunworld.db'
con = sql.connect(dbName)
cur = con.cursor()

# 分别从attraction和checkin表格取出所有数据
#cur.execute("SELECT * FROM attraction")
#attraction_table = cur.fetchall()

cur.execute("SELECT * FROM sequences")
sequences = cur.fetchall()

# print(sequences)
TotalTimeSlots = 192
ColNumOfTimeSlotInfo = 2
TargetAttID = '8'  # 目标attractionID

count = dict()
for TimeSlotID in range(TotalTimeSlots):    
    count[TimeSlotID] = 0   # 初始化每个time slot的初始值为0


AtmosfearVisit = list()

for records in sequences:  # 提取sequences中的每一条记录record
    AtmosfearVisit.append(records[ColNumOfTimeSlotInfo])  # 把record中的采集的time slot序列送到AtmosfearVisit列表中

#print(AtmosfearVisit[1])
#print(len(AtmosfearVisit[1]))


for visit in AtmosfearVisit:

    #print(visit)
    record = visit.split(sep = '-')  # 把字符串拆分，形成列表
    #print(record)
    for TimeSlotID in range(TotalTimeSlots):    
         
        if record[TimeSlotID] == TargetAttID: # 比较
            count[TimeSlotID] += 1

        else:
            continue

FinalResult = []

for TimeSlotID in count.keys():
    FinalResult.append((TimeSlotID, count[TimeSlotID]))
print(FinalResult)
X = count.keys()
Y = count.values()
plt.plot(X, Y)
plt.xlabel('TimeslotID')
plt.ylabel('VisitNumber')
plt.title('Attendance at Atmosfear')

plt.show()
