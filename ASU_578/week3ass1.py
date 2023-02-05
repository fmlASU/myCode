'''


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


target_visitor = [165316, 296394, 404385, 448990, 1835254]

target = dict()
for oneline in sequences:
    for visitorID in target_visitor:
        if oneline[1] == visitorID:
            target[oneline[1]] = oneline[2].split(sep = '-')

#print(target)

# import copy

PrimaryDistance = dict()
SubDistance = dict()

for targetID in target.keys():   
    PrimaryDistance[targetID] = 0

    compare_target = target.copy()

    del compare_target[targetID]
    #print(compare_target)
    #print(target)    


    for compID in target.keys():
        if(targetID == compID):
            continue
        else:
            pass


    num = len(target[targetID])
    #print(num)
    #print(target[targetID])
    SubDistance = dict()
    for compareID in compare_target.keys():
        SubDistance[compareID] = 0

        for i in range(num):
            if target[targetID][i] != compare_target[compareID][i]:
                SubDistance[compareID] += 1
        #print(dis2)
    PrimaryDistance[targetID] = SubDistance
    

print(PrimaryDistance)

        

    #print(targetID)