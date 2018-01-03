centerX = 15
centerY = 15
radius = 10
style = "fill:rgb(200,200,255);"

f = open('helloworld.svg','w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
f.write('<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">\n')

for x in range(0, 12):
    f.write('\t<circle cx="%s" cy="%s" r="%s" style="%s"/>\n' % (centerX+(x*((radius*2)+5)), centerY, radius, style))

f.write('</svg>')
f.close()
