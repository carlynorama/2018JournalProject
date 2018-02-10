#bulletjournalSVG.py

import datetime
import calendar


year = 2018
month = 2

viewBoxWidth = 2550
viewBoxHeight = 3300
horizonatal_offset = -150 # "min_x"
vertical_offset = 0 # "min_y"

radius = viewBoxHeight/80
centerX = 0
centerY = 0
day_ymargin = radius/4
outline_style_for_day = "fill:rgb(200,200,255);"
font_size_for_day = int(radius)
font_style_for_day = "font-family:\'Helvetica\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_day
font_size_for_month = int(2*radius)
font_style_for_month = "font-family:\'Helvetica\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_month

first_day = datetime.date(year, month, 1)
first_weekday = first_day.strftime("%w") #Sunday = 0
first_week_of_the_month = first_day.strftime("%U") #Sunday = 0
file_name = first_day.strftime("%Y%B")
month_name = first_day.strftime("%B, %Y")
day_range_of_the_month = calendar.monthrange(year,month)

days_of_the_week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

f = open('%s.svg' % file_name, 'w')
#print month_name
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
f.write('<svg width="100%%" height="100%%" viewBox="%s %s %s %s" xmlns="http://www.w3.org/2000/svg">\n' % (horizonatal_offset, vertical_offset, viewBoxWidth, viewBoxHeight))

f.write('\t<g transform="translate(%s, %s)" style="%s">\n' % ((radius*4), (viewBoxHeight/10), outline_style_for_day))
for x in range(0, day_range_of_the_month[1]):
    my_day = x+ 1
    my_date = datetime.date(year, month, my_day)
    my_weekday = int(my_date.strftime("%w")) #Sunday = 0
    my_week = int(int(my_date.strftime("%U")) - int(first_week_of_the_month))
    print("my day: {}, my week: {}, my day: {}".format(my_day, my_week, my_weekday))
    my_x = centerX
    my_date_x = my_x
    my_dayoftheweek_x = my_x - 3*font_size_for_day
    my_y = centerY + ((my_day) * ((radius*2)+day_ymargin))
    my_date_y = my_y #- font_size_for_day
    my_date_text = my_day
    my_dayoftheweek_text = days_of_the_week[my_weekday]
    f.write('\t<circle cx="%s" cy="%s" r="%s"/>\n' % (my_x, my_y, radius))
    f.write('\t<text x="%s" y="%s" style="%s" dominant-baseline="central">%s</text>\n' % (my_dayoftheweek_x, my_date_y, font_style_for_day, my_dayoftheweek_text))
    f.write('\t<text x="%s" y="%s" style="%s" text-anchor="middle" dominant-baseline="central">%s</text>\n' % (my_date_x, my_date_y, font_style_for_day, my_date_text))
f.write('\t</g>\n')


f.write('\t<g transform="translate(%s, %s)" style="%s">\n' % ((radius), (viewBoxHeight/12), font_style_for_month))
f.write('\t\t<text>%s</text>\n' % month_name)
f.write('\t</g>\n')

f.write('</svg>')
f.close()
