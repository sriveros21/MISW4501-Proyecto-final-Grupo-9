import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { TipousuarioComponent } from './tipousuario/tipousuario.component';
import { InicioProfesionalComponent } from './inicioProfesional/inicioProfesional.component';
import { PlantrainingComponent } from './plantraining/plantraining.component';
import { HistorialtrainingComponent } from './historialtraining/historialtraining.component';
import { CreareventoComponent } from './crearevento/crearevento.component';
import { InicioOrganizadorComponent } from './inicioOrganizador/inicioOrganizador.component';

export const routes: Routes = [
  {path: '', component:HomeComponent},
  {path: 'home', component:HomeComponent},
  {path: 'tipousuario', component:TipousuarioComponent},
  {path: 'inicioprofesional', component:InicioProfesionalComponent},
  {path: 'planentrenamiento', component: PlantrainingComponent},
  {path: 'historialentrenamiento', component: HistorialtrainingComponent},
  {path: 'crearevento', component: CreareventoComponent},
  {path: 'inicioorganizador', component: InicioOrganizadorComponent}
];
