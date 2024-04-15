import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-inicioProfesional',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './inicioProfesional.component.html',
  styleUrls: ['./inicioProfesional.component.css']
})
export class InicioProfesionalComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
