// src/plotting.js

const chart = new Chart("chart", {
  type: "line",
  data: {
    datasets: [{
        borderColor: "#007cfb",
        backgroundColor: "#0062c5",
      }
    ]
  },
  options: {
    plugins: {
      legend: {display: false},
      tooltip: {enabled: true},
    },
    scales: {
      x: {
        display: true,
        // Round the numbers on the x axis (ticks) to the nearest int
        // https://stackoverflow.com/questions/63821723/how-can-i-remove-the-decimals-from-the-tick-when-im-zooming
        // https://www.chartjs.org/docs/latest/samples/scale-options/ticks.html
        ticks: {callback: value => Math.round(value)}
      },
      y: {display: true}
    },
  }
})

function updateChart(xValues, yValues) {
  chart.data.labels = xValues
  chart.data.datasets[0].data = yValues
  chart.update()
}
