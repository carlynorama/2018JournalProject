---
layout: post
title:  "Date Handling"
date:   2018-01-03 08:07:01 -0600
tags: pvj
---

## Python

imports

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

.strftime to get date in different formats

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



{% highlight python %}



## Javascript

{% highlight javascript %}

{% endhighlight %}
