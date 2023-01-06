const circle = function(ctx, color, x, y) {
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.arc(x, y, 15, (Math.PI / 180) * 0, (Math.PI / 180) * 360);
  ctx.fill();
}

const car = function(ctx, x, y) {
  // chassis
  ctx.fillStyle = this.voiture;
  ctx.fillRect(x - 37.5, y - 10, 75, 15);

  // back wheel
  ctx.fillStyle = 'black';
  ctx.beginPath();
  ctx.arc(x - 17.5, y + 7, 7.5, 0, 2 * Math.PI);
  ctx.fill();
  ctx.fillStyle = this.silver;
  ctx.beginPath();
  ctx.arc(x - 17.5, y + 7, 3, 0, 2 * Math.PI);
  ctx.fill();

  // front wheel
  ctx.fillStyle = 'black';
  ctx.beginPath();
  ctx.arc(x + 17.5, y + 7, 7.5, 0, 2 * Math.PI);
  ctx.fill();
  ctx.fillStyle = this.silver;
  ctx.beginPath();
  ctx.arc(x + 17.5, y + 7, 3, 0, 2 * Math.PI);
  ctx.fill();

  // cabin
  ctx.fillStyle = 'black';
  ctx.beginPath();
  ctx.moveTo(x - 12.5, y - 17.5);
  ctx.lineTo(x + 12.5, y - 17.5);
  ctx.lineTo(x + 22.5, y - 9);
  ctx.lineTo(x - 22.5, y - 9);
  ctx.fill();

  // logo
  this.x_logo = x + 32.5;
  this.y_logo = y - 16;
  ctx.strokeStyle = this.silver;
  ctx.fillStyle = this.silver;
  ctx.fillRect(
    this.x_logo - 0.5,
    this.y_logo + this.size_logo / 2 + 1,
    1,
    1
  );
  ctx.beginPath();
  ctx.arc(this.x_logo, this.y_logo, this.size_logo / 2, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(this.x_logo, this.y_logo - this.size_logo / 2);
  ctx.lineTo(
    this.x_logo - (Math.sqrt(3) / 2) * (this.size_logo * 0.05),
    this.y_logo - 0.5 * (this.size_logo * 0.05)
  );
  ctx.lineTo(
    this.x_logo - (Math.sqrt(3) / 2) * (this.size_logo / 2),
    this.y_logo + 0.5 * (this.size_logo / 2)
  );
  ctx.lineTo(this.x_logo, this.y_logo + this.size_logo * 0.05);
  ctx.lineTo(
    this.x_logo + (Math.sqrt(3) / 2) * (this.size_logo / 2),
    this.y_logo + 0.5 * (this.size_logo / 2)
  );
  ctx.lineTo(
    this.x_logo + (Math.sqrt(3) / 2) * (this.size_logo * 0.05),
    this.y_logo - 0.5 * (this.size_logo * 0.05)
  );
  ctx.fill();
}

module.exports = {
  circle, car
}