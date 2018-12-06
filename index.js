var express = require("express");
var twilio = require("twilio");

let app = express();
app.post('/voice', (req, res) => {
	console.log("Call Recieved");
	let audioURL = "http://jokes.ednerd.net/new.mp3";
	let twiml = new twilio.TwimlResponse();
	twiml.play(audioURL);
	res.send(twiml.toString());
});

app.listen(3000, () => console.log("Listening at :3000"));

