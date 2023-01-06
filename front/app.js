// app.js

const express = require("express")
const app = express()
const port = 4000

app.listen(port, () => console.log(`The server is listening on port ${port}`))

const { createCanvas } = require('canvas')
const canvas = createCanvas(1000, 1000)
const ctx = canvas.getContext('2d')
ctx.fillStyle = "gray";
ctx.fillRect(0, 0, canvas.width, canvas.height);

jaune = '#FFD733';
vert = '#94D800';
voiture = '#5E5C1A';
silver = '#B2B2B2';

const draw = require("./draw")

draw.circle(ctx, jaune, 500, 500)
draw.car(ctx, 100, 100)

let x = 0
setInterval(function(){
  draw.circle(ctx, x, 500)
  x += 100
  console.log("test " + x)
}, 1000);

app.get("/", (req, res) => {
    res.setHeader('Content-Type', 'image/png');
    canvas.pngStream().pipe(res);
});

