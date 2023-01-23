const drawStuff = function(ctx, data, pos_car) {
  ctx.fillStyle = "gray";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  offset = (canvas.width-100)/7;
  if (data && pos_car) {
    circle(ctx, data[0]['cpu_score_trust'], data[0]['ram_score_trust'], 50 + data[0]['x']*offset, 50 + data[0]['y']*offset)
    circle(ctx, data[1]['cpu_score_trust'], data[1]['ram_score_trust'], 50 + data[1]['x']*offset, 50 + data[1]['y']*offset);
    circle(ctx, data[2]['cpu_score_trust'], data[2]['ram_score_trust'], 50 + data[2]['x']*offset, 50 + data[2]['y']*offset);
    car(ctx, 50 + pos_car["x_car"]*offset, 50 + pos_car["y_car"]*offset);
    write(ctx, "cpu", 50 + data[0]['x']*offset -9, 50 + data[0]['y']*offset - 9);
    write(ctx, "ram", 50 + data[0]['x']*offset -10, 50 + data[0]['y']*offset + 12);
    write(ctx, "cpu", 50 + data[1]['x']*offset -9, 50 + data[1]['y']*offset - 9);
    write(ctx, "ram", 50 + data[1]['x']*offset -10, 50 + data[1]['y']*offset + 12);
    write(ctx, "cpu", 50 + data[2]['x']*offset -9, 50 + data[2]['y']*offset - 9);
    write(ctx, "ram", 50 + data[2]['x']*offset -10, 50 + data[2]['y']*offset + 12);
  }
}

const circle = function(ctx, s_cpu, s_ram, x, y) {
  ctx.fillStyle = getColor(s_cpu);
  ctx.beginPath();
  ctx.arc(x, y, 25, 0, Math.PI, false);
  ctx.fill();

  ctx.fillStyle = getColor(s_ram);
  ctx.beginPath();
  ctx.arc(x, y, 25, 0, Math.PI, true);
  ctx.fill();
}

const write = function(ctx, txt, x, y) {
  ctx.fillStyle = 'black';
  ctx.font = "10px Arial";
  ctx.fillText(txt,x,y);
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


const getColor = function(t) {
  let color
  if (t <= 0.1) {
    color = "#7F00FF";
  }
  else if (t <= 0.2) {
    color = "#0000FF";
  }
  else if (t <= 0.3) {
    color = "#007FFF";
  }
  else if (t <= 0.4) {
    color = "#00FFFF";
  }
  else if (t <= 0.5) {
    color = "#00FF7F";
  }
  else if (t <= 0.6) {
    color = "#00FF00";
  }
  else if (t <= 0.7) {
    color = "#7FFF00";
  }
  else if (t <= 0.8) {
    color = "#FFFF00";
  }
  else if (t <= 0.9) {
    color = "#FF7F00";
  }
  else {
    color = "#FF0000";
  }

  return color;
}