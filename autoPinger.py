import requests, time, asyncio

async def pingAtInterval():
	for x in range(0,30):
		code = requests.post("http://127.0.0.1:5000/heartbeat", data="ok")
		print(code.text, code.status_code)
		time.sleep(10)

asyncio.run(pingAtInterval())
