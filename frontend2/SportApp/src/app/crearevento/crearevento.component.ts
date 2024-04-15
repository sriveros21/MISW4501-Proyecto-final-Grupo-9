import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-crearevento',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './crearevento.component.html',
  styleUrls: ['./crearevento.component.css']
})
export class CreareventoComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
