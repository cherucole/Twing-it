var myChart = document.querySelector("#myChart").getContext("2d");
var chartTwo = document.querySelector("#chartTwo").getContext("2d");
var legend = document.querySelector("#search").innerHTML;

var times = [];
var polarity = [];
var timeleft = 500;

var getData = $.get("/data");

polarity = [];
times = [];
subjectivity = [];
var data = [];

window.onload = function() {
  getData.done(function(results) {
    data = results["twing"];
    if (data.length != 0) {
      for (var i = 0; i < 15; i++) {
        polarity.push(i);
        times.push(data[i][3]);
        subjectivity.push(data[i][4]);
      }
    }
  });
};

increment = 15;

var chartLoader = setInterval(function() {
  times.push(data[increment][3]);
  console.log(times);
  polarity.push(increment);
  times = times.splice(1, times.length - 1);
  // console.log(times);
  polarity = polarity.splice(1, polarity.length - 1);
  subjectivity = subjectivity.splice(1, subjectivity.length - 1);

  if (timeleft <= 0) {
    handleFileSelect();
    timeleft = 5;
  }
  let sentimentChart = new Chart(myChart, {
    type: "line", //horizontalbar, pie, line, doughnut,radar, polarArea, bar
    data: {
      labels: polarity,
      datasets: [
        {
          label: legend,
          data: times,
          backgroundColor: [
            "rgba(255, 99, 132, 0.6)",
            "rgba(54, 162, 235, 0.6)",
            "rgba(255, 206, 86, 0.6)",
            "rgba(75, 192, 192, 0.6)",
            "rgba(153, 102, 255, 0.6)",
            "rgba(255, 159, 64, 0.6)",
            "rgba(255, 99, 132, 0.6)",
            "rgba(255, 99, 132, 0.6)",
            "rgba(54, 162, 235, 0.6)",
            "rgba(255, 206, 86, 0.6)",
            "rgba(75, 192, 192, 0.6)",
            "rgba(153, 102, 255, 0.6)",
            "rgba(255, 159, 64, 0.6)",
            "rgba(255, 99, 132, 0.6)",
            "rgba(255, 99, 132, 0.6)"
          ]
        }
      ]
    },
    options: {
      animation: false
    }
  });

  var polarityChart = new Chart(chartTwo, {
    type: "pie", //horizontalbar, pie, line, doughnut,radar, polarArea, bar
    data: {
      labels: subjectivity,
      datasets: [
        {
          label: "Senate",
          data: times
        },
        {
          label: "column2",
          data: times
        }
      ]
    },
    options: {
      animation: false
    }
  });

  timeleft = --timeleft;
  if (increment >= data.length - 2) {
    increment = 0;
  } else {
    increment++;
  }
}, 1000);
