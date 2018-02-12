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

function getnames(linedata, callback) {
    returnarray = [];
    for (const entry of linedata) {
      console.log(entry);
      try {
          if(entry == "") throw "empty";
          if (allowedFirst.includes(entry.charAt(0))) {
            cleanedentry = getname(entry)
            returnarray.push(cleanedentry)
          }
      }
      catch(err) {
          console.log("Line doesn't have name b/c", err);
      }
    }
    callback(returnarray);
}



//Expose API
exports.hello="hello";
exports.loaddatafromfile = loaddatafromfile;
exports.getnames = getnames;




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
function getname(rawstring) {
    let name = "";
    const regex = /- (.*?)([#|[(@]|$)/g;
    const regexdefault = /-( \[.*\] | )(.*?)([@#|(]|$)/g;
    const regexbujo = /^([xX!><OaD\-\[?0123456789ø·•]*)\s(.*?)([#|[(@]|$)/g;
    const str = rawstring;
    var match = regexdefault.exec(str);
    if (match) {
      //console.log(match);
      name = match[2];
    } else {
      match = regexbujo.exec(str);
      if (match) {
        name = match[2];
      }
    }
    return name
}
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
