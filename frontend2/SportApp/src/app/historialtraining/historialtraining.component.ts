import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { TrainingPlanService } from '../services/training-plan.service';

@Component({
  selector: 'app-historialtraining',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './historialtraining.component.html',
  styleUrls: ['./historialtraining.component.css']
})
export class HistorialtrainingComponent implements OnInit {

  plans: any = {};

  constructor(
    private trainingPlan: TrainingPlanService
  ) { }

  ngOnInit(): void {
    this.getTrainings();
  }

  getTrainings(): void {
    this.trainingPlan.getTrainings().subscribe(
      (response) => {
        this.plans = response;
        console.log(response);
      },
      (error) => {
        console.error('Error al obtener los planes de entrenamiento:', error);
      }
    );
  }

}
