var img;
var orig = [];
var resetButton, bwButton, invertButton;

function preload() {
  img = loadImage('https://bootyass.github.io/Files/Photos/Frog.png');
}

function setup() {
  createCanvas(650, 500);

  background(245);

  img.resize(width - 100, height - 100);

  drawImg();

  for (let i = 0; i < img.width; i++) {
    orig[i] = [];
    for (let j = 0; j < img.height; j++) {
      orig[i][j] = img.get(i, j);
    }
  }

  resetButton = createButton('Reset');
  bwButton = createButton('BW mode');
  invertButton = createButton('Invert mode');
  sobelButton = createButton('Sobel filter');

  resetButton.mousePressed(Reset);
  bwButton.mousePressed(BW);
  invertButton.mousePressed(Invert);
  sobelButton.mousePressed(Sobel);

  resetButton.size(width / 3, 50);
  bwButton.size(width / 3, 50);
  invertButton.size(width / 3, 50);
  sobelButton.size(width / 3, 50);

  resetButton.position(800, 220);
  bwButton.position(800, 280);
  invertButton.position(800, 340);
  sobelButton.position(800, 400);

  resetButton.style('font-size', '20px');
  bwButton.style('font-size', '20px');
  invertButton.style('font-size', '20px');
  sobelButton.style('font-size', '20px');

  resetButton.style('border-radius', '6px');
  bwButton.style('border-radius', '6px');
  invertButton.style('border-radius', '6px');
  sobelButton.style('border-radius', '6px');
}


function drawImg() {
  image(img, 50, 50);
  //h1 = select('h1').position(500, 500);
}

function BW() {
  clear();
  background(245);

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
  background(245);

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
  background(245);


  for (let i = 0; i < img.width; i++) {
    for (let j = 0; j < img.height; j++) {
      img.set(i, j, orig[i][j]);
    }
  }

  img.updatePixels();
  drawImg();
}

Gx = [
  [-1, -2, -1],
  [0, 0, 0],
  [1, 2, 1]
];
Gy = [
  [-1, 0, 1],
  [-2, 0, 2],
  [-1, 0, 1]
];

function Sobel() {
  for (let x = 1; x < img.width - 1; x++) {
    for (let y = 1; y < img.height - 1; y++) {
      X = 0;
      Y = 0;

      // thats a clean code but ...
      // for (let i = 0; i < 3; i++) {
      //   for (let j = 0; j < 3; j++) {
      //     I = x + i - 1;
      //     J = y + j - 1;
      //     temp = (orig[I][J][0] + orig[I][J][1] + orig[I][J][2]) / 3;
      //     X += temp * Gx[i][j];
      //     Y += temp * Gy[i][j];
      //   }
      // }

      // thats faster
      temp = (orig[x - 1][y - 1][0] + orig[x - 1][y - 1][1] + orig[x - 1][y - 1][2]) / 3;
      X += temp * Gx[0][0];
      Y += temp * Gy[0][0];

      temp = (orig[x][y - 1][0] + orig[x][y - 1][1] + orig[x][y - 1][2]) / 3;
      X += temp * Gx[1][0];
      Y += temp * Gy[1][0];

      temp = (orig[x + 1][y - 1][0] + orig[x + 1][y - 1][1] + orig[x + 1][y - 1][2]) / 3;
      X += temp * Gx[2][0];
      Y += temp * Gy[2][0];

      temp = (orig[x - 1][y][0] + orig[x - 1][y][1] + orig[x - 1][y][2]) / 3 ;
      X += temp * Gx[0][1];
      Y += temp * Gy[0][1];

      temp = (orig[x + 1][y][0] + orig[x + 1][y][1] + orig[x + 1][y][2]) / 3 ;
      X += temp * Gx[2][1];
      Y += temp * Gy[2][1];

      temp = (orig[x - 1][y + 1][0] + orig[x - 1][y + 1][1] + orig[x - 1][y + 1][2]) / 3 ;
      X += temp * Gx[0][2];
      Y += temp * Gy[0][2];

      temp = (orig[x][y + 1][0] + orig[x][y + 1][1] + orig[x][y + 1][2]) / 3 ;
      X += temp * Gx[1][2];
      Y += temp * Gy[1][2];

      temp = (orig[x + 1][y + 1][0] + orig[x + 1][y + 1][1] + orig[x + 1][y + 1][2]) / 3;
      X += temp * Gx[2][2];
      Y += temp * Gy[2][2];

      s = sqrt(sq(X) + sq(Y));
      img.set(x, y, color(s, s, s));
    }
  }
  img.updatePixels();
  drawImg();
}