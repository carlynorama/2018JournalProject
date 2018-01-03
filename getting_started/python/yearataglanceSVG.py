#calendarSVG.py

import datetime
import calendar


year = 2018

viewBoxWidth = 2550
viewBoxHeight = 3300
radius = viewBoxWidth/75
day_xmargin = radius
day_ymargin = radius
outline_style_for_day = "fill:rgb(200,200,255);"
font_size_for_day = int(radius)
font_style_for_day = "font-family:\'Helvetica\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_day
font_size_for_month = int(radius)*2
font_style_for_month = "font-family:\'Helvetica\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_month

file_name = year
days_of_the_week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']


f = open('%s.svg' % file_name, 'w')
#print month_name
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')



f.write('<svg width="100%%" height="100%%" viewBox="0 0 %s %s" xmlns="http://www.w3.org/2000/svg">\n' % (viewBoxWidth, viewBoxHeight))
f.write(' <style>/* <![CDATA[ */circle{%s}/* ]]> */</style>\n' % outline_style_for_day)
f.write('\t<g id="calendar" transform="translate(%s, %s)">\n' % (0, 0))

for m in range(0, 12):
    month = m+1
    month_x_offset = (month-1)%3 * (viewBoxWidth/3)
    month_y_offset = (month-1)/3 * (viewBoxHeight/4)
    print('%s: (%s, %s)' % (month, month_x_offset, month_y_offset))
    first_day = datetime.date(year, month, 1)
    month_title = first_day.strftime("%B, %Y")
    month_name = first_day.strftime("%B")
    first_weekday = first_day.strftime("%w") #Sunday = 0
    first_week_of_the_month = first_day.strftime("%U") #Sunday = 0
    day_range_of_the_month = calendar.monthrange(year,month)
    f.write('\t<g id="%s" transform="translate(%s, %s)">\n' % (month_name, month_x_offset, month_y_offset))
    f.write('\t<text x="%s" y="%s" style="%s" text-anchor="middle" dominant-baseline="central">%s</text>\n' % (0, 0, font_style_for_month, month_title))
    f.write('\t<g id="%s_weekbar" transform="translate(%s, %s)" style="%s" text-anchor="middle" dominant-baseline="central">\n' % (month_name, 0, font_size_for_month*1.5, font_style_for_day,))
    for d in range(0, 7):
        my_x = (d * ((radius*2)+day_xmargin))
        my_y = 0
        f.write('\t<text x="%s" y="%s">%s</text>\n' % (my_x, my_y, days_of_the_week[d]))
    f.write('\t</g>\n')
    f.write('\t<g id="%s_days" transform="translate(%s, %s)" text-anchor="middle" dominant-baseline="central" style="%s" >\n' % (month_name, 0, font_size_for_month*1.5, font_style_for_day))
    for x in range(0, day_range_of_the_month[1]):
        my_date = datetime.date(year, month, x+1)
        my_weekday = int(my_date.strftime("%w")) #Sunday = 0
        my_week = int(int(my_date.strftime("%U")) - int(first_week_of_the_month)) + 1
        #print ("my day: %s, my week: %s, my day: %s") % (x+1, my_week, my_weekday)
        my_x = (my_weekday * ((radius*2)+day_xmargin))
        my_date_x = my_x
        my_y = (my_week * ((radius*2)+day_ymargin))
        my_date_y = my_y #- font_size_for_day
        f.write('\t<circle cx="%s" cy="%s" r="%s"/>\n' % (my_x, my_y, radius))
        f.write('\t<text x="%s" y="%s">%s</text>\n' % (my_date_x, my_date_y, my_date.strftime("%d")))
    f.write('\t</g>\n')
    f.write('\t</g>\n')
f.write('\t</g>\n')


#f.write('\t<g transform="translate(%s, %s)" style="%s">\n' % ((radius/2), (viewBoxHeight/8), font_style_for_month))
#f.write('\t\t<text>%s</text>\n' % month_name)
#f.write('\t</g>\n')

f.write('</svg>')
f.close()
