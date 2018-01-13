---
layout: post
title:  "Using Jekyll to generate SVG To-Do lists"
date:   2018-01-12 08:03:01 -0600
tags: SVG jekyll liquid
---

My goal wasn't to generate SVG's with Jekyll, but apparently you can. I did an example over at the [Tuesday Sweep][1]. Nothing fancy yet, but I enjoyed the cross polination. When I pull in data here, I'll try to do it from similarly formatted YAML files.  

### Step 1: Create a YML file for the list

this should be in `_data` directory in the jekyll source folder.  

{% highlight YML %}
group_title: Basic Weekly Checklist
bwc:

- title: Thing 1
  short_description: description 1

- title: Thing 2
  short_description: description 2

- title: Thing N
  short_description: description N
{% endhighlight %}

### Step 2: Create a layout

Called `checklist.html` in the `_layouts` folder.

{% highlight HTML%}
<!DOCTYPE html>
<html>
  <body>
    <svg width="100%" height="100%" viewBox="0 0 2500 3300" xmlns="http://www.w3.org/2000/svg">
      <g id="checklist" transform="translate(300, 300)" style="font-family:'Helvetica';font-size:75px;fill:rgb(102,102,102);">
        {{ content }}
      </g>
    </svg>
  </body>
</html>
{% endhighlight %}

### Step 3: Create a post

The math for the for loop was found at the [Liquid official Math docs][2] and a [HowTo posted by a community member][3].

{% highlight Liquid %}
---
collection: sweep
layout: checklist
name: my_checklist.md
title: Basic Checklist
---
<text x="0" y="0">{{page.title}} for  {{ "now" | date: "%Y-%m-%d %H:%M" }}</text>
<g id="list" transform="translate(0, 150)">
{% assign todolist_count = '' %}
{% for item in site.data.basic_weekly_checklist.bwc %}
  <rect x="30" y="{{ todolist_count.size | times: 150.0 | minus: 65}}" width="75" height="75" style="fill:rgb(255,255,255);stroke:rgb(153,153,153);stroke-width:2" />
  <text x="150" y="{{ todolist_count.size | times: 150.0 }}">{{ item.title }}</text>
  {% assign todolist_count = todolist_count | append: 'x' %}
{% endfor %}
</g>
{% endhighlight %}


[1]: https://carlynorama.github.io/tuesday/sweep/printable_checklist.html
[2]: https://help.shopify.com/themes/liquid/filters/math-filters
[3]: https://ecommerce.shopify.com/c/ecommerce-design/t/how-to-increment-count-in-liquid-209692
