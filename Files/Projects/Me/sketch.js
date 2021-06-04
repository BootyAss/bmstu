var masks = [];
var sizeX = 1920;
var sizeY = 1080;
var amount = 25;
var img = [];

function preload() {
  for (let i = 0; i < amount; i++) {
    img[i] = loadImage('https://bootyass.github.io/Files/img/Temp.png');
  }
}

function setup() {
  createCanvas(sizeX, sizeY);

  for (let i = 0; i < amount; i++) {
    x = random(-10, sizeX + 10);
    y = random(0, sizeY + 5);
    z = random(0.4, 1);
    masks.push(new Mask(x, y, z, i));
  }
}


function draw() {
  background(20, 20, 20);
  for (let i = 0; i < amount; i++) {
    masks[i].fall();
    masks[i].draw();
  }

}