import React, { useState } from 'react';

const ChartViewer = ({ graphType }) => {
    const [imageUrl, setImageUrl] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const handleRefresh = async () => {
        try {
            setIsLoading(true); // Disable button during fetch
            const response = await fetch(`http://127.0.0.1:5000/run-script?type=${graphType}`);
            if (!response.ok) throw new Error('Failed to fetch image');
            const blob = await response.blob();
            const objectUrl = URL.createObjectURL(blob);
            setImageUrl(objectUrl);
        } catch (error) {
            console.error('Error fetching image:', error);
        } finally {
            setIsLoading(false); // Re-enable button after fetch
        }
    };

    return (
        <div className="chart-viewer">
            <h1>Chart Viewer: {graphType}</h1>
            <button onClick={handleRefresh} disabled={isLoading}>
                {isLoading ? 'Loading...' : 'Refresh Chart'}
            </button>
            {imageUrl ? (
                <img src={imageUrl} alt={`${graphType} Chart`} style={{ width: '100%', height: 'auto' }} />
            ) : (
                <p>Click "Refresh" to generate the chart.</p>
            )}
        </div>
    );
};

export default ChartViewer;
