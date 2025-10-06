from flask import Flask, jsonify, Response, send_from_directory, render_template
from flask_cors import CORS
import json, os

app = Flask(__name__, static_folder='frontend', template_folder='frontend')
CORS(app)

# Load provinces data
with open(os.path.join(os.path.dirname(__file__), 'provinces.json'), encoding='utf-8') as f:
    provinces = json.load(f)

@app.route('/api/provinces')
def get_provinces():
    ### Return JSON with Thai characters properly encoded
    
    return Response(json.dumps(provinces, ensure_ascii=False), mimetype='application/json')

# Serve the frontend index.html
#@app.route('/<path:path>')
#def serve_frontend(path):
 #   if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
  #      return send_from_directory(app.static_folder, path)
   # else:
    #    return send_from_directory(app.static_folder, 'index.html')

@app.route('/')
def index():
    return "Backend is running! Try /api/province?name=เชียงใหม่"

if __name__ == '__main__':
    app.run(debug=True)



