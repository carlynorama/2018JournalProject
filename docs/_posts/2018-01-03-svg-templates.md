---
layout: post
title:  "SVG Templates"
date:   2018-01-03 08:06:01 -0600
tags: SVG
---

For copy-pasting ease. Not al SVG rendering applications work with CSS styling.

## Shapes

{% highlight SVG %}

<circle cx=" " cy=" " r=" "/>
<ellipse cx=" " cy=" " rx=" " ry=" "/>
(stroke=" " fill=" " stroke-width=" "  or style="stroke: ;fill: ;stroke-width: ")

<rect x=" " y=" " width=" " height=" "/>
<rect x=" " y=" " rx=" " ry=" " width=" " height=" "/>
(stroke=" " fill=" " stroke-width=" "  or style="stroke: ;fill: ;stroke-width: ")


<line x1=" " x2=" " y1=" " y2=" "/>
(stroke=" " stroke-width=" "  or or style="stroke: ;stroke-width: ")

<!-- commas for x y coord pairs aren't strictly necessary-->
<polyline points="0,40 40,40 40,80 80,80 80,120 120,120 120,160"/>
<polygon points="200,10 250,190 160,210"/>
(stroke=" " fill=" " stroke-width=" "  or style="stroke: ;fill: ;stroke-width: ")

<path d="M20,230 Q40,205 50,230 T90,230" />
(stroke=" " fill=" " stroke-width=" "  or style="stroke: ;fill: ;stroke-width: ")

{% endhighlight %}

## Text

{% highlight SVG %}
<text x=" " y=" ">  </text>

<text x=" " y=" " style=" ">Heading:
  <tspan x=" " y=" " style=" ">First line.</tspan>
  <tspan x=" " y=" " style=" ">Second line.</tspan>
</text>

style="font-family:'Helvetica';font-size: px;fill:rgb( , , );"
(fill=" " or style="stroke: ;fill: ;stroke-width: ")
(font='' font-family='' font-size='' font-weight='' font-size-adjust='' font-stretch='' font-style='' font-variant='')

{% endhighlight %}


## Groups & Transformations

Groups can also have style attributes, in fact probably should whenever possible to make for the smallest/most readable file.

### Groups

{% highlight SVG %}
<g id=" " width=" " height=" " transform="translate( , )">
  <item></item>
</g>

<g id=" " width=" " height=" " transform="translate( , )">
  <g id=" " class=" " transform="translate( , )">
    <item></item>
  </g>
</g>

{% endhighlight %}

### Transforms

{% highlight SVG %}
<g transform="matrix(a,b,c,d,e,f)">
  <line x1=" " y1=" " x2=" " y2=" "/>
</g>
<!-- New coordinate system
     x1 = a * 10 + c * 20 + e   | x2 = a * 30 + c * 40 + e
     y1 = b * 10 + d * 20 + f   | y2 = b * 30 + d * 40 + f
-->
transform="translate(<x> [<y>])" <!-- matrix(1 0 0 1 x y) -->
transform="scale(<x> [<y>])"  <!-- matrix(x 0 0 y 0 0) -->
transform="rotate(<a> [<x> <y>])" <!-- translate(<x>, <y>) rotate(<a>) translate(-<x>, -<y>) -->
transform="skewX(<a>)"
transform="rskewY(<a>)"

{% endhighlight %}
