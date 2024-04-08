import { Component } from '@angular/core';
import { InputComponent } from '../../shared/input/input.component';
import { ButtonComponent } from '../../shared/button/button.component';

@Component({
  selector: 'app-training-plan',
  standalone: true,
  imports: [InputComponent, ButtonComponent],
  templateUrl: './training-plan.component.html',
  styleUrl: './training-plan.component.css'
})
export class TrainingPlanComponent {

}
