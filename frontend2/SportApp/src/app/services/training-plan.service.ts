import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TrainingPlanService {

  constructor(
    private http: HttpClient
  ) { }

  getTrainings(): Observable<any> {
    return this.http.get<any>('http://127.0.0.1:5000/training-plans');
  }

}
