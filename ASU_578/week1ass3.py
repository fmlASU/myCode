import sqlite3 as sql
dbName = 'D:\python_test\dinofunworld.db'
con = sql.connect(dbName)
cur = con.cursor()

# 分别从attraction和checkin表格取出所有数据
cur.execute("SELECT * FROM attraction")
attraction_table = cur.fetchall()

cur.execute("SELECT * FROM checkin")
checkin = cur.fetchall()


# 从attraction表格中找出type是fast food的attractionID，并保存到fastfoodID中
attID_name = dict()  # ID和名字对应信息
FastFoodID = dict()  # fastfood对应的ID
visitors = set() # 后面比较时要用到游客总数，不要重复计算

for OneRecord in attraction_table:     
    attID_name[OneRecord[1]] = OneRecord[2]
    if OneRecord[5] == 'Fast Food': # 如果记录中index=5的数据为fast food，则把相应的attID加入到attraction_count中去
        FastFoodID[OneRecord[1]] = set()


print(FastFoodID)

# 遍历attraction_count和checkin表格，如果attraction_count的attID和checkin中的attraction一致，则统计该attID下的数量


for attraction in checkin:
    attID = attraction[3]
    visitorID = attraction[1]
    visitors.add(visitorID)

    if attID in FastFoodID :
        FastFoodID[attID].add(visitorID)


print(FastFoodID)

# 统计每个fast foodID下的游客总数
finalcount = dict()

for attID in FastFoodID.keys():
    finalcount[attID] = len(FastFoodID[attID])

print(finalcount)

#找出有最少游客的fastfoodID
min = len(visitors)+1
minID = 0
for attID in finalcount:
    if min > finalcount[attID]:
        min = finalcount[attID]
        minID = attID
print("ID =", minID)
print('Name =', attID_name[minID])
print(attID_name[minID])



'''

for onecheckin in checkin:

    attractionID = onecheckin[3]
    visitorID = onecheckin[1]
    visitors.add(visitorID)

    if attractionID in records :
        records[attractionID].add(visitorID)
 

final_result = dict()

for ID in records.keys() : 
    final_result[ID] = len(records[ID])

min = len(visitors) + 1
minID = 0
for ID in final_result.keys():
    if min > final_result[ID]:
        min = final_result[ID]
        minID = ID

#print("ID=", minID)
#print("Name = ", attractionIDNameMap[minID])
print(attractionIDNameMap[minID])

'''