#habit_weekly_grid.py
import json
import fileparser

save_file_name = "habit_weekly_pygen"
data_file_name = 'example_data/simplesthabits.txt'

viewBoxWidth = 3300
viewBoxHeight = 2550

font_size_for_row = 32
font_size_for_col = 24
row_max_label_length = 9

col_items = ["M", "T", "W", "Th", "F", "S", "Su"]
row_items = fileparser.loadnamesonlyfromfile(data_file_name)

row_range = range(0,(len(row_items))) #0 is header
max_row_number = max(row_range)
row_height = 1.5 * font_size_for_row
row_label_size = font_size_for_row * row_max_label_length
grid_height = row_height * (max_row_number+2)


col_range = range(0,(len(col_items))) #0 is header
max_col_number = max(col_range)
col_width = 3 * font_size_for_col
grid_width = row_label_size + ((max_col_number+1) * col_width)

divider_line_style = "stroke:rgb(153,153,153);stroke-width:2"
heavy_divider_line_style = "stroke:rgb(153,153,153);stroke-width:4"

font_style_for_col = "font-family:\'Helvetica\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_col
font_style_for_row = "font-family:\'Helvetica\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_row

f = open('%s.svg' % save_file_name, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')

f.write('<svg width="100%%" height="100%%" viewBox="0 0 %s %s" xmlns="http://www.w3.org/2000/svg">\n' % (viewBoxWidth, viewBoxHeight))

f.write('<g id="tracker" transform="translate(%s, %s)">\n' % ("100", "100"))

#Column line after row lable
f.write('\t\t\t<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />\n' % (row_label_size, 0, row_label_size, grid_height, heavy_divider_line_style))
for c in col_range:
    my_line_x = row_label_size + ((c+1) * col_width)
    my_text_x = row_label_size + col_width/2 + ((c) * col_width)
    my_text = col_items[c]
    f.write('\t\t<text x="%s" y="%s" style="%s" text-anchor="middle" dominant-baseline="middle">%s</text>\n' % (my_text_x, row_height/2, font_style_for_col, my_text))
    f.write('\t\t\t<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />\n' % (my_line_x, 0, my_line_x, grid_height, divider_line_style))

#Row line after row lable
f.write('\t\t\t<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />\n' % (0, row_height, grid_width, row_height, heavy_divider_line_style))
for r in row_range:
    my_line_y = (r + 2) * row_height
    my_text_y = my_line_y - row_height/2
    my_text = row_items[r]
    f.write('\t\t<text x="%s" y="%s" style="%s" text-anchor="end" dominant-baseline="middle">%s</text>\n' % ((row_label_size-font_size_for_row), my_text_y, font_style_for_row, my_text))
    f.write('\t\t\t<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />\n' % (0, my_line_y, grid_width, my_line_y, divider_line_style))

f.write('\t</g>\n') #end grid
f.write('</svg>')
f.close()
