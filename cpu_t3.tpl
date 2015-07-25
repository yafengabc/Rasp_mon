<html>
<head>
<title>TestChart.js</title>
</head>
<body>
<script
src="http://lib.sinaapp.com/js/jquery/1.9.1/jquery-1.9.1.min.js"></script>

<script src="http://code.highcharts.com/highcharts.js"></script>
<script src="http://code.highcharts.com/modules/exporting.js"></script>

<div id="container" style="min-width: 400px; height: 400px; margin: 0
auto"></div>
<script>
var chart = new Highcharts.Chart({
	chart: {
		renderTo: 'container',
		type: 'line',
		marginRight: 130,
		marginBottom: 25
	},
	title: {
		text: 'CPU Temperature',
		x: -20 //center
	},
	xAxis: {
		categories: {{!label}}
	},
	yAxis: {
		title: {
			text: 'Temperature (°C)'
		},
		plotLines: [{
			value: 0,
			width: 1,
			color: '#808080'
		}]
	},
	tooltip: {
		formatter: function() {
				return '<b>'+ this.series.name +'</b><br/>'+
				this.x +': '+ this.y +'°C';
		}
	},
	legend: {
		layout: 'vertical',
		align: 'right',
		verticalAlign: 'top',
		x: -10,
		y: 100,
		borderWidth: 0
	},
	series: [{
		name: 'CPU Temp',
		data: {{data}}
	}]
});
</script>
</html>
