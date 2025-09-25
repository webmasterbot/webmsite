const lastHeardSpan = document.getElementById("lastHeardSpan");
const lastHeardBox = document.getElementById("lastHeardBox");
var lastBeat = null;



function tick() {
	if (lastBeat) {
		const now = Date.now() / 1000;
		const diff = now - lastBeat;
		lastHeardSpan.textContent = diff;
		if (diff <= 10) {
			lastHeardBox.style.backgroundColor = "green"
		} else if (diff > 10 && diff <=15) {
			lastHeardBox.style.backgroundColor = "yellow"
		} else if (diff > 15) {
			lastHeardBox.style.backgroundColor = "red"
		}
	} else {
		lastHeardSpan.textContent = "(waiting for data...)"
		lastHeardBox.style.backgroundColor = "grey";
	}

};



async function updateLastBeat() {
	try {
		const r = await fetch("/heartbeat");
		const data = await r.json();
		lastBeat = data.lastheard;
	} catch {
		lastBeat = null;
	}
};

setInterval(updateLastBeat, 5000);
setInterval(tick, 1000);
updateLastBeat();
tick();
