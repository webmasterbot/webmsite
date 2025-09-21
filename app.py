from flask import Flask, render_template
import tracemalloc, asyncio,  os, logging, requests

logging.basicConfig(filename="log.txt", level=logging.INFO, filemode="w")
logger = logging.getLogger(__name__)
logger.info("Log started")

app = Flask(__name__)

@app.route('/')
def main():
	return render_template("main.html", botStatus="All good")

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
	return

if __name__ == "__main__":
	app.run(port=5000)
