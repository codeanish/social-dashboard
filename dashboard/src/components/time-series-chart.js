import React, {useEffect, useRef, useState} from 'react';
import Chartjs from 'chart.js'

const chartConfig = {
    type: 'line',
    data: {
        labels: ["2020-11-01", "2020-11-02", "2020-11-03", "2020-11-04", "2020-11-05"],
        datasets: [
            {
                label: "Twitter followers",
                data: [101,105,108,103,111]
            }
        ]
    },
    options: {
        legend: {
            display: false
        },
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'day'
                }                
            }],
            yAxes: [{
                gridLines: {
                    display:false
                }   
            }]
        }
    }
};


const TimeSeriesChart = () => {
    const chartContainer = useRef(null);
    const [chartInstance, setChartInstance] = useState(null);

    useEffect(() => {
        if (chartContainer && chartContainer.current) {
          const newChartInstance = new Chartjs(chartContainer.current, chartConfig);
          setChartInstance(newChartInstance);
        }
      }, [chartContainer]);

    return (
        <div>
            <canvas ref={chartContainer} />
        </div>
    );
};

export default TimeSeriesChart;