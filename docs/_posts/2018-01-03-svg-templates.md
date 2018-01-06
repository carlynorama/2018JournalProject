---
layout: post
title:  "SVG Templates"
date:   2018-01-03 08:06:01 -0600
tags: SVG
---

For copy-pasting ease. Not al SVG rendering applications work with CSS styling.

## File Essentials

Letter sized, landscape orientation.

{% highlight SVG %}
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="100%" height="100%" viewBox="0 0 3300 2550" xmlns="http://www.w3.org/2000/svg">

</svg>
{% endhighlight %}

## Shapes

{% highlight SVG %}

<circle cx=" " cy=" " r=" "/>
<ellipse cx=" " cy=" " rx=" " ry=" "/>

<rect x=" " y=" " width=" " height=" "/>
<rect x=" " y=" " rx=" " ry=" " width=" " height=" "/>

<line x1=" " x2=" " y1=" " y2=" "/>

<!-- commas for x y coord pairs aren't strictly necessary-->
<polyline points="0,40 40,40 40,80 80,80 80,120 120,120 120,160"/>
<polygon points="200,10 250,190 160,210"/>

<path d="M20,230 Q40,205 50,230 T90,230" />

{% endhighlight %}

Common attributes
- stroke
- fill
- stroke-width
- stroke-opacity
- fill-opacity

Examples
`<circle cx="100" cy="100" r="100" fill="#666" stroke="green" stroke-width="10"/>`
`<line x1="15" y1="15" x2="15" y2="185" style="stroke:rgb(153,153,153);stroke-width:2" />`

## Text

{% highlight SVG %}
<text x=" " y=" ">  </text>

<text x=" " y=" " style=" ">Heading:
  <tspan x=" " y=" " style=" ">First line.</tspan>
  <tspan x=" " y=" " style=" ">Second line.</tspan>
</text>

{% endhighlight %}

Text specific attributes in addition to fill, etc.

- font-family=' ' | font-family: ;
- font-size=' '
- font-weight=' '
- font-size-adjust=' '
- font-stretch=' '
- font-style=' '
- font-variant=' '
- kerning: hkern, vkern
- letter-spacing
- text-anchor=
- dominant-baseline=" "
- text-decoration=" "

Examples
`<text x="30" y="108" text-anchor="end" dominant-baseline="middle" style="font-family:"Times New Roman",Times,serif;font-size:54px;fill:rgb(102,102,102);" >Jan 3</text>`



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
