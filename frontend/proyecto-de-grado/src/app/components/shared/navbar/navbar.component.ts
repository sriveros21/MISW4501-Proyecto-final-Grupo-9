import { Component } from '@angular/core';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

}


// import { Component, Input } from '@angular/core';

// @Component({
//   selector: 'app-button',
//   templateUrl: './button.component.html',
//   styleUrls: ['./button.component.css']
// })
// export class ButtonComponent {
//   @Input() type: 'primary' | 'secondary' = 'primary';
//   @Input() text: string = 'Button';
//   @Input() loading: boolean = false;
// }