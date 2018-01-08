#yearataglanceSVG.py

import datetime

import calendar
#https://docs.python.org/2/library/calendar.html

year = 2018
month = 1 #1 thru 12
start_day = 1
number_of_days = 4
start_date = datetime.date(year, month, start_day)
end_date = start_date + datetime.timedelta(days=number_of_days)

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
font_style_for_month = "font-family:\'Futura\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_month
font_size_for_title = int(radius)*2
font_style_for_title = "font-family:\'Futura\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_title

content_x_offset = 75
content_y_offset = 2 * viewBoxHeight / 15
title_x_offset = content_x_offset
title_y_offset = content_y_offset - (font_size_for_title*1.5)

file_name = "%s_week_%s_%s_pygen" % (year, start_date.strftime("%m%d"), end_date.strftime("%m%d"))
page_title = "Weekly Planning - %s to %s" % (start_date.strftime("%b %-d, %Y"), end_date.strftime("%b %-d, %Y"))

day_range = range(0,number_of_days)

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
for d in day_range:
    current_day = start_day + d
    day_x_offset = (d)%number_of_days * (calendarWidth/number_of_days + (2*radius))
    left_margin = radius
    #month_y_offset = (month-1)/3 * (calendarHeight/4 + (2*radius))
    #print('%s: (%s, %s)' % (month, month_x_offset, month_y_offset))
    day_as_date = datetime.date(year, month, current_day)
    print(day_as_date)
    day_of_the_week_text = day_as_date.strftime("%A")
    day_date_text = day_as_date.strftime("%b %-d")
    day_name = day_as_date.strftime("%b_%-d")

    f.write('\t\t<g id="%s" transform="translate(%s, %s)">\n' % (day_name, day_x_offset, 0))
    f.write('\t\t\t<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />\n' % (0, 0, 0, calendarHeight, divider_line_style))
    #print('%s line: (%s, %s) to (%s, %s)' % (current_day, day_x_offset + left_margin, 0, day_x_offset, calendarHeight))
    f.write('\t\t\t<text x="%s" y="%s" style="%s" text-anchor="left">%s</text>\n' % (0+left_margin, font_size_for_month, font_style_for_month, day_of_the_week_text))
    f.write('\t\t\t<text x="%s" y="%s" style="%s" text-anchor="left">%s</text>\n' % (0+left_margin, font_size_for_month*2, font_style_for_month, day_date_text))
    f.write('\t\t</g>\n') #end month

f.write('\t</g>\n') #end calendar

f.write('</svg>')
f.close()
