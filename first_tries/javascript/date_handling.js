

let today = new Date(); //no input = curent datetime
let day_tested = new Date(1515267948639); //date in millis
let this_millis = new Date().getTime();
let o_day = new Date(January 1, 1970); //anything recognizable with Date.parse()
let foo_day = new Date(1983, 12, 16, 8, 23, 12, 532); //year, month, day, hours, minutes, seconds, milliseconds

let day_of_the_month = today.getDate();
let day_of_the_week_num = today.getDay()
let year = today.getFullYear();
let month = today.getMonth();  // 0 to 11, 12 is January of next year
let third_of_this_month = today.setDate(3); //sets the date's day to 3

let options = {
    weekday: 'long', year: 'numeric', month: 'short',
    day: 'numeric', hour: '2-digit', minute: '2-digit'
  };

let message = today.toLocaleTimeString('en-us', options);
console.log(message)

//Switch to moment.js

let moment = require('moment');
let new_date = Date();
let mday = moment(new_date);

let weekday_as_number = mday.format('d')
let weekday_as_two_letter_text = mday.format('dd')
let zero_led_date = mday.format('DD') // zero leading day of the month
let week_of_the_month = mday.format('w')
let full_month_full_year = mday.format("MMMM, YYYY")
let last_day_of_the_month = mday.daysInMonth()

//seven days from now
let next_week = mday.add(7, 'days');
let next_week2 = mday.add(7, 'd');

//3 days from now next month
let added_date = mday.add(3, 'days').add(1, 'months'); // with chaining
let added_date2 = mday.add({days:3,months:1}); // with object literal

//snap to beginning, there is also .endOf
let first_day_of_year = mday.startOf('year');    // set to January 1st, 12:00 am this year
let first_day_of_month = mday.startOf('month');   // set to the first of this month, 12:00 am
let first_day_of_quarter =mday.startOf('quarter');  // set to the beginning of the current quarter, 1st day of months, 12:00 am
let first_day_of_week = mday.startOf('week');    // set to the first day of this week, 12:00 am
let first_day_of_weekISO = mday.startOf('isoWeek');

//iterating
//https://stackoverflow.com/questions/17163809/iterate-through-a-range-of-dates-in-nodejs
var a = moment('2013-01-01');
var b = moment('2013-06-01');

// If you want an exclusive end date (half-open interval)
for (var m = moment(a); m.isBefore(b); m.add(1, 'days')) {
  console.log(m.format('YYYY-MM-DD'));
}

// If you want an inclusive end date (fully-closed interval)
for (var m = moment(a); m.diff(b, 'days') <= 0; m.add(1, 'days')) {
  console.log(m.format('YYYY-MM-DD'));
}
