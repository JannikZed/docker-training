from flask import Flask
from datetime import datetime
from flask_cors import CORS
from redis import Redis

app = Flask(__name__)
CORS(app)
cache = Redis(host='redis', port=6379)

@app.route("/api/v1/time")
def get_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cache.set("last_time", current_time)
    return f"Current time: {current_time}"

@app.route("/api/v1/last_time")
def get_last_time():
    response = cache.get('last_time')
    if response is None:
        return ""
    else:
        return f"Last time: {response.decode('utf-8')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
