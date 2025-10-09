from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    build = os.getenv("BUILD", "local")
    return f"Hello from Flask containerized app! Build: {build}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
