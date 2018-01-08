const fs = require('fs')
let moment = require('moment')
//https://momentjs.com/docs/#/displaying/

let year = 2018
let month = 3

let viewBoxWidth = 2550
let viewBoxHeight = 3300
let radius = viewBoxWidth/16
let day_xmargin = radius/10
let day_ymargin = radius
let centerX = radius
let centerY = radius
let outline_style_for_day = "fill:rgb(200,200,255);"
let font_size_for_day = radius
let font_style_for_day = `font-family:\'Helvetica\';font-size:${font_size_for_day}px;fill:rgb(102,102,102);`
let font_size_for_month = 2*radius
let font_style_for_month = `font-family:\'Helvetica\';font-size:${font_size_for_month}px;fill:rgb(102,102,102);`


let day = new Date(year, month, 1);
let first_day = moment(day);
first_weekday = first_day.format('d')
first_week_of_the_month = first_day.format('w')
file_name = first_day.format('YYYYMMM')
month_name = first_day.format("MMMM, YYYY")
last_day_of_the_month = first_day.daysInMonth()
console.log(`START !!! my date: ${day} my week: ${first_week_of_the_month}, my day: ${first_weekday}"`)


let svg = ""
svg += '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
svg += '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'

svg += `<svg width="100%" height="100%" viewBox="0 0 ${viewBoxWidth} ${viewBoxHeight}" xmlns="http://www.w3.org/2000/svg">\n`

svg += `\t<g transform="translate(${(radius/2)}, ${(viewBoxHeight/4)})" style="${outline_style_for_day}">\n`

for (let x = 0; x < last_day_of_the_month; x++) {
    let my_date = new Date(year, month, x+1)
    let my_moment = moment(my_date)
    let my_weekday = my_moment.format('d')
    let my_week = my_moment.format('w') - first_week_of_the_month
    //console.log(`my date: ${my_date} my week: ${my_week}, my day: ${my_weekday}"`)
    let my_x = centerX + day_xmargin + (my_weekday * ((radius*2)+day_xmargin))
    let my_date_x = my_x + day_xmargin/2
    let my_y = centerY + ((my_week) * ((radius*2)+day_ymargin))
    let my_date_y = my_y //- font_size_for_day
    let my_date_text = my_moment.format('DD')

    svg += `\t<circle cx="${my_x}" cy="${my_y}" r="${radius}"/>\n`
    svg += `\t<text x="${my_date_x}" y="${my_date_y}" style="${font_style_for_day}" text-anchor="middle" dominant-baseline="central">${my_date_text}</text>\n`


    //svg += `\t<circle cx="${centerX+(x*((radius*2)+5))}" cy="${centerY}" r="${radius}" style="${outline_style_for_day}"/>\n`
}
svg += '\t</g>\n'

svg += `\t<g transform="translate(${(radius/2)}, ${(viewBoxHeight/8)})" style="${font_style_for_month}">\n`
svg += `\t\t<text>${month_name}</text>\n`
svg += '\t</g>\n'

svg += '</svg>'

fs.writeFile(`${file_name}.svg`, svg, (err) => {  
    // throws an error, you could also catch it here
    if (err) throw err;

    // success case, the file was saved
    console.log('SVG !');
});
