//

const fs = require('fs')
var moment = require('moment')
//https://momentjs.com/docs////displaying/

let year = 2018
let start_month = 0
let start_day = 6
let number_of_days = 7
let start_date = new Date(year, start_month, start_day);

let start_moment = moment(start_date);
console.log(`start moment: ${start_moment}`)
let end_moment = moment(start_moment.toDate()).add(number_of_days, 'days')
console.log(`start moment: ${start_moment}`)
console.log(`end moment: ${end_moment}`)

let viewBoxWidth = 3300
let viewBoxHeight = 2550
let calendarWidth = 2900
let calendarHeight = 2100

let radius = calendarWidth/((6*7)*2.5)
let day_xmargin = radius/3
let day_ymargin = radius/3
let outline_style_for_day = "fill:rgb(220,230,255);"
let divider_line_style = "stroke:rgb(153,153,153);stroke-width:2"
let font_size_for_day = radius*2
let font_style_for_day = `font-family:\'Futura\', \'Helvetica\';font-size:${font_size_for_day}px;fill:rgb(102,102,102);`
let font_size_for_title = radius*2
let font_style_for_title = `font-family:\'Futura\', \'Helvetica\';font-size:${font_size_for_title}px;fill:rgb(102,102,102);`

let content_x_offset = 75
let content_y_offset = 2 * viewBoxHeight / 15
let title_x_offset = content_x_offset
let title_y_offset = content_y_offset - (font_size_for_title*1.5)

let file_name = `${year}_week_${start_moment.format('MMDD')}_${end_moment.format('MMDD')}_jsgen`
let page_title = `Weekly Planning - ${start_moment.format('MMM Do, YYYY')} to ${end_moment.format('MMM Do, YYYY')}`

var svg = ""
svg += '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
svg += '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'

svg += `<svg width="100%" height="100%" viewBox="0 0 ${viewBoxWidth} ${viewBoxHeight}" xmlns="http://www.w3.org/2000/svg">\n`
svg += `<style>/* <![CDATA[ */circle{${outline_style_for_day}}/* ]]> */</style>\n` //% outline_style_for_day)

svg += `\t<g id="page_title" transform="translate(${title_x_offset}, ${title_y_offset})">\n`
svg += `\t\t<text x="0" y="0" style="${font_style_for_title}" text-anchor="start" dominant-baseline="central">${page_title}</text>\n`
svg += '\t\t</g>\n' // end page_title

svg += `<g id="calendar" width="${calendarWidth}" height="${calendarHeight}" transform="translate(${content_x_offset}, ${content_y_offset})">\n`
for (let d=0; d < number_of_days; d++) {
    var current_moment = moment(start_moment) // passes by reference? You're killeing me.
    current_moment.add(d, 'days');
    console.log(`current: ${current_moment}, start: ${start_moment}`)
    let day_x_offset = (d)%number_of_days * (calendarWidth/number_of_days + (2*radius))
    let left_margin = radius

    let day_of_the_week_text = current_moment.format('dddd')
    let day_date_text = current_moment.format('MMM D')
    let day_name = current_moment.format('MMDD')

    svg += `\t\t<g id="${day_name}" transform="translate(${day_x_offset}, 0)">\n`
    svg += `\t\t\t<line x1="${0}" y1="${0}" x2="${0}" y2="${calendarHeight}" style="${divider_line_style}" />\n`
    svg += `\t\t\t<text x="${0+left_margin}" y="${font_size_for_day}" style="${font_style_for_day}" text-anchor="left">${day_of_the_week_text}</text>\n`
    svg += `\t\t\t<text x="${0+left_margin}" y="${font_size_for_day*2}" style="${font_style_for_day}" text-anchor="left">${day_date_text}</text>\n`
    svg += '\t\t</g>\n' //end day
}
svg += '\t</g>\n' //end calendar

svg += '</svg>' //end svg

fs.writeFile(`${file_name}.svg`, svg, (err) => {  
    // throws an error, you could also catch it here
    if (err) throw err;

    // success case, the file was saved
    console.log('SVG !');
});
