//parsing functions
const fs = require('fs')



const special="-#|[]()@"
const allowedFirst="xX!><Oa-D?0123456789ø·•"

//module.exports.loaddatafromfile = function(data_file_path) {
function loaddatafromfile(data_file_path, callback) {
    var bufferString, bufferStringSplit;
    fs.readFile(data_file_path, function(err, data) {
      if (err) throw err;;
      bufferString = data.toString();
      bufferStringSplit = bufferString.split('\n');
      callback(bufferStringSplit);
    });
    //return bufferStringSplit
    //return data_file_path
}

//Expose API
exports.hello="hello"
exports.loaddatafromfile = loaddatafromfile;

//    function loaddatafromfile(data_file_path) {
//     var bufferString, bufferStringSplit;
//     fs.readFile(data_file_path, function(err, data) {
//       bufferString = data.toString();
//       bufferStringSplit = bufferString.split('\n');
//     });
//     return bufferStringSplit
//         //print(linedata)
// }

// function getnames(linedata):
//     returnarray = []
//     for entry in linedata:
//         if entry and entry[0] in allowedFirst:
//             cleanedentry = getname(entry)
//             returnarray.append(cleanedentry)
//     return returnarray
// }
//
// function hassublist(linedata) {
//     returnbool = 0
//     myarray = getsublists(linedata)
//     if myarray:
//         returnbool = 1
//     return returnbool
// }
//
// function getsublists(linedata) {
//     returnarray = []
//     header = ""
//     for entry in linedata:
//         if entry and entry[0] == "#":
//             header = getheader(entry)
//             returnarray.append(header)
//     return returnarray
// }
//
// function getitems(linedata) {
//     returnarray = []
//     header = ""
//     for entry in linedata:
//         if entry:
//             if entry[0] in allowedFirst:
//                 cleanedentry = getitemdictionary(entry)
//                 if header:
//                     cleanedentry["sublist"] = header
//                 returnarray.append(cleanedentry)
//             if entry[0] == "#":
//                 header = getheader(entry)
//     return returnarray
// }
//
// function getitemdictionary(rawitem) {
//     itemdictionary = {}
//     brokenatnotes = rawitem.partition("|")
//     //None of these check what's in the notes.
//     if getname(brokenatnotes[0]):
//         itemdictionary["name"] = getname(brokenatnotes[0])
//     if getcontext(brokenatnotes[0]):
//         itemdictionary["context"] = getcontext(brokenatnotes[0])
//     if getstatus(brokenatnotes[0]):
//         itemdictionary["status"] = getstatus(brokenatnotes[0])
//     if getdays(brokenatnotes[0]):
//         itemdictionary["days"] = getdays(brokenatnotes[0])
//     //#Takes the notes without examination.
//     if brokenatnotes[2]:
//         itemdictionary["note"] = brokenatnotes[2].strip()
//     //#print(itemdictionary)
//     return itemdictionary
// }
//
// function getheader(rawstring) {
//     regex = r"####(.*?)####"
//     match = re.search(regex, rawstring)
//     if match:
//         days = match.group(1).strip()
//     else:
//         days = ""
//     return days
// }
//
// function getname(rawstring) {
//     regexdefault = r"-( \[.*\] | )(.*?)[@#|(]"
//     regexbujo = r"^([xX!><OaD\-\[?0123456789ø·•]*)\s(.*?)[@#|(]"
//     match = re.search(regexdefault, rawstring)
//     if match:
//         name = match.group(2).strip()
//     else:
//         match = re.search(regexbujo, rawstring)
//         if match:
//             name = statuslookup(match.group(2))
//         else:
//             name = ""
//     return name
// }
//
// function getnote(rawstring) {
//     note = rawstring.partition("|")[2].strip()
//     return note
// }
//
// function getdays(rawstring) {
//     regex = r"\(([^()]*)\)"
//     match = re.search(regex, rawstring)
//     if match:
//         days = match.group(1)
//     else:
//         days = ""
//     return days
// }
//
// function getcontext(rawstring) {
//     regex = r"(@[^\s]+)\s"
//     match = re.search(regex, rawstring)
//     if match:
//         context = match.group(0)
//     else:
//         context = ""
//     return context
// }
//
// function statuslookup(x) {
//     return {
//         ' ': "unmarked",
//         'x': "done",
//         'X': "done",
//         '!': "urgent",
//         '>': "migrated",
//         '<': "scheduled",
//         'O': "event",
//         'a': "assigned",
//         'D': "delegated",
//         '-': "archived",
//         '?': "needs research",
//         '1': "1st priority",
//         '2': "2nd priority",
//         '3': "3rd priority",
//     }.get(x, x)
// //#    }.get(x, "unknown mark")
// }
//
// function getstatus(rawstring) {
//     regexdefault = r"\[(.*)\]"
//     regexbujo = r"^([xX!><Oa\-?0123456789ø·•]*)\s"
//     match = re.search(regexdefault, rawstring)
//     if match:
//         status = statuslookup(match.group(1))
//     else:
//         match = re.search(regexbujo, rawstring)
//         if match:
//             status = statuslookup(match.group(1))
//         else:
//             status = ""
//     return status
//   }
