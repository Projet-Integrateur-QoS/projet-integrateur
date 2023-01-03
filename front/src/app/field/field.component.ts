import { NgIfContext } from '@angular/common';
import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-field',
  // templateUrl: './field.component.html',
  // styleUrls: ['./field.component.scss'],
  templateUrl: './field.component.html',
  styleUrls: ['./field.component.scss'],
})
export class FieldComponent implements OnInit {
  @ViewChild('field', { static: true }) field!: ElementRef;

  private jaune: string = '#FFD733';
  private vert: string = '#94D800';
  private voiture: string = '#5E5C1A';
  private silver: string = '#B2B2B2';

  private x_logo!: number;
  private y_logo!: number;
  private size_logo: number = 7.5;

  ngOnInit(): void {
    const canvas: HTMLCanvasElement = this.field.nativeElement;
    const context = canvas.getContext('2d');
    if (context) {
      this.#drawCircle(context, this.jaune, 500, 500);
      this.#drawCar(context, 100, 100);
    }
  }

  #drawCircle(
    context: CanvasRenderingContext2D,
    color: string,
    x: number,
    y: number
  ) {
    context.fillStyle = color;
    context.beginPath();
    context.arc(x, y, 15, (Math.PI / 180) * 0, (Math.PI / 180) * 360);
    context.fill();
  }

  #drawCar(context: CanvasRenderingContext2D, x: number, y: number) {
    // chassis
    context.fillStyle = this.voiture;
    context.fillRect(x - 37.5, y - 10, 75, 15);

    // back wheel
    context.fillStyle = 'black';
    context.beginPath();
    context.arc(x - 17.5, y + 7, 7.5, 0, 2 * Math.PI);
    context.fill();
    context.fillStyle = this.silver;
    context.beginPath();
    context.arc(x - 17.5, y + 7, 3, 0, 2 * Math.PI);
    context.fill();

    // front wheel
    context.fillStyle = 'black';
    context.beginPath();
    context.arc(x + 17.5, y + 7, 7.5, 0, 2 * Math.PI);
    context.fill();
    context.fillStyle = this.silver;
    context.beginPath();
    context.arc(x + 17.5, y + 7, 3, 0, 2 * Math.PI);
    context.fill();

    // cabin
    context.fillStyle = 'black';
    context.beginPath();
    context.moveTo(x - 12.5, y - 17.5);
    context.lineTo(x + 12.5, y - 17.5);
    context.lineTo(x + 22.5, y - 9);
    context.lineTo(x - 22.5, y - 9);
    context.fill();

    // logo
    this.x_logo = x + 32.5;
    this.y_logo = y - 16;
    context.strokeStyle = this.silver;
    context.fillStyle = this.silver;
    context.fillRect(
      this.x_logo - 0.5,
      this.y_logo + this.size_logo / 2 + 1,
      1,
      1
    );
    context.beginPath();
    context.arc(this.x_logo, this.y_logo, this.size_logo / 2, 0, 2 * Math.PI);
    context.stroke();
    context.beginPath();
    context.moveTo(this.x_logo, this.y_logo - this.size_logo / 2);
    context.lineTo(
      this.x_logo - (Math.sqrt(3) / 2) * (this.size_logo * 0.05),
      this.y_logo - 0.5 * (this.size_logo * 0.05)
    );
    context.lineTo(
      this.x_logo - (Math.sqrt(3) / 2) * (this.size_logo / 2),
      this.y_logo + 0.5 * (this.size_logo / 2)
    );
    context.lineTo(this.x_logo, this.y_logo + this.size_logo * 0.05);
    context.lineTo(
      this.x_logo + (Math.sqrt(3) / 2) * (this.size_logo / 2),
      this.y_logo + 0.5 * (this.size_logo / 2)
    );
    context.lineTo(
      this.x_logo + (Math.sqrt(3) / 2) * (this.size_logo * 0.05),
      this.y_logo - 0.5 * (this.size_logo * 0.05)
    );
    context.fill();
  }
}
