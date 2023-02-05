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
    if attID in attraction_count:  # 如果attID在字典attraction_count中，attID就是key，把visitorID添加进去，逐渐形成value列表
        attraction_count[attID].append(visitorID)  # attraction_count[attID]的value是列表，可以用append()操作
    else:
        attraction_count[attID] = [visitorID]    # 否则，建立新的字典，attID是key，visitorID是value,首次循环时进入该语句，value是列表，


# 统计每个attID被访问了多少次
attraction_count_number = dict()

for attID in attraction_count.keys():
    count_number = len(attraction_count[attID]) # attraction_count = {attID: [visitorID, visitorID, visitorID ....]}每个attID键对应的值是一个列表，统计列表长度，即统计被访问次数
    attraction_count_number[attID] = count_number  # 建立字典{attID, 被访问次数}

# 遍历字典attraction_count_number，根据keys()取出count_number,然后比较
max_num = -1  # 初始化
popular_attID = 0
for attID in attraction_count_number.keys():
    count_number = attraction_count_number[attID]
    if max_num < count_number :
        max_num = count_number
        popular_attID = attID # 把当前有最大count_number值所对应的attID赋值给popular_attID
#print(popular_attID)

# 根据popular_attID，去attration_table中遍历，找到该ID对应的attraction name
for line in attration_table:
    if line[1] == popular_attID :
        print(line[2])

