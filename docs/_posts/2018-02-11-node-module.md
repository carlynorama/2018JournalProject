---
layout: post
title:  "Node module"
date:   2018-02-11 10:07:01 -0600
tags: node
---

in module
{highlight javascript}
module.exports.hello="hello"

module.exports.loaddatafromfile = function(data_file_path) {
    return data_file_path
}
{end highlight}

in file
{highlight javascript}
const jparser = require('./jparser.js');
const input_file_name = "./example_data/simplehabits.txt"
console.log(jparser.hello)
const linedata = jparser.loaddatafromfile(input_file_name)
console.log(linedata)
{end highlight}

//Expose API
exports.hello="hello"
exports.loaddatafromfile = loaddatafromfile;
