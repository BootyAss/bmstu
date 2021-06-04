var start = {
  x: 0,
  y: 0
}

var end = {
  x: 0,
  y: 0
}

var mouseIsReleased = false;
var reset = false;

function setup() {
  createCanvas(800, 800);
  background(255);

  topLayer = createGraphics(800, 800);
  bottomLayer = createGraphics(800, 800);
}

function draw() {
  if (reset) {
    
    for (let i = 0; i < topLayer.width; i++) {
      for (let j = 0; j < topLayer.width; j++) {
        topLayer.set(i, j, color(255, 255, 255, 0));
      }
    }
    updatePixels();
    reset = false;
  }

  drawBottom();
  drawTop();

  image(bottomLayer, 0, 0);
  image(topLayer, 0, 0);
}

function drawTop() {
  if (mouseIsReleased) {
    bottomLayer.background(255);
    drawLine(start.x, start.y, end.x, end.y);
    mouseIsReleased = false;
  }
}

function drawBottom() {
  if (mouseIsPressed) {
    bottomLayer.background(255);
    bottomLayer.strokeWeight(4);
    bottomLayer.stroke(255, 75, 75);
    bottomLayer.line(start.x, start.y, mouseX, mouseY);
  }
}

function drawLine(x0, y0, x1, y1) {
  var dx = Math.abs(x1 - x0);
  var dy = Math.abs(y1 - y0);
  var sx = (x0 < x1) ? 1 : -1;
  var sy = (y0 < y1) ? 1 : -1;
  var err = dx - dy;

  while (true) {
    if (Math.abs(x0 - x1) < 0.0001 && Math.abs(y0 - y1) < 0.0001)
      break;
    var e2 = 2 * err;
    if (e2 > -dy) {
      err -= dy;
      x0 += sx;
    }
    if (e2 < dx) {
      err += dx;
      y0 += sy;
    }
    topLayer.set(x0, y0, 0);
    topLayer.updatePixels();
  }
}

function mousePressed() {
  start.x = mouseX;
  start.y = mouseY;
}

function mouseReleased() {
  end.x = mouseX;
  end.y = mouseY;
  mouseIsReleased = true;
}

function keyPressed() {
  if (key === 'r') {
    reset = true;
  }
}