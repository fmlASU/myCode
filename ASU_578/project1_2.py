fileName = 'C:\\temp\myCode\ASU_578\\adult.data'
fileObj = open(fileName)

Up50K_Male = 0
Up50K_Female = 0
Down50K_Male = 0
Down50K_Female = 0

for oneLine in fileObj:

    if len(oneLine) < 15:
        continue

    Items = oneLine[0: len(oneLine) - 1].split(sep = ',')

    if Items[14] == ' >50K' and Items[9] == ' Male':
        Up50K_Male += 1
    elif Items[14] == ' >50K' and Items[9] == ' Female':
        Up50K_Female += 1
    elif Items[14] == ' <=50K' and Items[9] == ' Male':
        Down50K_Male += 1
    elif Items[14] == ' <=50K' and Items[9] == ' Female':
        Down50K_Female += 1

print(Up50K_Male, Up50K_Female, Down50K_Male, Down50K_Female)


fileObj.close()