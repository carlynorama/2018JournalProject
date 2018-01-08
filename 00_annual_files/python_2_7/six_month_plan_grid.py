#yearataglanceSVG.py

import datetime
import calendar


year = 2018

viewBoxWidth = 3300
viewBoxHeight = 2550
calendarWidth = 2900
calendarHeight = 2100

radius = calendarWidth/((6*7)*2.5)
day_xmargin = radius/3
day_ymargin = radius/3
outline_style_for_day = "fill:rgb(220,230,255);"
divider_line_style = "stroke:rgb(153,153,153);stroke-width:2"
font_size_for_day = int(radius)
font_style_for_day = "font-family:\'Helvetica\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_day
font_style_for_days_of_week = "font-family:\'Helvetica\';font-weight=\'bold\';font-size:%spx;fill:rgb(51,51,51);" % font_size_for_day
font_size_for_month = int(radius)*2
font_style_for_month = "font-family:\'Futura\', \'Helvetica\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_month
font_size_for_title = int(radius)*4
font_style_for_title = "font-family:\'Futura\', \'Helvetica\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_title

content_x_offset = 75
content_y_offset = 2 * viewBoxHeight / 15
title_x_offset = content_x_offset
title_y_offset = content_y_offset - (font_size_for_title*1.5)

file_name = "%s_sixmo_pygen" % year
page_title = "Future Planning - %s" % year

month_range = range(0,6)

days_of_the_week = ['S', 'M', 'T', 'W', 'T', 'F', 'S']

f = open('%s.svg' % file_name, 'w')
#print month_name
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')

f.write('<svg width="100%%" height="100%%" viewBox="0 0 %s %s" xmlns="http://www.w3.org/2000/svg">\n' % (viewBoxWidth, viewBoxHeight))
f.write(' <style>/* <![CDATA[ */circle{%s}/* ]]> */</style>\n' % outline_style_for_day)

f.write('\t<g id="page_title" transform="translate(%s, %s)">\n' % (title_x_offset, title_y_offset))
f.write('\t\t<text x="%s" y="%s" style="%s" text-anchor="left">%s</text>\n' % (0, 0, font_style_for_title, page_title))
f.write('\t\t</g>\n') # end page_title

f.write('<g id="calendar" width="%s" height="%s" transform="translate(%s, %s)">\n' % (calendarWidth, calendarHeight, content_x_offset, content_y_offset))
for m in month_range:
    month = m+1
    month_x_offset = (month-1)%6 * (calendarWidth/6 + (2*radius))
    left_margin = radius
    #month_y_offset = (month-1)/3 * (calendarHeight/4 + (2*radius))
    #print('%s: (%s, %s)' % (month, month_x_offset, month_y_offset))
    first_day = datetime.date(year, month, 1)
    month_title = first_day.strftime("%B")
    month_name = first_day.strftime("%B")
    first_weekday = first_day.strftime("%w") #Sunday = 0
    first_week_of_the_month = first_day.strftime("%U") #Sunday = 0
    day_range_of_the_month = calendar.monthrange(year,month)
    f.write('\t\t<g id="%s" transform="translate(%s, %s)">\n' % (month_name, month_x_offset, 0))
    f.write('\t\t\t<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />\n' % (0, 0, 0, calendarHeight, divider_line_style))
    print('%s line: (%s, %s) to (%s, %s)' % (month, month_x_offset + left_margin, 0, month_x_offset, calendarHeight))
    f.write('\t\t\t<text x="%s" y="%s" style="%s" text-anchor="left">%s</text>\n' % (0+left_margin, font_size_for_month, font_style_for_month, month_title))
    f.write('\t\t\t<g id="minical" transform="translate(%s, %s)" text-anchor="middle">\n' % (0, font_size_for_month*3))
    f.write('\t\t\t\t<g id="%s_weekbar" transform="translate(%s, %s)" style="%s" text-anchor="middle">\n' % (month_name, 0, 0, font_style_for_days_of_week))
    for d in range(0, 7):
        my_x = (d * ((radius*2)+day_xmargin)) + radius + left_margin
        my_y = 0
        f.write('\t\t\t\t\t<text x="%s" y="%s">%s</text>\n' % (my_x, my_y, days_of_the_week[d]))
    f.write('\t\t\t\t</g>\n') # end month_weekbar
    f.write('\t\t\t\t<g id="%s_days" transform="translate(%s, %s)" text-anchor="middle" dominant-baseline="central" style="%s" >\n' % (month_name, 0, 0, font_style_for_day))
    for x in range(0, day_range_of_the_month[1]):
        my_date = datetime.date(year, month, x+1)
        my_weekday = int(my_date.strftime("%w")) #Sunday = 0
        my_week = int(int(my_date.strftime("%U")) - int(first_week_of_the_month)) + 1 #plus 1 shifts for weekbar
        #print ("my day: %s, my week: %s, my day: %s") % (x+1, my_week, my_weekday)
        my_x = (my_weekday * ((radius*2)+day_xmargin)) + radius + left_margin
        my_date_x = my_x
        my_y = (my_week * ((radius*2)+day_ymargin))
        my_date_y = my_y #- font_size_for_day
        #f.write('\t\t\t\t<circle cx="%s" cy="%s" r="%s"/>\n' % (my_x, my_y, radius))
        f.write('\t\t\t\t\t<text x="%s" y="%s">%s</text>\n' % (my_date_x, my_date_y, my_date.strftime("%d")))
    f.write('\t\t\t\t</g>\n') # end month_days
    f.write('\t\t\t</g>\n') #end minical
    f.write('\t\t</g>\n') #end month

f.write('\t</g>\n') #end calendar

f.write('</svg>')
f.close()
