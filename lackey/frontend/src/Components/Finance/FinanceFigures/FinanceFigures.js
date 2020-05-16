import React from 'react';
import { VictoryLine, 
    VictoryChart, 
    VictoryTheme, 
    VictoryTooltip,
    VictoryVoronoiContainer } from 'victory';

const financeFigures = (props) => {
    const data = props.data;
    console.log(data)

    let figData = [];
    let index = 0;
    data.map(i => {
        figData.push({x: index++, y: i.close, date: i.date})
            }
    )   ;
    let style = {
        data: { stroke: "#c43a31" },
        parent: { border: "1px solid #ccc"}
      }
    /*let ticks = [];
    for(let x = 0; x < data.length; x++){
        ticks.push(x);
        x += 10
    }
    <VictoryAxis
    tickValues={ticks}
    tickFormat={''}
/> */
    return ( 
        <VictoryChart
            theme={VictoryTheme.material}
            containerComponent={
                <VictoryVoronoiContainer />}
        >
            <VictoryLine
                labelComponent={<VictoryTooltip />}
                labels={({ datum }) => `Close: ${datum.y}\nDate: ${datum.date}`}
                style={style}
                data={figData}
                x="x"
                y="y"
            />
        </VictoryChart>
     );
}
 
export default financeFigures;