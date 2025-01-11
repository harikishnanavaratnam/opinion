from flask import Flask, request, send_file
import subprocess
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/run-script', methods=['GET'])
def generate_chart():
    graph_type = request.args.get('type', 'default')

    # Map graph types to script names and image paths
    scripts = {
        'emotion': {'script': 'emotion.py', 'image': 'emotion.png'},
        'sentiment': {'script': 'sentiment.py', 'image': 'sentiment.png'},
        'trend': {'script': 'trend.py', 'image': 'trend.png'},
        'cluster':{'script':'cluster.py','image':'cluster.png'}
    }

    if graph_type in scripts:
        script_info = scripts[graph_type]
        script_path = script_info['script']
        image_path = script_info['image']

        try:
          
            subprocess.run(['python', script_path], check=True)

            if os.path.exists(image_path):
                return send_file(image_path, mimetype='image/png')
            else:
                return f"Image not found for {graph_type}", 404

        except subprocess.CalledProcessError as e:
            return f"Error running script {script_path}: {str(e)}", 500
    else:
        return "Invalid graph type", 400

if __name__ == '__main__':
    app.run(debug=True)
