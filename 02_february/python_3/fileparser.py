# What the heck

item_line_start = "- "

def loaddatafromfile(data_file_path):
    with open(data_file_path, "r") as data_file:
        rawlinedata = [line.strip() for line in data_file]
        print(rawlinedata)
        returnarray = []
        for entry in rawlinedata:
            cleanedentry = getitemname(entry)
            returnarray.append(cleanedentry)
        return returnarray

#cleaner
def getitemname(rawitem):
    clean_name = rawitem.lstrip(item_line_start)
    print("|" + clean_name + "|")
    return clean_name
