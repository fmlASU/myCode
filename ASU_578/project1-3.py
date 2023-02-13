fileName = 'D:\myCode\ASU_578\\adult.data'
fileObj = open(fileName)

Race = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
Up50K = []
Down50K = []
Up50KCount = {}
Down50KCount = {}
for race in Race:
    Up50KCount[race] = 0
    Down50KCount[race] = 0


for oneLine in fileObj:

    if len(oneLine) < 15:
        continue

    Items = oneLine[0: len(oneLine) - 1].split(sep = ',')
    if Items[14] == ' >50K':
        Up50K.append(Items)
    elif Items[14] == ' <=50K':
        Down50K.append(Items)


#print(Up50K)
#print(Down50K)

for onelineup in Up50K:
    pass
