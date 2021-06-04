var img;
var orig = [];
var resetButton, bwButton, invertButton;

function preload() {
  img = loadImage('https://bootyass.github.io/Files/Photos/Frog.png');
}

function setup() {
  createCanvas(500, 500);

  img.resize(500, 500);

  drawImg();

  for (let i = 0; i < img.width; i++) {
    orig[i] = [];
    for (let j = 0; j < img.height; j++) {
      orig[i][j] = img.get(i, j);
    }
  }

  resetButton = createButton('Reset');
  resetButton.position(50, 580);
  resetButton.size(150, 40);
  resetButton.mousePressed(Reset);

  bwButton = createButton('BW mode');
  bwButton.position(225, 580);
  bwButton.size(150, 40);
  bwButton.mousePressed(BW);

  invertButton = createButton('Invert mode');
  invertButton.position(400, 580);
  invertButton.size(150, 40);
  invertButton.mousePressed(Invert);
}


function drawImg() {
  image(img, 0, 0);
}

function BW() {
  clear();
  background(200);

  for (let i = 0; i < img.width; i++) {
    for (let j = 0; j < img.height; j++) {
      img.set(i, j, (orig[i][j][0] + orig[i][j][1] + orig[i][j][2]) / 3);
    }
  }

  img.updatePixels();
  drawImg();
}

function Invert() {
  clear();
  background(200);

  for (let i = 0; i < img.width; i++) {
    for (let j = 0; j < img.height; j++) {
      img.set(i, j, color(255 - orig[i][j][0], 255 - orig[i][j][1], 255 - orig[i][j][2]));
    }
  }

  img.updatePixels();
  drawImg();
}

function Reset() {
  clear();
  background(200);


  for (let i = 0; i < img.width; i++) {
    for (let j = 0; j < img.height; j++) {
      img.set(i, j, orig[i][j]);
    }
  }

  img.updatePixels();
  drawImg();
}