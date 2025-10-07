import os

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/static/<path:path>")
def favicon():
    return send_file('src/static/icons/favicon.ico', mimetype='image/vnd.microsoft.icon')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
