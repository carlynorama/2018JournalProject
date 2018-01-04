
file_name = "grid_test"
viewBoxWidth = 3300
viewBoxHeight = 2550

row_font_size = 10
row_max_label_length = 15

grid_height = viewBoxHeight/2
row_range = range(0,13) #0 is header
max_row_number = max(row_range)
row_height = grid_height/max_row_number
row_label_size = row_font_size * row_max_label_length

grid_width = viewBoxWidth/2
col_range = range(1,32)
max_col_number = max(col_range)
col_width = (grid_width - row_label_size)/max_col_number

divider_line_style = "stroke:rgb(153,153,153);stroke-width:2"
heavy_divider_line_style = "stroke:rgb(153,153,153);stroke-width:4"
font_size_for_col = col_width/2
font_style_for_col = "font-family:\'Helvetica\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_col

f = open('%s.svg' % file_name, 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')

f.write('<svg width="100%%" height="100%%" viewBox="0 0 %s %s" xmlns="http://www.w3.org/2000/svg">\n' % (viewBoxWidth, viewBoxHeight))

#Column line after row lable
f.write('\t\t\t<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />\n' % (row_label_size, 0, row_label_size, grid_height, heavy_divider_line_style))
for c in col_range:
    my_line_x = row_label_size + ((c) * col_width)
    my_text_x = row_label_size + col_width/2 + ((c-1) * col_width)
    my_text = c
    f.write('\t\t<text x="%s" y="%s" style="%s" text-anchor="middle">%s</text>\n' % (my_text_x, font_size_for_col, font_style_for_col, my_text))
    f.write('\t\t\t<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />\n' % (my_line_x, 0, my_line_x, grid_height, divider_line_style))

for r in row_range:
    my_y = r * row_height
    my_text = "September"
    f.write('\t\t<text x="%s" y="%s" style="%s" text-anchor="end">%s</text>\n' % ((row_label_size-row_font_size), my_y, font_style_for_col, my_text))
    f.write('\t\t\t<line x1="%s" y1="%s" x2="%s" y2="%s" style="%s" />\n' % (0, my_y, grid_width, my_y, divider_line_style))


f.write('</svg>')
f.close()
