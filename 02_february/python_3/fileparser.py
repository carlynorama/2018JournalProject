# What the heck

import re
special="-#|[]()@"

def loadnamesonlyfromfile(data_file_path):
    returnarray = []
    with open(data_file_path, "r") as data_file:
        rawlinedata = [line.strip() for line in data_file]
        print(rawlinedata)
    for entry in rawlinedata:
        if entry and entry[0] == special[0]:
            cleanedentry = getitemname(entry)
            returnarray.append(cleanedentry)
    return returnarray

def loaddatafromfile(data_file_path):
    returnarray = []
    with open(data_file_path, "r") as data_file:
        rawlinedata = [line.strip() for line in data_file]
        print(rawlinedata)
    for entry in rawlinedata:
        if entry and entry[0] == special[0]:
            cleanedentry = getitemdictionary(entry)
            returnarray.append(cleanedentry)
    return returnarray

#cleaner
def getitemname(rawitem):
    clean_name = rawitem[2:]
    print("|" + clean_name + "|")
    return clean_name

#cleaner
def getitemdictionary(rawitem):
    itemdictionary = {}
    brokenatnotes = rawitem.partition("|")
    if getname(brokenatnotes[0]):
        itemdictionary["name"] = getname(brokenatnotes[0])
    if getcontext(brokenatnotes[0]):
        itemdictionary["context"] = getcontext(brokenatnotes[0])
    if getstatus(brokenatnotes[0]):
        itemdictionary["status"] = getstatus(brokenatnotes[0])
    if getdays(brokenatnotes[0]):
        itemdictionary["days"] = getdays(brokenatnotes[0])
    if brokenatnotes[2]:
        itemdictionary["note"] = brokenatnotes[2].strip()
    print(itemdictionary)
    return itemdictionary

def getname(rawstring):
    regex = r"-( \[.*\] | )(.*?)[@#|(]"
    match = re.search(regex, rawstring)
    if match:
        name = match.group(2)
    else:
        name = ""
    return name

def getnote(rawstring):
    note = rawstring.partition("|")[2].strip()
    return note

def getdays(rawstring):
    regex = r"\(([^()]*)\)"
    match = re.search(regex, rawstring)
    if match:
        days = match.group(1)
    else:
        days = ""
    return days

def getcontext(rawstring):
    regex = r"(@[^\s]+)\s"
    match = re.search(regex, rawstring)
    if match:
        context = match.group(0)
    else:
        context = ""
    return context

def statuslookup(x):
    return {
        ' ': "unmarked",
        'x': "done",
        'X': "done",
        '!': "urgent",
        '>': "migrated",
        '<': "scheduled",
        'O': "event",
        'a': "assigned",
        '-': "archived",
        '?': "needs research",
        '1': "1st priority",
        '2': "2nd priority",
        '3': "3rd priority",
    }.get(x, x)
#    }.get(x, "unknown mark")

def getstatus(rawstring):
    regex = r"\[(.*)\]"
    match = re.search(regex, rawstring)
    if match:
        status = statuslookup(match.group(1))
    else:
        status = ""
    return status

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
