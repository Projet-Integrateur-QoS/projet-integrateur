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

  ngOnInit(): void {
    const canvas: HTMLCanvasElement = this.field.nativeElement;
    const context = canvas.getContext('2d');
    if (context) {
      this.#drawCircle(context, this.jaune, 500, 500);
      this.#drawCar(context);
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
    context.arc(x, y, 20, (Math.PI / 180) * 0, (Math.PI / 180) * 360);
    context.fill();
  }

  #drawCar(context: CanvasRenderingContext2D) {
    // chassis
    context.fillStyle = 'black';
    context.fillRect(40, 65, 110, 25);

    // cabine x : 50, y : 65
    context.beginPath();
    context.moveTo(100, 65);
    context.lineTo(50 + 20, 65);
    context.lineTo(50 + 20 + 15 / 2, 65 + 20);
    context.lineTo(50 + 20 / 2, 65 + 20);
    context.fill();

    // back wheel
    context.fillStyle = 'black';
    context.beginPath();
    context.arc(65, 85, 15, 0, 2 * Math.PI);
    context.fill();

    // front wheel
    context.beginPath();
    context.arc(125, 85, 15, 0, 2 * Math.PI);
    context.fill();
  }
}
