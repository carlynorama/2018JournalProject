const fs = require('fs')
const moment = require('moment')

let habitdata = fs.readFileSync('example_data/habits.json');
let habits = JSON.parse(habitdata);
console.log(habits);

const file_name = "habit_weekly_jsgen"
const viewBoxWidth = 3300
const viewBoxHeight = 2550
const place_on_page_x = 100
const place_on_page_y = 100

const font_size_for_row = 32
const font_size_for_col = 24
const row_max_label_length = 9

const col_items = ["M", "T", "W", "Th", "F", "S", "Su"]
const row_items = ["Habit1", "Habit2", "Habit3", "Habit4", "Habit5", "Habit5", "Habit7", "Habit8"]

const num_of_rows = row_items.length
const max_row_number = num_of_rows-1
const row_height = 1.5 * font_size_for_row
const row_label_size = font_size_for_row * row_max_label_length
const grid_height = row_height * (max_row_number+2)


const num_of_cols = col_items.length
const max_col_number = num_of_cols-1
const col_width = 3 * font_size_for_col
const grid_width = row_label_size + ((max_col_number+1) * col_width)

const divider_line_style = "stroke:rgb(153,153,153);stroke-width:2"
const heavy_divider_line_style = "stroke:rgb(153,153,153);stroke-width:4"

const font_style_for_col = "font-family:\'Helvetica\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_col
const font_style_for_row = "font-family:\'Helvetica\';font-size:%spx;fill:rgb(102,102,102);" % font_size_for_row

let svg = ""
svg += `<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n`
svg += `<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n`

svg += `<svg width="100%%" height="100%%" viewBox="0 0 ${viewBoxWidth} ${viewBoxHeight}" xmlns="http://www.w3.org/2000/svg">\n`

svg += `<g id="tracker" transform="translate(${place_on_page_x}, ${place_on_page_y})">\n`

//Column line after row lable
svg += `\t\t\t<line x1="${row_label_size}" y1="${0}" x2="${row_label_size}" y2="${grid_height}" style="${heavy_divider_line_style}" />\n`

for (let c=0; c < num_of_cols; c++) {
    my_line_x = row_label_size + ((c+1) * col_width)
    my_text_x = row_label_size + col_width/2 + ((c) * col_width)
    my_text = col_items[c]
    svg += `\t\t<text x="${my_text_x}" y="${row_height/2}" style="${font_style_for_col}" text-anchor="middle" dominant-baseline="middle">${my_text}</text>\n`
    svg += `\t\t\t<line x1="${my_line_x}" y1="${0}" x2="${my_line_x}" y2="${grid_height}" style="${divider_line_style}" />\n`
}

//Row line after row lable
svg += `\t\t\t<line x1="${0}" y1="${row_height}" x2="${grid_width}" y2="${row_height}" style="${heavy_divider_line_style}" />\n`
for (let r=0; r < num_of_rows; r++) {
    my_line_y = (r + 2) * row_height
    my_text_y = my_line_y - row_height/2
    my_text = row_items[r]
    svg += `\t\t<text x="${(row_label_size-font_size_for_row)}" y="${my_text_y}" style="${font_style_for_row}" text-anchor="end" dominant-baseline="middle">${my_text}</text>\n`
    svg += `\t\t\t<line x1="${0}" y1="${my_line_y}" x2="${grid_width}" y2="${my_line_y}" style="${divider_line_style}" />\n`
}
svg += `\t</g>\n` //end grid
svg += '</svg>'

fs.writeFile(`${file_name}.svg`, svg, (err) => {  
    // throws an error, you could also catch it here
    if (err) throw err;

    // success case, the file was saved
    console.log('SVG !');
});
