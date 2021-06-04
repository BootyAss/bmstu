var cell = 20,
  cX = 20,
  cY = 20;

var snake = {
  cells: [],
  aX: 1,
  aY: 0,
  length : 1,
  add: false
};

var apple = {
  x: 0,
  y: 0
}


function setup() {
  createCanvas(cell * cX, cell * cY);

  snake.cells.push([floor(random(0, cX)), floor(random(0, cY))]);
  randomize();
  
  scoretxt = createP('Score:');
  score = createP('1');
}


function draw() {  
  frameRate(select('#speedSlider').value());
  background(255);
  
  drawNet();

  EatCheck();

  Update();

  drawSnake();

  drawApple();
  
  turn();
  
  endCheck();
    
  score.html(snake.length);
  score.position(500, 475);
  score.style('margin', '40px 20px');
  score.style('font-family','Lucida Calligraphy');
  score.style('font-size', '50px');
  
  scoretxt.position(400, 495);
  scoretxt.style('font-family','Lucida Calligraphy');
  scoretxt.style('font-size', '30px');
  scoretxt.style('margin', '40px 20px');
}


function drawNet() {
  for (let i = 0; i < cX; i++) {
    line(i * cell, 0, i * cell, cY * cell);
  }
  for (let i = 0; i < cX; i++) {
    line(0, i * cell, cX * cell, i * cell);
  }
}


function drawSnake() {
  fill(75, 220, 75);
  for (let i = 0; i < snake.length; i++) {
    rect(snake.cells[i][0] * cell, snake.cells[i][1] * cell, cell, cell);
  }
}


function randomize() {
  apple.x = floor(random(0, cX));
  apple.y = floor(random(0, cY));

  for (let i = 0; i < snake.length; i++) {
    if (snake.cells[i][0] == apple.x && snake.cells[i][1] == apple.y) {
      randomize();
      break;
    }
  }
}


function drawApple() {
  fill(220, 75, 75);
  rect(apple.x * cell, apple.y * cell, cell, cell);
}


function Update() {
  length = snake.length;
  if (snake.add) {
    length -= 1;
  }
  
  for (let i = length - 1; i > 0; i--) {
    snake.cells[i][0] = snake.cells[i - 1][0];
    snake.cells[i][1] = snake.cells[i - 1][1];
  }

  snake.add = false;

  snake.cells[0][0] += snake.aX;
  if (snake.cells[0][0] >= cX) {
    snake.cells[0][0] = 0;
  }
  if (snake.cells[0][0] < 0) {
    snake.cells[0][0] = cX - 1;
  }

  snake.cells[0][1] += snake.aY;
  if (snake.cells[0][1] >= cY) {
    snake.cells[0][1] = 0;
  }
  if (snake.cells[0][1] < 0) {
    snake.cells[0][1] = cY - 1;
  }
}


function EatCheck() {
  if (snake.cells[0][0] == apple.x && snake.cells[0][1] == apple.y) {
    snake.cells.push([snake.cells[snake.length - 1][0], snake.cells[snake.length - 1][1]]);
    snake.length += 1;
    snake.add = true;
    
    randomize();
  }
}


let tX = 0, tY = 0;
function keyPressed() {
  if (key === 'w' && snake.aY != 1) {
    tX = 0;
    tY = -1;
  }
  if (key === 'a' && snake.aX != -1) {
    tX = -1;
    tY = 0;
  }
  if (key === 's' && snake.aY != -1) {
    tX = 0;
    tY = 1;
  }
  if (key === 'd' && snake.aX != -1) {
    tX = 1;
    tY = 0;
  }

}


function turn() {
  if (snake.aX != -tX) {
    snake.aX = tX;
  }
  if (snake.aY != -tY) {
    snake.aY = tY;
  }
}


function endCheck() {
  for (let i = 1; i < snake.length; i++) {
    if (snake.cells[i][0] == snake.cells[0][0] && snake.cells[i][1] == snake.cells[0][1]) {
      snake.cells = [];
      snake.cells.push([floor(random(0, cX)), floor(random(0, cY))]);
      snake.length = 1;
    }
  }
}
