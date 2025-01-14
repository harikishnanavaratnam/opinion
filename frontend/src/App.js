import React from 'react';
import ChartViewer from './components/ChartViewer';
import ReportGenerator from './components/ReportGenerator.js';
import './App.css';

function App() {
    const chartTypes = ['emotion', 'sentiment', 'trend', 'cluster'];

    return (
        <div className="App">
            <header className="dashboard-header">
                <h1>AI Chart Dashboard</h1>
                <p>Monitor and visualize data trends across AI ethics and sentiments.</p>
            </header>
            <div className="chart-grid">
                {chartTypes.map((type) => (
                    <ChartViewer key={type} graphType={type} />
                ))}
            </div>
            <ReportGenerator />
        </div>
    );
}

export default App;
