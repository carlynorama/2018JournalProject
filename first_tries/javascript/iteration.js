let days_of_the_week = ['M', 'T', 'W', 'Th', 'F', 'Sa', 'Su']
let this_weeks_dates = [ 16, 17, 18, 19, 20, 21, 22]


//old school
for (let d = 0; d < 7; d++) {
    console.log(days_of_the_week[d]);
}

//for the length of the array
for (let d = 0; d < days_of_the_week.length; d++) {
    console.log(days_of_the_week[d]);
}

//dual array-ish
for (let d = 0; d < days_of_the_week.length; d++) {
    let message = `The ${this_weeks_dates[d]} is a ${days_of_the_week[d]}`
    console.log(message);
}

//start late, skip around
for (let d = 1; d < days_of_the_week.length; d +=2) {
    let message = `The ${this_weeks_dates[d]} is a ${days_of_the_week[d]}`
    console.log(message);
}

//apparently ad hoc order but will do all of them
for (d in days_of_the_week) {
  console.log(days_of_the_week[d]);
}

// like for in but will get them in order for sure
// const or let for "day" depending on whether you change it
for (const day of days_of_the_week) {
  console.log(day);
}

//get them in order and can perform a function/closure
function printMessage(message) {
    console.log(message)
}
days_of_the_week.forEach(printMessage)

//define add a little conditional with iteration
days_of_the_week.forEach(function(array_element, index) {
  return index > 2 ? printMessage(array_element) : null;
})

//over a string
day_name = "Monday"
for (let c of day_name) {
  console.log(c);
}

//"Zip" two arrays into a Map
let week_map = this_weeks_dates.map(function(array_element, index) {
  return [array_element, days_of_the_week[index]];
});

console.log(week_map)

//Using new "entries" feature. Like enumerate
for (const [key, value] of days_of_the_week.entries()) {
  console.log(`${key} ${value}`); // "a 5", "b 7", "c 9"
}

//Treating the array as an Object
Object.entries(days_of_the_week).forEach(([key, value]) => {
console.log(`${key} ${value}`); // "a 5", "b 7", "c 9"
});

//This does not work?
days_of_the_week.entries().forEach(([key, value]) => {
console.log(`${key} ${value}`); // "a 5", "b 7", "c 9"
});

//https://www.htmlgoodies.com/html5/javascript/getting-fancy-with-the-javascript-for-loop.html

//Dual conditions: Start at 0 end at Wednesday
for (let i=0; i<days_of_the_week.length && days_of_the_week[i] != 'W'; i++) {
  console.log( 'day #' + (i+1) + ' is a ' + days_of_the_week[i])
}

//Two Incrementors
for(let a = 1, b = 10; a*b; a++, b--) {
  console.log(`${a} ${b}`);
}

//letiable declarations galore.
for (let i=0, len=days_of_the_week.length, text="You've got "+len+" days:\n"; i<len; i++) {
    text += days_of_the_week[i] + "\n";
}
console.log(text) //text now persists after the for loop.
