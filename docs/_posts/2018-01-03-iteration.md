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
let days_of_the_week = ['M', 'T', 'W', 'Th', 'F', 'Sa', 'Su']
let this_weeks_dates = [ 16, 17, 18, 19, 20, 21, 22]


//old school
for (var d = 0; d < 7; d++) {
    console.log(days_of_the_week[d]);
}

//for the length of the array
for (var d = 0; d < days_of_the_week.length; d++) {
    console.log(days_of_the_week[d]);
}

//dual array-ish
for (var d = 0; d < days_of_the_week.length; d++) {
    let message = `The ${this_weeks_dates[d]} is a ${days_of_the_week[d]}`
    console.log(message);
}

//start late, skip around
for (var d = 1; d < days_of_the_week.length; d +=2) {
    let message = `The ${this_weeks_dates[d]} is a ${days_of_the_week[d]}`
    console.log(message);
}

//apparently ad hoc order but will do all of them
for (d in days_of_the_week) {
  console.log(days_of_the_week[d]);
}

// like for in but will get them in order for sure
// const or let for "day" depending on whether you change it
for (const day of days_of_the_week) {
  console.log(day);
}

//get them in order and can perform a function/closure
function printMessage(message) {
    console.log(message)
}
days_of_the_week.forEach(printMessage)

//define add a little conditional with iteration
days_of_the_week.forEach(function(array_element, index) {
  return index > 2 ? printMessage(array_element) : null;
})

//over a string
day_name = "Monday"
for (let c of day_name) {
  console.log(c);
}

//"Zip" two arrays into a Map
var week_map = this_weeks_dates.map(function(array_element, index) {
  return [array_element, days_of_the_week[index]];
});

console.log(week_map)

//Using new "entries" feature. Like enumerate
for (const [key, value] of days_of_the_week.entries()) {
  console.log(`${key} ${value}`); // "a 5", "b 7", "c 9"
}

//Treating the array as an Object
Object.entries(days_of_the_week).forEach(([key, value]) => {
console.log(`${key} ${value}`); // "a 5", "b 7", "c 9"
});

//This does not work?
days_of_the_week.entries().forEach(([key, value]) => {
console.log(`${key} ${value}`); // "a 5", "b 7", "c 9"
});

//https://www.htmlgoodies.com/html5/javascript/getting-fancy-with-the-javascript-for-loop.html

//Dual conditions: Start at 0 end at Wednesday
for (var i=0; i<days_of_the_week.length && days_of_the_week[i] != 'W'; i++) {
  console.log( 'day #' + (i+1) + ' is a ' + days_of_the_week[i])
}

//Two Incrementors
for(var a = 1, b = 10; a*b; a++, b--) {
  console.log(`${a} ${b}`);
}

//variable declarations galore.
for (var i=0, len=days_of_the_week.length, text="You've got "+len+" days:\n"; i<len; i++) {
    text += days_of_the_week[i] + "\n";
}
console.log(text) //text now persists after the for loop. 
{% endhighlight %}
