import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-plantraining',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './plantraining.component.html',
  styleUrls: ['./plantraining.component.css']
})
export class PlantrainingComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
