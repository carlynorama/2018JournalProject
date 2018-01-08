---
layout: post
title:  "Date Handling"
date:   2018-01-03 08:07:01 -0600
tags: pvj
---

## Python

import [datetime] and [calendar]

[datetime]: https://docs.python.org/2/library/datetime.html
[calendar]: https://docs.python.org/2/library/calendar.html

{% highlight python %}
import datetime
import calendar
{% endhighlight %}

set up the basics

{% highlight python %}
year = 2018
month = 4 #1 thru 12
day = 23
number_of_days = 4
day_range = range(0,number_of_days)
start_date = datetime.date(year, month, day)
end_date = start_date + datetime.timedelta(days=number_of_days)
number_of_days2 = end_date - start_date
print number_of_days2
{% endhighlight %}

[.strftime] to get date in different formats

[.strftime]: (http://strftime.org/)

{% highlight python %}
day_as_date = datetime.date(year, month, day)
print day_as_date

weekday = day_as_date.strftime("%w")
print weekday

week_of_the_month = day_as_date.strftime("%U")
print weekday

month_name = day_as_date.strftime("%B, %Y")
print month_name

day_of_the_week_text = day_as_date.strftime("%A")
day_date_text = day_as_date.strftime("%b %-d")
day_name = day_as_date.strftime("%b_%-d")
print day_of_the_week_text, day_date_text, day_name

{% endhighlight %}

`calendar` for date ranges, iterators, text calendars

{% highlight python %}
day_range_of_the_month = calendar.monthrange(year,month)
print day_range_of_the_month

for name in calendar.month_name:
    print name

#print mini text calendars
calendar.prmonth(year, month)
print(calendar.weekheader(5))
calendar.prcal(2018)

print "Loops with calendar iterators"
calendar.setfirstweekday(calendar.SATURDAY)
my_cal = calendar.Calendar(6)
for w in my_cal.monthdatescalendar(year, month):
    for d in w:
        print(d)
my_cal = calendar.Calendar(6)
for w in my_cal.monthdays2calendar(year, month):
    for d in w:
        print(d)

{% endhighlight %}

using `calendar` in loops

{% highlight python %}
print "Loops with calendar iterators"
calendar.setfirstweekday(calendar.SATURDAY)

my_cal = calendar.Calendar(6)
for w in my_cal.monthdatescalendar(year, month):
    for d in w:
        print(d)

my_cal = calendar.Calendar(6)
for w in my_cal.monthdays2calendar(year, month):
    for d in w:
        print(d)
{% endhighlight %}

## Javascript

Examples use both internal Javascript [Date] object] and [Moment.js] for [easier formatting].

[Date]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date
[Moment.js]: https://momentjs.com/
[easier formatting]: https://momentjs.com/docs/#/displaying/


### Built in functions

{% highlight javascript %}
let today = new Date(); //no input = curent datetime
let day_tested = new Date(1515267948639); //date in millis
let this_millis = new Date().getTime();
let o_day = new Date(January 1, 1970); //anything recognizable with Date.parse()
let foo_day = new Date(1983, 12, 16, 8, 23, 12, 532); //year, month, day, hours, minutes, seconds, milliseconds

let day_of_the_month = today.getDate();
let day_of_the_week_num = today.getDay()
let year = today.getFullYear();
let month = today.getMonth();  // 0 to 11, 12 is January of next year
let third_of_this_month = today.setDate(3); //sets the date's day to 3

let options = {
    weekday: 'long', year: 'numeric', month: 'short',
    day: 'numeric', hour: '2-digit', minute: '2-digit'
  };

let message = today.toLocaleTimeString('en-us', options);
console.log(message)
{% endhighlight %}

### Moment.js functions

#### Set up a moment

{% highlight javascript %}
let moment = require('moment');
let new_date = Date();
let mday = moment(new_date);
{% endhighlight %}

#### Getting formats out

{% highlight javascript %}
let weekday_as_number = mday.format('d')
let weekday_as_two_letter_text = mday.format('dd')
let zero_led_date = mday.format('DD') // zero leading day of the month
let week_of_the_month = mday.format('w')
let full_month_full_year = mday.format("MMMM, YYYY")
let last_day_of_the_month = mday.daysInMonth()
{% endhighlight %}

#### Manipulating time

Using a momentjs object , it's force create new moment instead of just passing an object reference.

{% highlight javascript %}
//seven days from now

let next_week = moment(mday.add(7, 'days'));
let next_week2 = moment(mday.add(7, 'd'));

//3 days from now next month
let added_date = moment(mday.add(3, 'days').add(1, 'months')); // with chaining
let added_date2 = moment(mday.add({days:3,months:1})); // with object literal

//snap to beginning, there is also .endOf
let first_day_of_year = moment(mday.startOf('year'));    // set to January 1st, 12:00 am this year
let first_day_of_month = moment(mday.startOf('month'));   // set to the first of this month, 12:00 am
let first_day_of_quarter =moment(mday.startOf('quarter'));  // set to the beginning of the current quarter, 1st day of months, 12:00 am
let first_day_of_week = moment(mday.startOf('week'));    // set to the first day of this week, 12:00 am
let first_day_of_weekISO = moment(mday.startOf('isoWeek'));
{% endhighlight %}

#### Iterating over a set of days

{% highlight javascript %}
//https://stackoverflow.com/questions/17163809/iterate-through-a-range-of-dates-in-nodejs
var a = moment('2013-01-01');
var b = moment('2013-06-01');

// If you want an exclusive end date (half-open interval)
for (var m = moment(a); m.isBefore(b); m.add(1, 'days')) {
  console.log(m.format('YYYY-MM-DD'));
}

// If you want an inclusive end date (fully-closed interval)
for (var m = moment(a); m.diff(b, 'days') <= 0; m.add(1, 'days')) {
  console.log(m.format('YYYY-MM-DD'));
}
{% endhighlight %}
