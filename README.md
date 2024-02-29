# Grupo 09 - Proyecto final

A continuación, presentamos el paso a paso para desplegar la aplicación desarrollado y obtener un despliegue como el que se presenta en la imagen a continuación:

![Figura 6](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/a8ec50f1-6c32-4499-9015-3742b325c36c)


## 1. Descargar el repositorio desde github en la siguiente URL: 
           (https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24.)

 **Importante validar que se carguen cada una de las carpetas de los servicios, y sus archivos, como se referencia en la siguiente imagen**

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/186d155e-0acf-4c7e-a9cf-e6867baa0612)

## 2. Crear clúster en GCP.

Antes de crear el clúster en GCP debemos crea las redes que utilizaron el despliegue en general tanto para el clúster como para la base de datos, teniendo en cuenta los siguientes parámetros:

- **Red virtual:** vpn-devnativa-24 
- **Subred (para el clúster de k8s):** red-k8s-devnativa-24
- **Subred para la base de datos:** red-dbs-devnativa-24
- **Rango de direcciones del pod:** 192.168.64.0/21 
- **Rango de direcciones del servicio:** 192.168.72.0/21
- **Dirección de la base de datos:** 192.168.0.3

El **Clúster** se debe crear en la red y la subred definida para este, con: 

- **Nombre:** cluster-devnativa-24

Imagen del cluster una vez a sido creado.

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/41c9a985-4e32-4701-a706-56cbcb3c0e07)


## 3. Crear y subir imagenes de cada unos de los PODs a a GCP.

Par el despliegue se debe contar con el **Container Registry** (activando la API del **Artifact Registry**) y dentro las imágenes de los microservicios que serán desplegado, para ello desde la carpeta del microservicio en el código creamos y subimos las imágenes a el **Container Registry** (siguiendo las intrucciónes del tutorial **Container Registry de la semana 3**). Para nuestro caso el container se llama dev-nativa-24-container y se presenta en la siguiente imagen:

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/66ce8457-997e-4742-af19-b7807a116730)


## 4. Crear base de datos Postgress.

Crear la base de datos en GCP, para lo cual elegimos POSTGRESS, y realizamos la configuracion correspondiente.

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/dc1c4ffa-da5f-4e84-8c0a-7cca643bd5c7)

Instancia de base de datos en postgress.
![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/dd25e911-a4c7-4f67-8655-bf96c574589b)

Desplegar con el siguiente comando el archivo **secrets.yaml** el cual lo encontrará en la raíz del proyecto. Este archivo contiene la información de conexión a la base de datos.

* Ejecutar comando: `kubectl apply -f secrets.yaml` estando conectado al clúster creado.

Asi se debe ver el secret en la seccion de **Kubernets > Secrets y ConfigMaps**

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/9808297d-8736-4c15-a78e-66093bdad655)


## 5. Configuracion del secret en los PODs que necesitan conexión con la base de datos.

Para que los PODS se puedan conectar a la base de datos, es importante realizar la siguiente configuración de **secret** en el archivo de despliegue, 

Ejemplo de como se razalizó la configuración a la base de datos y el nombre de la variable de entorno que se usa en la aplicación en este caso “**DATABASE_URL**”.

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/dcea6218-dec0-4e87-9019-b12f42e6f0f0)

## 6. Crear servicios, funciones e Ingress en GCP.

En la carpeta  “**deployment**” dentro de la solución, se generan 3 archivos *.yaml los cuales contienen la configuración para la creación de los servicios y el **Ingress** de la siguiente manera: 

* **k8s-componentes-entrega-3.yaml**: Este archivo contiene la configuración y despliegue de los servicios credit-card, usermangement.
* **k8s-true-native-deployment.yaml**: Este archivo contiene la configuración y despliegue de los servicios de TrueNative.
* **k8s-ingress-deloyment.yaml**: Contiene la configuración y despliegue del componente Ingress en GCP de los servicios desarrollados para la funcionalidad y de TrueNative.

> IMPORTANTE Tener en cuenta que los servicios internamente se pueden comunicar debido a la configuración del **Service Discovery**, y el cual fue configurado en cada Deployment de los PODs para poder comunicarse dentro del **Cluster** con los servicios que cada uno requiere.
>
> ![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/063d0b1f-9948-42f8-a6f1-b3e8873eaa6e)



* Ejecutar los siguientes comandos en su respectivo orden, para desplegar los **PODs**, los **Servicios**, y crear & configurar el **Ingress** en GCP.

1.	Ejecutar comando:  **`kubectl apply -f k8s-componentes-entrega-3.yaml`**
2.	Ejecutar comando:  **`kubectl apply -f k8s-true-native-deployment.yaml`**


En **Kubernets > Cargas de Trabajo** (Debe ver lo siguiente)

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/30dc1ecc-cd6c-478f-ba21-6cf5f1bf0664)


En **Kubernets > Ingress y Servicios > Servicios (Pestaña)** (Debe ver lo siguiente) 

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/893c1fe8-97f7-41e9-bd4b-029914a0e493)


3.	Ejecutar comando: **kubectl apply -f k8s-ingress-deloyment.yaml**

> IMPORTANTE: Para que ##**Ingress** pueda realizar el **HealtChek** de los servicios que va a exponer, se debe realizar la siguiente configuración en cada uno de los servivios a exponer.
>
> Esta configuración se realiza en **kind: BackendConfig** y  **kind: Service**.
> 
> ![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/39f7cfd2-9548-4b33-b788-a5cbff940633)



Finalmente en **Kubernets > Ingress y Servicios > Ingress (Pestaña)** (Debe ver lo siguiente), este proceso toma bastante tiempo en quedar en estado **OK**, 10-15 min aproximandamente.

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/37a48a9b-ed5d-498c-ba8d-4a2449c74497)


4. **Para crear la función de enviar mail** Ejecutar el siguiente comando.
 
**`gcloud functions deploy funcion-enviar-mail --entry-point enviar_mail --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1`**

Al terminar de correr este comando y si no hay errores en su ejecución, en la seccion de **Cloud Functions de GCP** debe ver lo siguiente:

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/7e56674d-1a04-47e2-9950-5a99df7efa09)

Al entrar al detalle de la funcion debe ver lo siguiente:

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/917b253b-e76c-4040-afe6-8a6245164d61)


## 7. Tomar la IP pública de Ingress.

Una vez finalizado el despliegue del **Ingress**, se debe validar que el estado este en **OK**, lo cual nos indicara que **Ingress** a logrado hacer validación “**Healtcheck**” de todos los servicios expuestos, y nos indicara que el despliegue se ha realizado con éxito.

En la columna **Frontends** se pueden visualizar cada uno de los servicios expuestos y la **IP** pública con la cual vamos a poder realizar las peticiones a nuestro sistema.


![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/f448d361-7a75-4ab8-9d97-d1d3d1712930)


## 8. Configurar en el archivo **config.yaml** la IP tomada de GCP Ingress. (Esto para correr el Pipeline de la entrega 3)

Este paso se debe realizar para que el pipeline pueda correr las pruebas hacia el proyecto correcto y no vaya a generar errores.

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/399562bc-ea3a-4520-b6ba-d092eca6e7d1)


## 9. Pruebas desde postman.

* En su colección de Postman deben ingresar en la sección variables y allí deben colocar en la variable **"INGRESS_PATH"** la **IP** obtenida del **Ingress** en el **punto 7**.

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/ef8bde64-53bb-40de-a3ce-0ee3a8395e09)



* Luego de Configurar la **IP** proceda a ejecutar las pruebas. 

Al realizar la ejecucion de **folder**  o **colecciones** desde postman se debe ver de la siguiente manera. 

![image](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/s202314-proyecto-grupo24/assets/111831086/a25a7f98-9fb4-4dda-b288-68df10a4d5b7)
