---
layout: post
title:  "Writing a Parser - Getting Started"
date:   2018-02-10 08:07:01 -0600
tags: text, pvj
---

json and YAML are ugly. I want a simpler looking files, but maybe with still some rich content. Kinda like [ToDo.txt](https://github.com/todotxt), but I don't like that file format either.

- Step 1
  - open a very very simple file, clean it up line by line, use that to row_items array.
- Step 2
  - open file with more info per line, insert information into internal data structure

Handy Regex Links:
- <https://regex101.com/>

These files are so simple I don't really need a parser with a grammar, but that stuff is interesting:
- <https://github.com/antlr>
- <https://github.com/antlr/antlr4/blob/master/doc/python-target.md>
- <https://www.youtube.com/watch?v=Rhqk9HYiB7Q&ab_channel=TheCodingTrain>
- <https://www.youtube.com/watch?v=224plb3bCog&ab_channel=Computerphile>

## Step 1: Python
### Option 1
  {% highlight python %}
  with open('example_data/simplesthabits.txt', "r") as data_file:
      rawlinedata = data_file.readlines()
      print(rawlinedata)

  #cleaner
  def gethabitname(rawhabit):
      clean_name = rawhabit.rstrip()
      clean_name = clean_name.lstrip("- ")
      print("|" + clean_name + "|")
      return clean_name
{% endhighlight %}

### Option 2
{% highlight python %}
with open('example_data/simplesthabits.txt', "r") as data_file:
    rawlinedata = [line.strip() for line in data_file]
    print(rawlinedata)

#cleaner
def gethabitname(rawhabit):
    clean_name = rawhabit.lstrip("- ")
    print("|" + clean_name + "|")
    return clean_name
{% endhighlight %}
