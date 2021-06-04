class Mask {
  constructor(x, y, z, i) {
    this.x = x;
    this.y = y;
    this.z = z;
    this.i = i;
    img[this.i].resize(200 * this.z, 200 * this.z);

  }
  
  draw() {
    image(img[this.i], this.x, this.y);
  }
  
  fall() {
    let speed = this.z;
    this.y += speed;
    if (this.y > sizeY + 10) {
      this.y = -100;
    }
  }
}

