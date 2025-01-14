from flask import Flask, request, send_file, jsonify
import subprocess
import os
from fpdf import FPDF
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PLOTS_DIR = os.path.join(app.root_path, 'static', 'plots')
os.makedirs(PLOTS_DIR, exist_ok=True)

scripts = {
    'emotion': {'script': 'emotion.py', 'image': 'emotion.png'},
    'sentiment': {'script': 'sentiment.py', 'image': 'sentiment.png'},
    'trend': {'script': 'trend.py', 'image': 'trend.png'},
    'cluster': {'script': 'cluster.py', 'image': 'cluster.png'}
}

@app.route('/run-script', methods=['GET'])
def generate_chart():
    graph_type = request.args.get('type', 'default')
    
    if graph_type in scripts:
        script_info = scripts[graph_type]
        script_path = script_info['script']
        image_path = script_info['image']

        try:
            if not os.path.exists(image_path):
                subprocess.run(['python', script_path], check=True)

            if os.path.exists(image_path):
                return send_file(image_path, mimetype='image/png')
            else:
                return jsonify({"error": f"Image not found for {graph_type}"}), 404
        except subprocess.CalledProcessError as e:
            return jsonify({"error": f"Error running {script_path}: {str(e)}"}), 500
    else:
        return jsonify({"error": "Invalid graph type"}), 400

@app.route('/api/generate_report', methods=['GET'])
def generate_report():
    try:
        for script_info in scripts.values():
            image_path = script_info['image']
            if not os.path.exists(image_path):
                subprocess.run(['python', script_info['script']], check=True)

        report_path = os.path.join(PLOTS_DIR, 'AI_Ethics_Report.pdf')
        create_pdf_report(report_path)

        return send_file(report_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def create_pdf_report(report_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="AI Ethics Discussion Report", ln=True, align='C')

    images = ['emotion.png', 'sentiment.png', 'trend.png', 'cluster.png']
    for image in images:
        image_path = image
        if os.path.exists(image_path):
            pdf.image(image_path, x=10, y=30, w=180)
            pdf.add_page()
        else:
            pdf.cell(200, 10, txt=f"Image {image} not found.", ln=True, align='C')

    pdf.output(report_path)

if __name__ == '__main__':
    app.run(debug=True)
