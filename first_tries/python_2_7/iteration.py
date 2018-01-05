days_of_the_week = ['M', 'T', 'W', 'Th', 'F', 'Sa', 'Su']

print "for i in array"
for i in days_of_the_week:
  print i

print "for i in defined range"
for i in range(0, 7):
    print days_of_the_week[i]

#for super big ranges, python 2.7 not 3
for i in xrange(0, 7):
    print days_of_the_week[i]

print "for i in defined range, every other"
for i in range(0, 7, 2):
    print days_of_the_week[i]

print "for i in range by length of array"
for i in range(len(days_of_the_week)):
     print days_of_the_week[i]

for num, day in enumerate(days_of_the_week):
    print("Day # {}: {}".format(num, day))

string = "Monday"
for c in string:
    print c

month = [ days_of_the_week, days_of_the_week, days_of_the_week, days_of_the_week]
print "month"
for week in month:
    print "next week"
    for day in week:
        print day
centerX = 15
centerY = 15
radius = 10
style = "fill:rgb(200,200,255);"

message2 = '\t<circle cx="{}" cy="{}" r="{}" style="{}"/>\n'.format(centerX+(1*((radius*2)+5)), centerY, radius, style)
print(message2)
