from flask import Flask, render_template, jsonify, request
import psutil
import subprocess

app = Flask(__name__)

# 1. Frontend Route: Serves your portfolio website
@app.route('/')
def home():
    return render_template('index.html')

# 2. Telemetry API: Returns live Raspberry Pi hardware metrics
@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    return jsonify({
        'cpu_percent': cpu_usage,
        'memory_percent': memory.percent
    })

# 3. CI/CD Webhook: Listens for GitHub pushes to auto-update
@app.route('/webhook/github', methods=['POST'])
def github_webhook():
    # In a production environment, you would validate a secret token here
    try:
        subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
        return jsonify({"status": "success", "message": "Code updated"}), 200
    except subprocess.CalledProcessError:
        return jsonify({"status": "error", "message": "Git pull failed"}), 500

if __name__ == '__main__':
    # Runs the server on port 5000, accessible to your Cloudflare tunnel
    app.run(host='0.0.0.0', port=5000)
