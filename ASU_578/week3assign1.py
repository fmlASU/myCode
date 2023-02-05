import sqlite3 as sql
#import pandas as pd
#import matplotlib.pyplot as plt

dbName = 'D:\python_test\dinofunworld.db'
con = sql.connect(dbName)
cur = con.cursor()

cur.execute("SELECT * FROM sequences")
sequences = cur.fetchall()

target_visitor = [165316, 296394, 404385, 448990, 1835254]

records = dict()
result = dict()

for targetVisitorID in target_visitor:
    records[targetVisitorID] = []
    result[targetVisitorID] = dict()

for oneline in sequences:
    visitorID = oneline[1]
    if visitorID in records:
        VisitInTimeSlot = oneline[2].split(sep = '-')
        records[visitorID] = VisitInTimeSlot

for i in range(len(target_visitor)):
    VisitorID_i = target_visitor[i]
    VisitInTimeSlot_i = records[VisitorID_i]
    for j in range(i+1, len(target_visitor)):
        VisitorID_j = target_visitor[j]
        VisitInTimeSlot_j = records[VisitorID_j]
        minLen = min(len(VisitInTimeSlot_i),len(VisitInTimeSlot_j))
        distance = 0
        for k in range(minLen):
            if(VisitInTimeSlot_i[k] != VisitInTimeSlot_j[k]):
                distance += 1
        result[VisitorID_i][VisitorID_j] = distance
        result[VisitorID_j][VisitorID_i] = distance

print(result)