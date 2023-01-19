const drawStuff = function(ctx, data) {
  ctx.fillStyle = "gray";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  offset = (canvas.width-100)/7;
  if (data) {
    console.log(data);
    circle(ctx, "yellow", 50 + data[0]['x']*offset, 50 + data[0]['y']*offset);
    circle(ctx, "yellow", 50 + data[1]['x']*offset, 50 + data[1]['y']*offset);
    circle(ctx, "yellow", 50 + data[2]['x']*offset, 50 + data[2]['y']*offset);
    car(ctx, 50 + data[3]['x']*offset, 50 + data[3]['y']*offset);
  }
}

const circle = function(ctx, color, x, y) {
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.arc(x, y, 15, (Math.PI / 180) * 0, (Math.PI / 180) * 360);
  ctx.fill();
}

const car = function(ctx, x, y) {
  silver = '#B2B2B2';

  // chassis
  ctx.fillStyle = '#5E5C1A';
  ctx.fillRect(x - 37.5, y - 10, 75, 15);

  // back wheel
  ctx.fillStyle = 'black';
  ctx.beginPath();
  ctx.arc(x - 17.5, y + 7, 7.5, 0, 2 * Math.PI);
  ctx.fill();
  ctx.fillStyle = silver;
  ctx.beginPath();
  ctx.arc(x - 17.5, y + 7, 3, 0, 2 * Math.PI);
  ctx.fill();

  // front wheel
  ctx.fillStyle = 'black';
  ctx.beginPath();
  ctx.arc(x + 17.5, y + 7, 7.5, 0, 2 * Math.PI);
  ctx.fill();
  ctx.fillStyle = silver;
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
  size_logo = 7.5;
  x_logo = x + 32.5;
  y_logo = y - 16;
  ctx.strokeStyle = silver;
  ctx.fillStyle = silver;
  ctx.fillRect(
    x_logo - 0.5,
    y_logo + size_logo / 2 + 1,
    1,
    1
  );
  ctx.beginPath();
  ctx.arc(x_logo, y_logo, size_logo / 2, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(x_logo, y_logo - size_logo / 2);
  ctx.lineTo(
    x_logo - (Math.sqrt(3) / 2) * (size_logo * 0.05),
    y_logo - 0.5 * (size_logo * 0.05)
  );
  ctx.lineTo(
    x_logo - (Math.sqrt(3) / 2) * (size_logo / 2),
    y_logo + 0.5 * (size_logo / 2)
  );
  ctx.lineTo(x_logo, y_logo + size_logo * 0.05);
  ctx.lineTo(
    x_logo + (Math.sqrt(3) / 2) * (size_logo / 2),
    y_logo + 0.5 * (size_logo / 2)
  );
  ctx.lineTo(
    x_logo + (Math.sqrt(3) / 2) * (size_logo * 0.05),
    y_logo - 0.5 * (size_logo * 0.05)
  );
  ctx.fill();
}
