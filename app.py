from flask import Flask, render_template, request, jsonify, redirect, url_for
import tracemalloc, asyncio,  os, logging, requests, time

logging.basicConfig(filename="log.txt", level=logging.INFO, filemode="w")
logger = logging.getLogger(__name__)
logger.info("Log started")

app = Flask(__name__)

lastHeard = None

@app.route('/')
def main():
	if lastHeard:
		return render_template("main.html", lastHeard=float(time.time()-lastHeard))
	return render_template("main.html", lastHeard="<not heard from yet>")

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
	global lastHeard
	lastHeard = time.time()
	data = request.data
	print(data.decode())
	return "success", 200

@app.route('/heartbeat', methods=['GET'])
def heartbeatGet():
	global lastHeard
	return jsonify({"lastheard": lastHeard}), 200

@app.route("/fakeheartbeat", methods=["GET"])
def devHeartbeatEmulator():
	data = heartbeat()
	return redirect(url_for("main"), code=307)


if __name__ == "__main__":
	app.run(port=5000)
