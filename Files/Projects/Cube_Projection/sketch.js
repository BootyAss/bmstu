/// Просто Объявления
var points = [8];
var pVec = [8];

var projection = [
  []
];

var rX = [
  []
];
var rY = [
  []
];
var rZ = [
  []
];

var angle = 0;

var alp = 204;
///

function setup() {
  createCanvas(800, 800);

  /// Заполняем координаты точек
  for (let i = 0; i < 8; i++) {
    let x = 1 - 2 * int(i / 4);
    let z = 1 - 2 * (i % 2);
    let y = 1 - 2 * (int(i / 2) % 2);


    // В Массив
    points[i] = [
      [x],
      [y],
      [z]
    ];

    // В Вектор
    pVec[i] = createVector(points[i][0][0], points[i][1][0], points[i][2][0]);
   }
}


function draw() {
  background(0);
  
  fill(255);
  noStroke();
  textAlign(CENTER);
  textSize(20);
  text("move ur mouse\npress any button", 400, 100);

  /// Матрицы поворота
  rX = [
    [1, 0, 0],
    [0, cos(angle), -sin(angle)],
    [0, sin(angle), cos(angle)]
  ];
  rY = [
    [cos(angle), 0, sin(angle)],
    [0, 1, 0],
    [-sin(angle), 0, cos(angle)]
  ];
  rZ = [
    [cos(angle), -sin(angle), 0],
    [sin(angle), cos(angle), 0],
    [0, 0, 1]
  ];


  for (let i = 0; i < 8; i++) {
    /// Вращаем по 3 осям 
    let rotatedV = matMult(rX, points[i]);
    rotatedV = matMult(rY, rotatedV);
    rotatedV = matMult(rZ, rotatedV);

    /// Задаем дистанцию до точек (для перспективы)
    let distance = 3;
    let Z = 1 / (distance - rotatedV[2][0]);

    // Для каждой точки свое растояние в матрице проекции
    projection = [
      [Z, 0, 0],
      [0, Z, 0],
      [0, 0, 0]
    ];

    let projectOn2D = matMult(projection, rotatedV);

    /// Переводим в Вектор
    pVec[i] = createVector(projectOn2D[0][0], projectOn2D[1][0], projectOn2D[2][0]);

    /// Увеличиваем в размере
    pVec[i].mult(300);

    /// Смещаем в центр
    pVec[i].add(400, 400, 0);


    stroke(255);
    strokeWeight(map(mouseX, 0, 600, 1, 20));
    point(pVec[i].x, pVec[i].y);

  }

  /// Делаем линии
  stroke(255, alp);
  strokeWeight(map(mouseY, 0, 600, 1, 150));
  line(pVec[0].x, pVec[0].y, pVec[1].x, pVec[1].y);
  line(pVec[1].x, pVec[1].y, pVec[3].x, pVec[3].y);
  line(pVec[2].x, pVec[2].y, pVec[3].x, pVec[3].y);
  line(pVec[2].x, pVec[2].y, pVec[0].x, pVec[0].y);
  
  line(pVec[4].x, pVec[4].y, pVec[5].x, pVec[5].y);
  line(pVec[4].x, pVec[4].y, pVec[6].x, pVec[6].y);
  line(pVec[5].x, pVec[5].y, pVec[7].x, pVec[7].y);
  line(pVec[6].x, pVec[6].y, pVec[7].x, pVec[7].y);

  line(pVec[0].x, pVec[0].y, pVec[4].x, pVec[4].y);
  line(pVec[1].x, pVec[1].y, pVec[5].x, pVec[5].y);
  line(pVec[2].x, pVec[2].y, pVec[6].x, pVec[6].y);
  line(pVec[3].x, pVec[3].y, pVec[7].x, pVec[7].y);

  angle += 0.02;
}

function keyPressed() {
  alp += 51
  if (alp > 255) {
    alp = 0;
  }
}