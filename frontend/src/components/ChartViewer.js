import React, { useState } from 'react';

const ChartViewer = ({ graphType }) => {
  const [imageUrl, setImageUrl] = useState(null);

  const handleRefresh = async () => {
    try {
      // Fetch the image for the specified graph type from the Flask server
      const response = await fetch(`http://127.0.0.1:5000/run-script?type=${graphType}`);
      if (!response.ok) throw new Error('Failed to fetch image');

      // Convert the response to a Blob and create an object URL
      const blob = await response.blob();
      const objectUrl = URL.createObjectURL(blob);

      // Update the image URL state
      setImageUrl(objectUrl);
    } catch (error) {
      console.error('Error fetching image:', error);
    }
  };

  return (
    <div>
      <h1>Chart Viewer: {graphType}</h1>
      <button onClick={handleRefresh}>Refresh Chart</button>
      {imageUrl ? (
        <img src={imageUrl} alt={`${graphType} Chart`} style={{ width: '100%', height: 'auto' }} />
      ) : (
        <p>Click "Refresh" to generate the chart.</p>
      )}
    </div>
  );
};

export default ChartViewer;
