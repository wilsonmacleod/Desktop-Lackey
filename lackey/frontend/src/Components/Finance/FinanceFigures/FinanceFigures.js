import React from 'react';
import { 
        VictoryLine, 
        VictoryChart, 
        VictoryAxis, 
        VictoryTooltip,
        VictoryVoronoiContainer
        } from 'victory';


const financeFigures = (props) => {
    const data = props.data;
    
    const style = {
        data: { stroke: "#DC143C", strokeWidth: 3 },
        axis: {stroke: "#f5f5f5", strokeWidth: 3 },
        grid : { stroke: "#797979", strokeWidth: 1},
        ticks: {stroke: "#f5f5f5", size: 5},
        tickLabels: {fill: "#f5f5f5"}
    }

    let figData = [];
    let range = [];
    let dates = [];
    data.map(i => {
        figData.splice(0, 0,{
            x: i.date, 
            y: i.close, 
            date: i.date,
            high: i.high,
            low: i.low,
            open: i.opening,
            close: i.close})
        range.push(i.close);
        dates.push(i.date);
            }
    );

    let min = Math.min(...range) * .90;
    let max = Math.max(...range) * 1.10;
    
    return ( 
        <VictoryChart
            height={230}
            width={400}
            padding={{ top: 10, bottom: 0, left: 35, right: 0 }}
            containerComponent={
                <VictoryVoronoiContainer />}
            minDomain={{ y: min }}
            maxDomain={{ y: max }}
        >
            <VictoryAxis 
                fixLabelOverlap
                style={style}
                />
            <VictoryAxis 
                tickCount={10}
                dependentAxis
                style={style}
            />
            <VictoryLine
                labelComponent={
                <VictoryTooltip 
                    constrainToVisibleArea
                    flyoutStyle={{ stroke: "#4ecdc4", strokeWidth: 2.5 }}
                    flyoutWidth={110}
                    flyoutHeight={55}
                    pointerWidth={10}
                    pointerHeight={5}
                    padding={0}
                    style={{ fill: "black", fontFamily: 'Ruda, sansSerif', fontSize:13, padding: 0}}
                 />}
                labels={({ datum }) => 
                `Close: ${datum.y}\nDate: ${String(datum.date).slice(0,10)}\nTime: ${String(datum.date).slice(11,16)}`}
                style={style}
                data={figData}
                x="x"
                y="y"
            />
        </VictoryChart>
     );
}
 
export default financeFigures;