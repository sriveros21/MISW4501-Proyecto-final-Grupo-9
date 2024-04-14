import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-inicioOrganizador',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './inicioOrganizador.component.html',
  styleUrls: ['./inicioOrganizador.component.css']
})
export class InicioOrganizadorComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
