
function createGauge(elementId, labelId, minValue, RedToOr, OrtoGreen, GreenToOr, OrToRed, maxValue, label, radius) {
  var opts = {
    angle: -0.2,
    lineWidth: 0.1,
    radiusScale: radius,
    pointer: {
      length: 0.6,
      strokeWidth: 0.035,
      color: 'rgb(75, 192, 192)'
    },
    limitMax: true,
    limitMin: true,
    colorStart: '#6FADCF',
    colorStop: '#8FC0DA',
    strokeColor: '#E0E0E0',
    generateGradient: true,
    highDpiSupport: false,
    staticZones: [
      {strokeStyle: "#F03E3E", min: minValue, max: RedToOr}, // Red zone
      {strokeStyle: "#FFA500", min: RedToOr, max: OrtoGreen}, // Orange zone
      {strokeStyle: "#30B32D", min: OrtoGreen, max:GreenToOr}, // Green zone
      {strokeStyle: "#FFA500", min: GreenToOr, max: OrToRed}, // Orange zone
      {strokeStyle: "#F03E3E", min: OrToRed, max: maxValue}, // Red zone
    ],
  };

  var target = document.getElementById(elementId);
  var gauge = new Gauge(target).setOptions(opts);
  gauge.maxValue = maxValue;
  gauge.setMinValue(minValue);
  gauge.animationSpeed = 0;
  gauge.set(minValue); // set initial value

  var labelElement = document.getElementById(labelId);
  labelElement.innerText = label;

  return gauge;
}

// Create gauges with their respective normal operating ranges
var interiorTempGauge = createGauge('mainTempGaugeIn', 'gridLabel11', 10, 40, 20, 25, 30, 'Interior Temp', 1);
var ambientTempGauge = createGauge('mainTempGaugeOut', 'gridLabel10', -20, 40, 15, 25, 30, 'Ambient Temp', 1);

var loadGauge = createGauge('gridCanvas1', 'gridLabel1', 0, 0, 0, 75, 90, 100, 'Load', .8);
var shortTrimGauge = createGauge('gridCanvas2', 'gridLabel2', -20, -15, -10, 10, 15, 20, 'Short Trim', .8);
var coolantGauge = createGauge('gridCanvas3', 'gridLabel3', 50, 50, 70, 110, 120,130, 'Coolant', .8);
var throttleGauge = createGauge('gridCanvas4', 'gridLabel4', 0, 0, 0, 100, 100,100, 'Throttle', .8);
// var runtimeGauge = createGauge('gridCanvas5', 'gridLabel5', 0, 6000, 500, 750, 2500, 'Runtime', .8);

var absoluteLoadGauge = createGauge('gridCanvas6', 'gridLabel6',0, 0, 0, 75, 90, 100, 'Abs Load', .8);
var longTrimGauge = createGauge('gridCanvas7', 'gridLabel7', -20, -15, -10, 10, 15, 20, 'Long Trim', .8);
var IntakeTempGauge = createGauge('gridCanvas8', 'gridLabel8', 0, 0, 0, 60, 100, 120, 'Intake D', .8);
var speedGauge = createGauge('gridCanvas9', 'gridLabel9', 0, 0, 0, 120,120, 120, 'MPH', .8);
var voltageGauge = createGauge('gridCanvas10', 'gridLabel10', 9, 10, 11.5, 14.5, 16, 16, 'Voltage', .8);

var RPMGauge = createGauge('gridCanvas11', 'gridLabel11', 0, 0, 600, 2500, 6000, 7000, 'RPM', .8);
var airFlowGauge   = createGauge('gridCanvas12', 'gridLabel12', 0, 0, 0, 150,200, 250, 'MAF', .8);
var fuelGauge = createGauge('gridCanvas13', 'gridLabel13', 0, 10, 20, 80, 90, 100, 'Fuel', .8);
// var g14 = createGauge('gridCanvas14', 'gridLabel14', 0, 6000, 500, 750, 2500, '', .8);
var equiRatioGaugeGauge = createGauge('gridCanvas15', 'gridLabel15', .5, .7, .7, .7,1.3, 1.5, 'Ratio', .8);


ambientTempGauge.set(20);
interiorTempGauge.set(20);

// var ctx = document.getElementById('gridCanvas1');
// var myChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: ['Current MPG'],  // Set your label
//         datasets: [{
//             label: '',  // Remove or leave this empty
//             data: [20],  // Set your data value
//             backgroundColor: [
//                 'rgb(75, 192, 192)'  // Set the color of your bar
//             ],
//         }]
//     },
//     options: {
//         plugins: {
//             legend: {
//                 display: false   //This will hide the legend
//             }
//         },
//         scales: {
//             y: {
//                 beginAtZero: false,  // This can be set to false if min value is not zero
//                 min: 0,   // This is the minimum value
//                 max: 30,    // This is the maximum value
//                 ticks: {
//                     stepSize: 10
//                 }
//             }
//         }
//     }
// });





// var opts = {
//   angle: -0.2, // The span of the gauge arc
//   lineWidth: 0.1, // The line thickness
//   radiusScale: .8, // Relative radius
//   pointer: {
//     length: 0.4, // // Relative to gauge radius
//     strokeWidth: 0.035, // The thickness
//     color: 'gold' // Fill color
//   },
//   limitMax: false,     // If false, max value increases automatically if value > maxValue
//   limitMin: false,     // If true, the min value of the gauge will be fixed
//   colorStart: '#6FADCF',   // Colors
//   colorStop: '#8FC0DA',    // just experiment with them
//   strokeColor: '#E0E0E0',  // to see which ones work best for you
//   generateGradient: true,
//   highDpiSupport: true,     // High resolution support
//   staticZones: [
//     {strokeStyle: "#F03E3E", min: -10, max: 20}, // Red from 100 to 130
//     {strokeStyle: "#30B32D", min: 20, max: 30}, // Yellow
//     {strokeStyle: "#F03E3E", min: 30, max: 60}, // Green
//  ],
  
// };


// console.log("creating grid gauges");
// var gridGauges = [];
// for(var i = 1; i < 11; i++){
//   var idName = "gridCanvas" + (i+1);
//   var g = new Gauge(document.getElementById(idName)).setOptions(opts);
  
//   g.maxValue = 60; // set max gauge value
//   g.setMinValue(-10);  // Prefer setter over gauge.minValue = 0
//   g.animationSpeed = 32; // set animation speed (32 is default value)
//   g.set(20); // set actual value

//   gridGauges.push(g);
// }



// opts.radiusScale = .9;


// var target1 = document.getElementById('mainTempGaugeIn'); // your canvas element
// var gauge1 = new Gauge(target1).setOptions(opts); // create sexy gauge!
// gauge1.maxValue = 60; // set max gauge value
// gauge1.setMinValue(-10);  // Prefer setter over gauge.minValue = 0
// gauge1.animationSpeed = 32; // set animation speed (32 is default value)
// gauge1.set(25); // set actual value

// var target = document.getElementById('mainTempGaugeOut'); // your canvas element
// var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
// gauge.maxValue = 60; // set max gauge value
// gauge.setMinValue(-10);  // Prefer setter over gauge.minValue = 0
// gauge.animationSpeed = 32; // set animation speed (32 is default value)
// gauge.set(40); // set actual value

// var target1 = ; // your canvas element
// var gauge1 = new Gauge(target1).setOptions(opts); // create sexy gauge!
// gauge1.maxValue = 60; // set max gauge value
// gauge1.setMinValue(-10);  // Prefer setter over gauge.minValue = 0
// gauge1.animationSpeed = 32; // set animation speed (32 is default value)
// gauge1.set(20); // set actual value

// console.log("hello");

// var gridGauges = Array(10);
// for(var i = 1; i<=10; i++){
//   var target1 = document.getElementById('gridSpace' + toString(i)); // your canvas element
//   var mewGauge = new Gauge(target1).setOptions(opts);
//   // gridGauges.push(i);
//   console.log(i);
//   // gridGauges.
//   //   // create sexy gauge!

//   mewGauge.maxValue = 60; // set max gauge value
//   mewGauge.setMinValue(-10);  // Prefer setter over gauge.minValue = 0
//   mewGauge.animationSpeed = 32; // set animation speed (32 is default value)
//   mewGauge.set(20); // set actual value

// }
