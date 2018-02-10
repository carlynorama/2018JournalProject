---
layout: post
title:  "Parsing JSON"
date:   2018-02-09 08:07:01 -0600
tags: pvj, JSON
---


## Python

most of this came [from MakeUseOf](https://www.makeuseof.com/tag/json-python-parsing-simple-guide/)

### Loading Data from File
{% highlight python %}
import json
from pprint import pprint

with open('example_data/habits.json', "r") as data_file:
    habitData = json.load(data_file)

pprint(habitData)

# or
for x in habitData:
	print(x)

{% endhighlight %}

### Parsing Data
{% highlight python %}
for x in loaded_json:
	print("%s: %d" % (x, loaded_json[x]))

{% endhighlight %}

## Javascript

### Loading Data from File
Very good tutorial on different ways to bring [JSON data into Javascript](http://stackabuse.com/reading-and-writing-json-files-with-node-js/) project on StackAbuse

{% highlight javascript %}
#### Synchronously
{% highlight javascript %}
const fs = require('fs');
let rawdata = fs.readFileSync('student.json');  
let student = JSON.parse(rawdata);  
console.log(student);
{% endhighlight %}

#### Asynchronously
{% highlight javascript %}
const fs = require('fs');
fs.readFile('student.json', (err, data) => {  
    if (err) throw err;
    let student = JSON.parse(data);
    console.log(student);
});
console.log('This is after the read call');  
{% endhighlight %}

#### Synchronously with require
{% highlight javascript %}
//synchronously w/ require
let jsonData = require('./student.json');
console.log(jsonData);  

{% endhighlight %}

### Using JSON

Once the data is in [this tutorial](https://www.codementor.io/codementorteam/how-to-use-json-files-in-node-js-85hndqt32) helped me use it.
