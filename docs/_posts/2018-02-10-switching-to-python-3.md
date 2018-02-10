---
layout: post
title:  "Switching to Python 3"
date:   2018-02-10 09:07:01 -0600
tags: python
---

## Up and running

Both [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos) and [The Hitch-Hikers Guide to Python](http://docs.python-guide.org/en/latest/starting/install3/osx/) had complete instructions.

If not already done:

- Install/Update Xcode Command line tools
  - `xcode-select --install`
- Install homebrew
  - `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

{% highlight shell %}
brew install python3
python3 myscript.py
{% endhighlight %}

I this project for now is not using a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref).

## What doesn't run

### habit_weekly_grid.py
no problems

### weekly_layout_1.py
no problems

### monthly_bullets.py

#### error message

{% highlight shell%}
my day: %s, my week: %s, my day: %s
Traceback (most recent call last):
  File "monthy_bullets.py", line 46, in <module>
    print ("my day: %s, my week: %s, my day: %s") % (my_day, my_week, my_weekday)
TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple'
{% endhighlight %}

#### the fix
{% highlight python%}
    print("my day: {}, my week: {}, my day: {}".format(my_day, my_week, my_weekday))
{% endhighlight %}
