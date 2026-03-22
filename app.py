from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask microservice app running"

@app.route("/info")
def info():
    return {
        "app": "flask-microservice-app",
        "status": "running",
        "environment": os.getenv("APP_ENV"),
        "redis_host": os.getenv("REDIS_HOST"),
        "db_host": os.getenv("DB_HOST")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)