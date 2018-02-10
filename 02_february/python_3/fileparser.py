# What the heck

item_line_start = "-"

def loadnamesonlyfromfile(data_file_path):
    returnarray = []
    with open(data_file_path, "r") as data_file:
        rawlinedata = [line.strip() for line in data_file]
        print(rawlinedata)
    for entry in rawlinedata:
        if entry[0] == item_line_start:
            cleanedentry = getitemname(entry)
            returnarray.append(cleanedentry)
    return returnarray

def loaddatafromfile(data_file_path):
    returnarray = []
    with open(data_file_path, "r") as data_file:
        rawlinedata = [line.strip() for line in data_file]
        print(rawlinedata)
    for entry in rawlinedata:
        if entry[0] == item_line_start:
            cleanedentry = getitemname(entry)
            returnarray.append(cleanedentry)
    return returnarray

#cleaner
def getitemname(rawitem):
    clean_name = rawitem[2:]
    print("|" + clean_name + "|")
    return clean_name

#def f(x):
#    return {
#        'a': 1,
#        'b': 2,
#    }[x]

#####def f(x):
####    return {
###        'a': 1,
##        'b': 2
#    }.get(x, 9)    # 9 is default if x not found
