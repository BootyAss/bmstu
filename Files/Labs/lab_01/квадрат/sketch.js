var Cube = {
  curAngle: 0,
  r: 200,
  a: 50,
  x: 0,
  y: 200,
  dir: 1,
  speed: 0
}


function setup() {
  createCanvas(600, 600);
}

function draw() {
  background(255);

  if (Cube.dir > 0) {
    if (Cube.speed < 0.06) {
      Cube.speed += 0.002;
    }
  } else {
    if (Cube.speed > -0.06) {
      Cube.speed -= 0.002;
    }
  }

  Cube.x = sin(Cube.curAngle) * Cube.r;
  Cube.y = cos(Cube.curAngle) * Cube.r;
  Cube.curAngle += Cube.speed;

  fill(0, 0, 0);
  textSize(20);
  textAlign(CENTER);
  text("press any key", width / 2, height / 2 - 40);

  fill(200, 50, 50);
  rectMode(CENTER);
  rect(width / 2 + Cube.x, height / 2 + Cube.y, Cube.a, Cube.a);
}

function keyPressed() {
  Cube.dir *= -1;
}
