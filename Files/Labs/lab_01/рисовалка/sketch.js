var released = false;

var lines = [];
var amount = 0;

var reset = false;

var start = {
  x: 0,
  y: 0
}

var end = {
  x: 0,
  y: 0
}

function setup() {
  createCanvas(1700, 800);
}

function draw() {
  if (reset) {
    clear();
    reset = !reset;
  }

  background(255);

  fill(0);
  textSize(20);
  text("R - reset", 50, 50);

  strokeWeight(4);
  fill(0, 0, 0);
  if (mouseIsPressed) {
    line(start.x, start.y, mouseX, mouseY);
  }

  for (let i = 0; i < amount; i++) {
    let l = lines[i];
    line(l[0], l[1], l[2], l[3]);
  }
}

function mousePressed() {
  start.x = mouseX;
  start.y = mouseY;
}

function mouseReleased() {
  append(lines, [start.x, start.y, mouseX, mouseY]);
  amount++;
}

function keyPressed() {
  if (key === 'r') {
    lines.splice(0, lines.length);
    amount = 0;
    reset = !reset;
  }
}