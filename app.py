import subprocess
import os
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def main():
    hostname = os.getenv("HOSTNAME")
    return "<h1>Welcome!</h1>  <h2>This is the node " + str(hostname) + "</h2>"

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    result_status = {"services": {}, "overall": "OK"}

    services = ["sshd", "mysqld"]

    for service in services:
        process = subprocess.run(["service", service, "status"], capture_output=True, text=True)
        if process.returncode  != 0 :
            result_status["services"][service] =  {"status": "KO", "error_message": process.stderr}
            result_status["overall"] =  "KO"
        else:
            result_status["services"][service] =  {"status": "OK"}

    return jsonify(result_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
