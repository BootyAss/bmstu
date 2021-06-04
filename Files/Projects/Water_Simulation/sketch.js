let cols;
let rows;
let current;
let previous;

let dampening = 0.9999;

function setup() {
  pixelDensity(1);
  createCanvas(1200, 800);
  cols = width;
  rows = height;
  
  current = new Array(cols).fill(0).map(n => new Array(rows).fill(0));
  previous = new Array(cols).fill(0).map(n => new Array(rows).fill(0));
}

function mouseDragged() {
  previous[mouseX][mouseY] = 2000;
}

function mousePressed() {
  previous[mouseX][mouseY] = 2000;
}

function draw() {
  background(0);

  loadPixels();
  for (let i = 1; i < cols - 1; i++) {
    for (let j = 1; j < rows - 1; j++) {
      current[i][j] =
        (previous[i - 1][j] +
          previous[i + 1][j] +
          previous[i][j - 1] +
          previous[i][j + 1]) /
          2 -
        current[i][j];
      current[i][j] = current[i][j] * dampening;
      let index = (i + j * cols) * 4;
      pixels[index + 0] = current[i][j];
      pixels[index + 1] = current[i][j];
      pixels[index + 2] = current[i][j];
    }
  }
  updatePixels();

  let temp = previous;
  previous = current;
  current = temp;
}