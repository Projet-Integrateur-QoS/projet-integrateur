// app.js

require('dotenv').config();
const express = require("express");
const app = express()
const path = require('path');
const front_port = process.env.FRONT_PORT
const sim_port = process.env.SIMULATOR_PORT

if (!front_port) {
  console.log("FRONTEND PORT UNDEFINED")
  exit()
}

app.listen(front_port, () => console.log(`The server is listening on port ${front_port}`))

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname+'/index.html'));
});
