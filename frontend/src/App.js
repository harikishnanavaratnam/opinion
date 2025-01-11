import React from 'react';
import ChartViewer from './components/ChartViewer';

function App() {
    return (
        <div className="App">
            <ChartViewer graphType="emotion"/>
            <ChartViewer graphType="sentiment"/>
            <ChartViewer graphType="trend"/>
            <ChartViewer graphType="cluster"/>
        </div>
    );
}

export default App;
