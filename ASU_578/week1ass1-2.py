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
    visitorID = OneRecord[1]  # visitor ID所在的index是1
    attID = OneRecord[3]  # attraction所在的index是3
    if attID in attraction_count:  # 如果attID在字典attraction_count中，则把visitorID添加进去，逐渐形成列表
        attraction_count[attID].append(visitorID)
    else:
        attraction_count[attID] = [visitorID]    # 否则，建立新的字典，attID是key，visitorID是value


# 统计每个attID被访问了多少次
max_num = -1  
popular_attID = 0
for attID in attraction_count.keys():
    count_number = len(attraction_count[attID]) # 每个attID键对应的value列表长度就是被访问的次数，直接进入比较
    if max_num < count_number :
        max_num = count_number
        popular_attID = attID
    

     
#print(popular_attID)

# 根据popular_attID，去attration_table中遍历，找到该ID对应的attraction name
for line in attration_table:
    if line[1] == popular_attID :
        print(line[2])

