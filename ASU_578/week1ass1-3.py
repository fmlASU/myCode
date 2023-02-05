'''
What is the most popular attraction to visit in the park?

Note: Your output should be the name of the attraction.

'''


import sqlite3 as sql
dbName = 'D:\python_test\dinofunworld.db'
con = sql.connect(dbName)
cur = con.cursor()

# 分别从attraction和checkin表格取出所有数据
cur.execute("SELECT * FROM attraction")
attration_table = cur.fetchall()

cur.execute("SELECT * FROM checkin")
checkin = cur.fetchall()

# 列出进入每个attractionID的所有visitorID
attraction_count = dict()
for OneRecord in checkin:
    visitorID = OneRecord[1]  
    attID = OneRecord[3]  
    if attID in attraction_count:  
        attraction_count[attID].append(visitorID)
    else:
        attraction_count[attID] = [visitorID]    


# 统计每个attID被访问了多少次
max_num = -1  
popular_attID = 0
for attID in attraction_count.keys():
    count_number = len(attraction_count[attID]) 
    if max_num < count_number :
        max_num = count_number
        popular_attID = attID
    

     
#print(popular_attID)

# 根据popular_attID，去attration_table中遍历，找到该ID对应的attraction name
for line in attration_table:
    if line[1] == popular_attID :
        print(line[2])

