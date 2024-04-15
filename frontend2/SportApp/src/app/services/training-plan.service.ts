import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';

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

  createPlan(formData: any): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post<any>('http://127.0.0.1:5000/training-plan', formData, { headers })
      .pipe(
        catchError(error => {
          console.error('Error al enviar datos:', error);
          return throwError(error);
        })
      );
  }

}
