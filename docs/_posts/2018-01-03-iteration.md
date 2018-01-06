---
layout: post
title:  "Itteration"
date:   2018-01-03 08:04:01 -0600
tags: pvj
---

## Python

{% highlight python %}
days_of_the_week = ['M', 'T', 'W', 'Th', 'F', 'Sa', 'Su']
this_weeks_dates = [ 16, 17, 18, 19, 20, 21, 22]

print "for i in array"
for i in days_of_the_week:
  print i

print "for i in defined range"
for i in range(0, 7):
    print days_of_the_week[i]

#for super big ranges, python 2.7 not 3
for i in xrange(0, 7):
    print days_of_the_week[i]

print "for i in defined range, every other"
for i in range(0, 7, 2):
    print days_of_the_week[i]

print "for i in range by length of array"
for i in range(len(days_of_the_week)):
     print days_of_the_week[i]

print "enumerate for when need index, too"
for num, day in enumerate(days_of_the_week):
    print("Day # {}: {}".format(num, day))

print "enumerate, dual array with one index"
for d, day in enumerate(days_of_the_week):
    date = this_weeks_dates[d]
    print("The {} is a {}".format(date, day))

print "zip for dual array"
for date, day in zip(this_weeks_dates, days_of_the_week):
    print("The {} is a {}".format(date, day))

string = "Monday"
for c in string:
    print c

month = [ days_of_the_week, days_of_the_week, days_of_the_week, days_of_the_week]
print "month"
for week in month:
    print "next week"
    for day in week:
        print day


{% endhighlight %}

## Javascript
{% highlight javascript %}
let centerX = 15
let centerY = 15
let radius = 10
let style = "fill:rgb(200,200,255);"

let message = `\t<circle cx="${centerX+(x*((radius*2)+5))}" cy="${centerY}" r="${radius}" style="${style}"/>\n`
console.log(message)
{% endhighlight %}
