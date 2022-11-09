// 그래프1
google.charts.load('current', {'packages':['line', 'corechart']});
      google.charts.setOnLoadCallback(drawChart1);
      google.charts.setOnLoadCallback(drawChart2);

    function drawChart1() {

      var data = new google.visualization.DataTable();
      data.addColumn('number', '기간');
      data.addColumn('number', '기획금액');
      data.addColumn('number', '총매표액');
      data.addColumn('number', '제작금액');

      data.addRows([
        [1,  37.8, 80.8, 41.8],
        [2,  30.9, 69.5, 32.4],
        [3,  25.4,   57, 25.7],
        [4,  11.7, 18.8, 10.5],
        [5,  11.9, 17.6, 10.4],
        [6,   8.8, 13.6,  7.7],
        [7,   7.6, 12.3,  9.6],
        [8,  12.3, 29.2, 10.6],
        [9,  16.9, 42.9, 14.8],
        [10, 12.8, 30.9, 11.6],
        [11,  5.3,  7.9,  4.7],
        [12,  6.6,  8.4,  5.2],
        [13,  4.8,  6.3,  3.6],
        [14,  4.2,  6.2,  3.4]
      ]);

      var options = {
        chart: {
          title: '총 매출액 변동 추이',
          subtitle: '원 기준'
        },
        width: 900,
        height: 500
      };

      var chart = new google.charts.Line(document.getElementById('curve_chart'));

      chart.draw(data, google.charts.Line.convertOptions(options));
    }

// 그래프2
      function drawChart2() {
        var data = google.visualization.arrayToDataTable([
          ['년도', '매표수', '관객수'],
          ['2019',  1000,      400],
          ['2020',  1170,      460],
          ['2021',  660,       1120],
          ['2022',  1030,      540]
        ]);

        var options = {
          title: '흥행률',
          hAxis: {title: '년도',  titleTextStyle: {color: '#333'}},
          vAxis: {minValue: 0}
        };

        var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }