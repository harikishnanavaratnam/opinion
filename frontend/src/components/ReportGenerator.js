import React, { useState } from 'react';

const ReportGenerator = () => {
    const [isGenerating, setIsGenerating] = useState(false);
    const [error, setError] = useState(null);

    const generateReport = async () => {
        setIsGenerating(true);
        setError(null);

        try {
            // Make GET request to generate the report
            const response = await fetch('http://127.0.0.1:5000/api/generate_report', { method: 'GET' });

            if (response.ok) {
                // Get the blob (PDF file)
                const blob = await response.blob();

                // Create a download link for the file
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = 'AI_Ethics_Report.pdf';
                link.click();
            } else {
                setError('Failed to generate the report.');
            }
        } catch (err) {
            setError('Error generating report.');
        }

        setIsGenerating(false);
    };

    return (
        <div className="report-generator">
            <button onClick={generateReport} disabled={isGenerating}>
                {isGenerating ? 'Generating Report...' : 'Generate and Download Report'}
            </button>
            {error && <p>{error}</p>}
        </div>
    );
};

export default ReportGenerator;
