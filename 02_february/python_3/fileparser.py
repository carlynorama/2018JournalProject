# What the heck

import re
special="-#|[]()@"
allowedFirst="xX!><Oa-D?0123456789ø·•"

def loadnames(data_file_path):
    returnarray = []
    with open(data_file_path, "r") as data_file:
        rawlinedata = [line.strip() for line in data_file]
        #print(rawlinedata)
    for entry in rawlinedata:
        if entry and entry[0] in allowedFirst:
            cleanedentry = getname(entry)
            returnarray.append(cleanedentry)
    return returnarray

def loaddatafromfile(data_file_path):
    returnarray = []
    with open(data_file_path, "r") as data_file:
        rawlinedata = [line.strip() for line in data_file]
        #print(rawlinedata)
    for entry in rawlinedata:
        if entry and entry[0] in allowedFirst:
            cleanedentry = getitemdictionary(entry)
            returnarray.append(cleanedentry)
    return returnarray

#cleaner
def getitemdictionary(rawitem):
    itemdictionary = {}
    brokenatnotes = rawitem.partition("|")
    #None of these check what's in the notes.
    if getname(brokenatnotes[0]):
        itemdictionary["name"] = getname(brokenatnotes[0])
    if getcontext(brokenatnotes[0]):
        itemdictionary["context"] = getcontext(brokenatnotes[0])
    if getstatus(brokenatnotes[0]):
        itemdictionary["status"] = getstatus(brokenatnotes[0])
    if getdays(brokenatnotes[0]):
        itemdictionary["days"] = getdays(brokenatnotes[0])
    #Takes the notes without examination. 
    if brokenatnotes[2]:
        itemdictionary["note"] = brokenatnotes[2].strip()
    #print(itemdictionary)
    return itemdictionary

def getname(rawstring):
    regexdefault = r"-( \[.*\] | )(.*?)[@#|(]"
    regexbujo = r"^([xX!><OaD\-\[?0123456789ø·•]*)\s(.*?)[@#|(]"
    match = re.search(regexdefault, rawstring)
    if match:
        name = match.group(2).strip()
    else:
        match = re.search(regexbujo, rawstring)
        if match:
            name = statuslookup(match.group(2))
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
        'D': "delegated",
        '-': "archived",
        '?': "needs research",
        '1': "1st priority",
        '2': "2nd priority",
        '3': "3rd priority",
    }.get(x, x)
#    }.get(x, "unknown mark")

def getstatus(rawstring):
    regexdefault = r"\[(.*)\]"
    regexbujo = r"^([xX!><Oa\-?0123456789ø·•]*)\s"
    match = re.search(regexdefault, rawstring)
    if match:
        status = statuslookup(match.group(1))
    else:
        match = re.search(regexbujo, rawstring)
        if match:
            status = statuslookup(match.group(1))
        else:
            status = ""
    return status
