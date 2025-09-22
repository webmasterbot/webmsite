from flask import Flask, render_template, request
import tracemalloc, asyncio,  os, logging, requests, time

logging.basicConfig(filename="log.txt", level=logging.INFO, filemode="w")
logger = logging.getLogger(__name__)
logger.info("Log started")

app = Flask(__name__)

lastHeard = "Not heard from"

@app.route('/')
def main():
	return render_template("main.html", lastHeard=time.time()-lastHeard)

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
	global lastHeard
	lastHeard = time.time()
	data = request.data
	print(data.decode())
	return 200

@app.route('/heartbeat', methods=['GET'])
def heartbeatGet():
	return str(time.time()-lastHeard)

if __name__ == "__main__":
	app.run(port=5000)
