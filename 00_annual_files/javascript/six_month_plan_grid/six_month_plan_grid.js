//

const fs = require('fs')
var moment = require('moment')
//https://momentjs.com/docs////displaying/

let year = 2018
let start_month = 0
let end_month = 6
let number_of_months = end_month-start_month

let viewBoxWidth = 3300
let viewBoxHeight = 2550
let calendarWidth = 2900
let calendarHeight = 2100

let radius = calendarWidth/((6*7)*2.5)
let day_xmargin = radius/3
let day_ymargin = radius/3
let outline_style_for_day = "fill:rgb(220,230,255);"
let divider_line_style = "stroke:rgb(153,153,153);stroke-width:2"
let font_size_for_day = radius
let font_style_for_day = `font-family:\'Helvetica\';font-size:${font_size_for_day}px;fill:rgb(102,102,102);`
let font_style_for_days_of_week = `font-family:\'Helvetica\';font-size:${font_size_for_day}px;fill:rgb(51,51,51);`
let font_size_for_month = radius*2
let font_style_for_month = `font-family:\'Futura\', \'Helvetica\';font-size:${font_size_for_month}px;fill:rgb(102,102,102);`
let font_size_for_title = radius*4
let font_style_for_title = `font-family:\'Futura\', \'Helvetica\';font-size:${font_size_for_title}px;fill:rgb(102,102,102);`

let content_x_offset = 75
let content_y_offset = 2 * viewBoxHeight / 15
let title_x_offset = content_x_offset
let title_y_offset = content_y_offset - (font_size_for_title*1.5)

let file_name = `${year}_sixmo_jsgen`
let page_title = `Future Planning - ${year}`

//momnent.js could be customized instead. Would be better for localization.
let days_of_the_week = ['S', 'M', 'T', 'W', 'T', 'F', 'S']

var svg = ""
svg += '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
svg += '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'

svg += `<svg width="100%" height="100%" viewBox="0 0 ${viewBoxWidth} ${viewBoxHeight}" xmlns="http://www.w3.org/2000/svg">\n`
svg += `<style>/* <![CDATA[ */circle{${outline_style_for_day}}/* ]]> */</style>\n` //% outline_style_for_day)

svg += `\t<g id="page_title" transform="translate(${title_x_offset}, ${title_y_offset})">\n`
svg += `\t\t<text x="0" y="0" style="${font_style_for_title}" text-anchor="start" dominant-baseline="central">${page_title}</text>\n`
svg += '\t\t</g>\n' // end page_title

svg += `<g id="calendar" width="${calendarWidth}" height="${calendarHeight}" transform="translate(${content_x_offset}, ${content_y_offset})">\n`
for (let m=start_month; m < end_month; m++) {
    let month = m
    let month_x_offset = (month)%number_of_months * (calendarWidth/number_of_months + (2*radius))
    let left_margin = radius
      //console.log(`${month}: (${month_x_offset}, ${month_y_offset})`)
    let day = new Date(year, m, 1);
    let first_day = moment(day);
    let first_weekday = first_day.format('d')
    let first_week_of_the_month = first_day.format('w')
    let month_name = first_day.format("MMMM")
    let month_title = first_day.format("MMMM")
    let last_day_of_the_month = first_day.daysInMonth()

    svg += `\t\t<g id="${month_name}" transform="translate(${month_x_offset}, 0)">\n`
    svg += `\t\t\t<line x1="${0}" y1="${0}" x2="${0}" y2="${calendarHeight}" style="${divider_line_style}" />\n`
    console.log('${month} line: (${month_x_offset + left_margin}, ${0}) to (${month_x_offset}, ${calendarHeigh})')
    svg += `\t\t\t<text x="${0+left_margin}" y="${font_size_for_month}" style="${font_style_for_month}" text-anchor="left">${month_title}</text>\n`
    svg += `\t\t\t<g id="minical" transform="translate(${0+left_margin}, ${font_size_for_month*3})" text-anchor="middle">\n`
    svg += `\t\t\t\t<g id="${month_name}_weekbar" transform="translate(0, ${0})" style="${font_style_for_day}">\n`
    for (let d=0; d < 7; d++) {
        my_x = (d * ((radius*2)+day_xmargin)) + radius
        my_y = 0
        svg += `\t\t\t\t\t<text x="${my_x}" y="${my_y}">${days_of_the_week[d]}</text>\n`
    }
    svg += '\t\t\t\t</g>\n' // end month_weekbar
    svg += `\t\t\t\t<g id="${month_name}_days" transform="translate(0, 0)" style="${font_style_for_day}" >\n`
    for (let x = 0; x < last_day_of_the_month; x++) {
        let my_day = x+1
        let my_date = new Date(year, month, my_day)
        let my_moment = moment(my_date)
        let my_weekday = my_moment.format('d')

        //catches 5th week in December error w/o causing weird March error
        var my_week = 0
        if ((month == 11) && (my_moment.format('w') < first_week_of_the_month)) {
            my_week = parseInt(my_moment.format('w')) + 52 - first_week_of_the_month + 1
        } else {
            my_week = (my_moment.format('w') - first_week_of_the_month) + 1
        }

        //let my_week = (my_moment.format('w') - first_week_of_the_month) + 1
        console.log(`my week: ${my_moment.format('w')}, first week: ${first_week_of_the_month}, calc'd: ${my_week}"`)
        //console.log(`my date: ${my_date} my week: ${my_week}, my day: ${my_weekday}"`)

        let my_x = (my_weekday * ((radius*2)+day_xmargin)) + radius
        let my_date_x = my_x
        let my_y = (my_week * ((radius*2)+day_ymargin))
        let my_date_y = my_y //- font_size_for_day
        let my_date_text = my_moment.format('DD')

        //svg += `\t\t\t\t\t<circle cx="${my_x}" cy="${my_y}" r="${radius}"/>\n`
        svg += `\t\t\t\t\t<text x="${my_date_x}" y="${my_date_y}">${my_date_text}</text>\n`
      }
    svg += '\t\t\t\t</g>\n' // end month_days
    svg += '\t\t\t</g>\n' //end minical
    svg += '\t\t</g>\n' //end month
}
svg += '\t</g>\n' //end calendar

svg += '</svg>'

fs.writeFile(`${file_name}.svg`, svg, (err) => {  
    // throws an error, you could also catch it here
    if (err) throw err;

    // success case, the file was saved
    console.log('SVG !');
});
